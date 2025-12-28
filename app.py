import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model

MODEL_PATH = "model/plant_disease.h5"

CLASS_NAMES = [
    "Pepper - Bacterial Spot",
    "Pepper - Healthy",
    "Potato - Early Blight",
    "Potato - Healthy",
    "Potato - Late Blight",
    "Tomato - Early Blight",
    "Tomato - Healthy",
    "Tomato - Leaf Mold",
]

st.set_page_config(page_title="Plant Disease Detection", layout="centered")
st.title("🌿 Plant Disease Detection")

model = load_model(MODEL_PATH)

uploaded = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img = img.resize((224, 224))
    arr = np.array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)

    preds = model.predict(arr)[0]
    idx = np.argmax(preds)

    st.subheader(f"Prediction: **{CLASS_NAMES[idx]}**")
    st.write(f"Confidence: **{preds[idx]*100:.2f}%**")
