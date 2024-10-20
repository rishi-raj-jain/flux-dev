FROM python:3.12 AS runner

WORKDIR /app

COPY app.py requirements.txt .

RUN pip install -r requirements.txt --root-user-action=ignore
RUN pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu121 --root-user-action=ignore

RUN apt-get update 
RUN apt-get install -y libsm6 libxext6 git git-lfs cuda-toolkit
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 8000

ARG HF_TOKEN
CMD ["streamlit", "run", "./app.py", "--server.port", "8000"]