FROM python:3.10

WORKDIR /app

COPY --chown=1000:1000 requirements.txt .

RUN pip install \
      --no-cache \
      --requirement requirements.txt

COPY --chown=1000:1000 . .