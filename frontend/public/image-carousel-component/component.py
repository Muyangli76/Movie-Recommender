import os
import streamlit as st
import random

# Define the custom component's frontend logic
def image_carousel_component(image_urls, height=300):
    if not image_urls:
        st.error("No image URLs provided for the carousel.")
        return
    
    # Load images from local path if available
    image_path = os.path.join(os.getcwd(), 'frontend', 'public', 'image-carousel-component', 'TopMovie.jpeg')
    
    if os.path.exists(image_path):
        st.image(image_path, caption="Local Movie Image", width=600, use_column_width=True)
    else:
        st.error("Image not found. Please check the path.")
        
    return image_path  # You can return the local image path or URL if needed

# Register the component with Streamlit
def declare_component(*args, **kwargs):
    return image_carousel_component
