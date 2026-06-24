🌐 Language:
- 🇺🇸 [English](README.md)
- 🇮🇷 [فارسی](README_FA.md)


# Brain Tumor MRI Classification 🧠

This project is a deep learning system for **brain MRI image classification** into four different categories. It consists of a CNN model based on **Transfer Learning (ResNet)** and a web-based user interface implemented using Streamlit.

<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/1d966ee0-1890-48e8-802a-c05475bf6c9f" />

## 📊 Sample Output

The model output includes:

* Predicted class
* Confidence score for each class
* Confidence bar chart

<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/949bb3c3-40ba-4c97-9826-a7e3c47cf3bf" />

---

## 📌 Prediction Classes

The model classifies brain MRI images into the following four categories:

* Glioma Tumor
* Meningioma Tumor
* Pituitary Tumor
* Normal

---

## 🧠 Overview of the Trained Model (Jupyter Notebook)

This project uses a brain MRI dataset containing images belonging to the four classes listed above.

### Main Steps

### 1. Image Filtering and Data Augmentation

To increase the diversity of the training dataset, several image enhancement and filtering techniques were applied, including:

* Blur
* Sobel
* CLAHE

Experimental results showed that combining the original images with Blur and CLAHE augmented images produced better performance, while Sobel filtering did not improve the model accuracy.

---

### 2. Model Architecture (Transfer Learning)

The model is built using a pre-trained **ResNet** network as the base model.

* Initial layers: Frozen (weights not updated during training)
* Final layers:

  * Dense Layer
  * Softmax Classification Layer with 4 output neurons

Advantages of this approach:

* Better feature extraction
* Reduced training time
* Improved classification accuracy

---

### 3. Model Training

* Early Stopping was employed during training.
* Stopping criterion: Minimum `validation loss`
* Best model selection criterion: Maximum `validation recall`
* Maximum number of epochs: 300

---

### 4. Model Evaluation
 
The final model's accuracy in terms of the recall metric (a crucial metric for healthcare models) was over 99.5 percent. It was also evaluated using test images that were not included in either the training or validation datasets. The results demonstrated excellent performance, and in our test examples, all MRI images were classified correctly.
 

---

## 🌐 Streamlit Web Application

A Streamlit-based web application was developed to provide an interactive interface for the trained model.

### Features

* Upload MRI images
* Automatic image preprocessing (Resize + Normalization)
* Display predicted class
* Display confidence scores for all classes

---

## 📁 Repository Structure

```txt
├── streamlitCNN.py          # Streamlit web application
├── opt1Channelmodel.keras   # Trained model
├── brain-tumor.ipynb        # Training and analysis notebook
├── 1.jpg                    # Streamlit UI screenshot
├── 2.jpg                    # Sample prediction output
└── README.md
```

---

## 🚀 Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/fboloori/BrainTumorDetectionWebApp-MRI.ImageClassification.git
cd BrainTumorDetectionWebApp-MRI.ImageClassification
```

### 2. Run the Streamlit Application

```bash
python -m venv brain_tumor_env
brain_tumor_env\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```
and run the web app by:

```bash
streamlit run streamlitCNN.py
```

Or specify a custom port if needed:

```bash
python -m streamlit run streamlitCNN.py --server.port 8080
```

---

## 📌 Important Notes

* The trained model is already provided in the `.keras` file.
* Retraining the model is not required to run the application.
* Ensure that the model file is located in the same directory as the Python script.
* After launching the Streamlit application, simply upload an MRI image to obtain a prediction.
 

---

## ✨ Technologies Used

* Python
* TensorFlow / Keras
* ResNet (Transfer Learning)
* Streamlit
* NumPy
* Matplotlib
* Pillow (PIL)

--- 
