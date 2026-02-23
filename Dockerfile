FROM python:3.12-alpine
RUN apk add --no-cache git
COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["python", "/entrypoint.py"]
