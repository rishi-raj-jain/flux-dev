import os
import streamlit as st
from diffusers import DiffusionPipeline
from huggingface_hub import login, snapshot_download

login(token=os.getenv('HF_TOKEN'))

st.title("AI Image Generation with FLUX.1-schnell")
prompt = st.text_input("Enter your prompt:", "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k")

if st.button("Load Model"):
    with st.spinner("Downloading model..."):
        snapshot_download(repo_id="black-forest-labs/FLUX.1-schnell", cache_dir="./FLUX_1_dev")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        try:
            pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", cache_dir="./FLUX_1_dev")
            image = pipe(prompt).images[0]
            st.image(image, caption=prompt)
        except Exception as e:
            st.error(f"An error occurred: {e}")