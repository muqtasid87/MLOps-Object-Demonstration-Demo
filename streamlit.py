import streamlit as st
import os
import time
from ultralytics import YOLO
from PIL import Image
import numpy as np
import glob
# Load the trained YOLOv8 model
model_path = glob.glob('production_model/*.pt')[0] if glob.glob('production_model/*.pt') else None
model = YOLO(model_path)

st.subheader("**Live E8 East Coast Highway Toll Plaza Monitoring**")

# Toll plaza selection
toll_plaza = st.selectbox("Lebuh Raya Pantai Timur (LPT) E8 Toll Booth Locations:", 
                          ["Chenor", "Gambang", "Jabor", "Karak", "Kuantan", "Lanchang", "Maran", "Temerloh"])

# Create columns for layout
col1, col2 = st.columns([2, 2])  # Adjust column widths as needed

# Placeholders for images and other elements
image_placeholder = col1.empty()  # Left column for the raw image
countdown_placeholder = col1.empty()
progress_bar = col1.progress(0)
link_placeholder = col1.empty()  # Hyperlink in left column
prediction_placeholder = col2.empty()  # Placeholder for the model's predictions (right column)

# Function to get the latest image path
def get_latest_image(plaza_name):
    img_path = f"src/utils/scraper/scraped_images/{plaza_name}.png"
    return img_path if os.path.exists(img_path) else None

# Function to read the timer from the text file
def read_timer():
    try:
        with open("src/utils/scraper/scraped_images/timer/timer.txt", "r") as file:
            return int(file.read().strip())
    except Exception as e:
        st.error("Error reading timer: " + str(e))
        return 0

# Function to run model inference on the image
def run_inference(image_path):
    img = Image.open(image_path)
    img_np = np.array(img)

    # Run YOLOv8 inference
    results = model(img_np)

    # Draw bounding boxes and labels on the image
    annotated_image = results[0].plot()  # Get the rendered image with bounding boxes
    
    return annotated_image

# Auto-refresh logic
while True:
    # Read the timer value
    remaining_time = read_timer()

    # Start countdown if the remaining time is below 30
    if remaining_time < 30:
        # Update the displayed image on the left
        latest_image_path = get_latest_image(toll_plaza)
        if latest_image_path:
            # Display the raw image on the left column
            image_placeholder.image(latest_image_path, caption=f"{toll_plaza} Toll Plaza on E8 Highway", width=350)
            
            # Set caption as a hyperlink to the specified URL
            link_placeholder.markdown("[View Source](https://www.llm.gov.my/awam/cctv)", unsafe_allow_html=True)
            
            # Run inference and update the right column with the prediction
            annotated_image = run_inference(latest_image_path)
            prediction_placeholder.image(annotated_image, caption="Model Predictions", width=350)
        else:
            image_placeholder.error("Image not found.")
        
        # Update countdown text
        countdown_placeholder.text(f"Updating image in {remaining_time} seconds")
        
        # Update progress bar based on remaining time
        progress = (30 - remaining_time) / 30  # Normalizing to a range of 0 to 1
        progress_bar.progress(progress)
    else:
        # If the time is not below 30, just show the image and a message
        countdown_placeholder.text("Fetching Image from CCTV...")

    # Refresh every second
    time.sleep(1)

    # Use a stop mechanism (optional)
    if st.session_state.get('stop_loop', False):
        break
