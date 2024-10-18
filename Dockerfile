FROM python:3.12 AS runner

WORKDIR /app

COPY app.py requirements.txt load.py .

RUN pip install -r requirements.txt

RUN apt-get update 
RUN apt-get install -y libsm6 libxext6 git git-lfs 
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 8000

RUN python3 load.py
RUN ls

CMD ["streamlit", "run", "./app.py", "--server.port", "8000"]
