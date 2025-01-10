FROM python:3.12-slim-bullseye

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

# Run the application.
ENV ENV_MODE="PROD"
CMD ["/app/.venv/bin/uvicorn", "app.main:app","--port", "8000", "--host", "0.0.0.0"]
