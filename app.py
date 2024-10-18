import os
import streamlit as st
from diffusers import DiffusionPipeline
from huggingface_hub import login, snapshot_download

login(token=os.getenv('HF_TOKEN'))
snapshot_download(repo_id="black-forest-labs/FLUX.1-dev", cache_dir="./FLUX_1_dev")

pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", cache_dir="FLUX_1_dev", local_files_only=True)

st.title("AI Image Generation with FLUX.1-dev")
prompt = st.text_input("Enter your prompt:", "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        image = pipe(prompt).images[0]
        st.image(image, caption=prompt)
