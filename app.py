import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image

MODEL_PATH = "best.pt"
if not os.path.exists(MODEL_PATH):

    url = "https://drive.google.com/uc?id=1zsZYO1tJlWHaOidtIxKJsYk93VIm_DgP"
    gdown.download(url, MODEL_PATH, quiet=False)

model = YOLO(MODEL_PATH)

st.title("Kidney Stone Detection System")

uploaded_file = st.file_uploader("Upload Kidney Image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(img)

    results = model(img_array)

    boxes = results[0].boxes
    result_img = results[0].plot()

    st.image(result_img, caption="Detection Result")

    if boxes is not None and len(boxes) > 0:
        confidences = boxes.conf.cpu().numpy()
        max_conf = max(confidences)

        st.success("✅ Kidney Stone Present")
        st.info(f"Confidence Score: {max_conf*100:.2f}%")

    else:
        st.error("❌ No Kidney Stone Detected")import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image

model = YOLO("best.pt")

st.title("Kidney Stone Detection System")

uploaded_file = st.file_uploader("Upload Kidney Image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(img)

    results = model(img_array)

    boxes = results[0].boxes
    result_img = results[0].plot()

    st.image(result_img, caption="Detection Result")

    if boxes is not None and len(boxes) > 0:
        confidences = boxes.conf.cpu().numpy()
        max_conf = max(confidences)

        st.success("✅ Kidney Stone Present")
        st.info(f"Confidence Score: {max_conf*100:.2f}%")

    else:

        st.error("❌ No Kidney Stone Detected")
