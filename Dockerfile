FROM python:3.12-alpine

WORKDIR /code

RUN apk add --no-cache \
    build-base \
    cargo \
    g++ \
    libffi-dev \
    libgcc \
    libstdc++ \
    openssl-dev \
    python3-dev \
    tzdata && \
    rm -rf /var/cache/apk/*

ENV TZ=America/Sao_Paulo

RUN adduser -D appuser

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry config virtualenvs.in-project false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --with dev

COPY . .

EXPOSE 8000

RUN chown -R appuser:appuser /code

USER appuser

RUN chmod +x ./scripts/start.sh

CMD ["./scripts/start.sh"]
