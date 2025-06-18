
# Hello World Flask App with Docker & Kubernetes

## Project Structure


``` 
.
├── app
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
├── .dockerignore
├── kubernetes
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

## Prerequisites

- Docker Desktop (Windows)
- Minikube or any local Kubernetes cluster
- kubectl CLI
- Python

---

## Build and Run Locally with Docker

1. Build Docker image (run in project root):
   ```
   docker build -t hello-world .
   ```

2. Run container locally:
   ```
   docker run -p 8000:8000 hello-world
   ```

3. Visit [http://localhost:8000](http://localhost:8000) to see the hello message.

---

## Deploy to Kubernetes (Minikube)

1. Start Minikube if not already running:
   ```
   minikube start
   ```

2. Build the Docker image inside Minikube’s Docker daemon:
   ```
   minikube -p minikube docker-env | Invoke-Expression
   docker build -t hello-world .
   ```

3. Apply the Kubernetes manifests:
   ```
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
   ```

4. Check pods and services:
   ```
   kubectl get pods
   kubectl get svc
   ```

5. To access the app:
   - If using Minikube, run:
     ```
     minikube service hello-world-service
     ```
     This will open the service URL in your browser.

5. To stop:
     ```
     minikube stop
     ```


---
