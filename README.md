# 🌿 Plant Disease Detection using Deep Learning

<p align="center">
  <b>End-to-end Deep Learning project to detect plant leaf diseases</b><br>
  <i>From model training to cloud deployment</i>
</p>

<p align="center">
  🚀 <a href="https://plant-disease-detection-vl4xb8iaffoazkwjtwyfyz.streamlit.app/" target="_blank"><b>Live Demo</b></a>
</p>

---

## 🚀 Project Overview

This project focuses on **automatic plant disease detection** using **Deep Learning and Computer Vision**.  
Users can upload an image of a plant leaf, and the system predicts the disease (or healthy state) along with a confidence score.

🔗 **Live Application:**  
👉 https://plant-disease-detection-vl4xb8iaffoazkwjtwyfyz.streamlit.app/

---

## ❓ Problem Statement

Plant diseases significantly affect agricultural productivity.  
Manual inspection by experts is:
- Time-consuming  
- Error-prone  
- Not scalable  

This project aims to **automate disease detection** using image classification, helping faster and more reliable decision-making.

---

## 🧠 Solution Approach

- Used **Transfer Learning** instead of training from scratch  
- Leveraged **MobileNetV2**, pretrained on ImageNet  
- Fine-tuned the model for plant disease classification  
- Deployed the trained model as a **real-time web application**

---

## 📊 Dataset

- Publicly available plant leaf image dataset  
- Crops included:
  - Potato
  - Tomato
  - Pepper
- Total classes: **8** (Diseased + Healthy)

---

## 🏗 Model Architecture

| Component | Description |
|---------|------------|
| Base Model | MobileNetV2 (Pretrained) |
| Technique | Transfer Learning |
| Input Size | 224 × 224 RGB |
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Regularization | Dropout + Data Augmentation |

---

## 📈 Results

- **Training Accuracy:** ~96%  
- **Validation Accuracy:** ~98%  
- **Overfitting:** Minimal  

Training and validation performance were closely matched, indicating good generalization.

---

## 🖥️ Web Application

The application is built using **Streamlit** and allows users to:
- Upload a plant leaf image  
- View predictions in real time  
- See confidence scores  
- Get warnings for low-confidence / invalid inputs  

🔗 **Live Demo:**  
https://plant-disease-detection-vl4xb8iaffoazkwjtwyfyz.streamlit.app/

---

## 🛠 Tech Stack

- Python  
- TensorFlow / Keras  
- NumPy  
- SciPy  
- Pillow  
- Streamlit  
- Git & GitHub  

---

## 📁 Project Structure


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


