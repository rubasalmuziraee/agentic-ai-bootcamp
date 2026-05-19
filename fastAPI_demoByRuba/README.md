## Instructions
### 1. Start server locally (A) or locally with Docker (B)
```bash
### A. Locally
uvicorn main:app --reload --host 0.0.0.0 --port 80
```
```bash
### B. Locally with Docker

# Build a Docker image
docker build -t wecloud-iris-ml-build-image .

# Run image as a Docker container
docker run -d -p 80:80 --name wecloud-iris-api wecloud-iris-ml-build-image
```
### 2. Go to url at localhost or http://127.0.0.1