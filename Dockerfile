FROM python:3.12 AS builder

WORKDIR /app

COPY . .

RUN python3 -m venv .venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -e ".[all]"

FROM python:3.12 AS runner

WORKDIR /app

COPY --from=builder /app /app

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8000

CMD ["streamlit", "run", "./demo_st.py", "--server.port", "8000"]
