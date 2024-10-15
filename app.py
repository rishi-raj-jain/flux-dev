import os
import streamlit as st
from huggingface_hub import login
from diffusers import DiffusionPipeline

login(token=os.getenv('HF_TOKEN'))
pipe = DiffusionPipeline.from_pretrained("./FLUX.1-dev")

st.title("AI Image Generation with FLUX.1-dev")
prompt = st.text_input("Enter your prompt:", "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        image = pipe(prompt).images[0]
        st.image(image, caption=prompt)
