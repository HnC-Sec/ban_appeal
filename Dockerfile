FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV DISCORD_WEBHOOK_URL=""
ENV DISCORD_CLIENT_ID=""
ENV DISCORD_CLIENT_SECRET=""

COPY src/ /app
COPY pyproject.toml .python-version /app/

WORKDIR /app

RUN uv python install 3.13 &&\
    uv sync

CMD ["uv", "run", "uvicorn", "ban_appeal.__main__:app", "--host", "0.0.0.0"]