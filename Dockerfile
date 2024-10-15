FROM python:3.12 AS builder

WORKDIR /app

COPY . .

RUN python3 -m venv .venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -e ".[all]"

FROM python:3.12 AS runner

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app /app

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8000

CMD ["streamlit", "run", "./demo_st.py", "--server.port", "8000"]
