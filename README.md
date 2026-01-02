# 🌿 Plant Disease Detection using Deep Learning

<p align="center">
  <b>End-to-end Deep Learning project to detect plant leaf diseases</b><br>
</p>

---

## 🚀 Project Overview

This project focuses on **automatic plant disease detection** using **Deep Learning and Computer Vision**.  
Users can upload an image of a plant leaf, and the system predicts the disease (or healthy state) along with a confidence score.

The complete pipeline covers:
- Dataset handling
- CNN-based model training
- Real-time inference
- Web deployment

---

## ❓ Problem Statement

Plant diseases significantly affect agricultural productivity.  
Manual inspection by experts is:
- Time-consuming
- Error-prone
- Not scalable

This project aims to **automate disease detection** using image classification, helping farmers and researchers make faster decisions.

---

## 🧠 Solution Approach

- Used **Transfer Learning** instead of training from scratch
- Leveraged **MobileNetV2**, pretrained on ImageNet
- Fine-tuned the model for plant disease classification
- Deployed the trained model as a **web application**

---

## 📊 Dataset

- Publicly available plant leaf image dataset
- Crops included:
  - Potato
  - Tomato
  - Pepper
- Total classes: **8**
  - Diseased + Healthy leaves

Dataset was split into:
- Training set
- Validation set

---

## 🏗 Model Architecture

| Component | Description |
|---------|------------|
| Base Model | MobileNetV2 (pretrained) |
| Technique | Transfer Learning |
| Input Size | 224 × 224 RGB |
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Regularization | Dropout + Data Augmentation |

---

## 🧪 Training Highlights

- Image preprocessing and normalization
- Data augmentation (rotation, flipping)
- Frozen base layers to reduce overfitting
- Fine-tuned custom classification head

### 📈 Results
- **Training Accuracy:** ~96%
- **Validation Accuracy:** ~98%
- **Overfitting:** Minimal (train & validation accuracy closely matched)

---

## 🖥️ Web Application

The trained model is deployed using **Streamlit**.

### Features:
- Upload leaf image
- Real-time prediction
- Confidence score display
- Confidence-based rejection for invalid/random images

> Predictions below a confidence threshold are flagged as unreliable.

---

## 🛠 Tech Stack

- **Python**
- **TensorFlow / Keras**
- **NumPy**
- **SciPy**
- **Pillow**
- **Streamlit**
- **Git & GitHub**

---

## 📁 Project Structure

plant_disease_project/
├── app.py # Streamlit web app
├── train_model.py # Model training script
├── model/
│ └── plant_disease.h5 # Trained CNN model
├── requirements.txt
└── README.md



---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/USERNAME/plant-disease-detection.git
cd plant-disease-detection
pip install -r requirements.txt
streamlit run app.py

