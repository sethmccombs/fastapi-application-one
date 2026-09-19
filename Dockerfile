FROM python:3.14.7-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY app ./app

EXPOSE 8080

CMD ["uv", "run", "fastapi", "run", "app/main.py", "--port", "8080"]
