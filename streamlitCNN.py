import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import keras
import matplotlib.pyplot as plt

# Load the pre-trained model
model = tf.keras.models.load_model('opt1Channelmodel.h5') 
 


# Define the class labels

class_indices = {"glioma_tumor":0 , "meningioma_tumor":1 , "normal":2 , "pituitary_tumor":3}
TARGET_SIZE = (224,224)

# Function to preprocess the image
def preprocess_image(image):
    resized_image = image.resize(TARGET_SIZE)  # Resize the image to match the input size of the CNN model
    normalized_image = tf.keras.preprocessing.image.img_to_array(resized_image) / 255.0  # Normalize the image
    return tf.expand_dims(normalized_image, axis=0)  # Add an extra dimension for batch

# Function to make predictions
def predict(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)[0]
    predicted_class_index = np.argmax(predictions)  # Get the index of the predicted class 
    for key, value in class_indices.items():
        if value == predicted_class_index:
            predicted_class=key
    confidence = class_indices.copy()
    for key in  confidence.keys(): 
        confidence[key]= predictions[confidence[key]]
    return predicted_class, confidence    

# App
st.title("Image Classification App")
st.write("Upload an image and get it classified!")

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])





if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=False , width=300  )

    # Make predictions
    if st.button('Classify'):
        predicted_class, confidence = predict(image)
        #st.write("Predicted Class:", predicted_class)
        fig, ax = plt.subplots()
        fig.set_size_inches(7 , 2)
        ax.bar(list(confidence.keys()), list(confidence.values()))
        ax.set_ylabel('Values')
        st.write('Confidence Plot:')
        plt.suptitle("Predicted Class:"+ predicted_class)
        st.pyplot(fig) 


# python -m streamlit run streamlitCNN.py --server.port 8080