import os
import torch
import streamlit as st
from diffusers import DiffusionPipeline
from huggingface_hub import login, snapshot_download

login(token=os.getenv('HF_TOKEN'))

st.title("AI Image Generation with FLUX.1-dev")
prompt = st.text_input("Enter your prompt:", "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k")
num_inference_steps = st.number_input("Enter number of inference steps:", min_value=1, value=3)

if st.button("Load Model"):
    with st.spinner("Downloading model..."):
        snapshot_download(repo_id="black-forest-labs/FLUX.1-dev", cache_dir="./FLUX_1_dev")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        try:
            pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.float16, use_safetensors=True, cache_dir="./FLUX_1_dev").to("cuda")
            images = pipe(prompt=prompt, num_inference_steps=num_inference_steps).images
            for i, image in enumerate(images):
                st.image(image, caption=f"{prompt} - Image {i+1}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
