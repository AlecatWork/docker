from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Docker!", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}



# 1. when you docker run the same image twice, docker creates 2 separate containers from that single image, each with its own environment and container ID.
# 2. Files created inside a container persists when the container stops.
# 3. the -p flag maps a port on your host machine to a port inside the container