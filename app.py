import os, torch, streamlit
from diffusers import FluxPipeline
from huggingface_hub import login, snapshot_download

login(token=os.getenv('HF_TOKEN'))

streamlit.title("AI Image Generation with FLUX.1-dev")
num_width = streamlit.number_input("Enter number of width:", min_value=1, value=256)
num_height = streamlit.number_input("Enter number of height:", min_value=1, value=256)
num_images = streamlit.number_input("Enter number of images:", min_value=1, value=3)
num_inference_steps = streamlit.number_input("Enter number of inference steps:", min_value=1, value=3)
prompt = streamlit.text_input("Enter your prompt:", "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k")

if streamlit.button("Load Model"):
    snapshot_download(repo_id="black-forest-labs/FLUX.1-dev", cache_dir="./FLUX_1_dev")

if streamlit.button("Generate Image"):
    pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16, cache_dir="./FLUX_1_dev")
    images = pipe(prompt=prompt, num_inference_steps=num_inference_steps, height=num_height, width=num_width, num_images_per_prompt=num_images).images
    for i, image in enumerate(images):
        streamlit.image(image, caption=prompt)