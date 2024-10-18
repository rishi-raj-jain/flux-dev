FROM python:3.12 AS builder

WORKDIR /app

COPY app.py .
COPY load.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python3 ./load.py

FROM python:3.12 AS runner

WORKDIR /app

COPY --from=builder app.py app.py
COPY --from=builder load.py load.py

RUN apt-get update 
RUN apt-get install -y libsm6 libxext6 git git-lfs 
RUN rm -rf /var/lib/apt/lists/*

# RUN git lfs install
# ARG HF_TOKEN
# RUN git clone https://RishiRajJain:$HF_TOKEN@huggingface.co/black-forest-labs/FLUX.1-dev

EXPOSE 8000

CMD ["streamlit", "run", "./app.py", "--server.port", "8000"]
