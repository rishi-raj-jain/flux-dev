import os
from huggingface_hub import login, snapshot_download

login(token=os.getenv('HF_TOKEN'))
snapshot_download(repo_id="black-forest-labs/FLUX.1-dev", cache_dir="./FLUX_1_dev")

print('Done')
