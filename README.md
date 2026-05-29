# DevOps Observability Project

## End-to-end CI/CD & Monitoring on Kubernetes

### Architecture Diagram

```mermaid
graph TD
    Developer[👨‍💻 Developer] -->|git push| GitHub
    GitHub -->|trigger| GitHubActions
    GitHubActions -->|docker build & push| DockerHub
    DockerHub -->|pull image| Minikube
    Minikube -->|helm install| Helm
    Helm -->|deploy| Pods[Flask App Pods]
    Pods -->|metrics| Prometheus
    Prometheus -->|visualize| Grafana
    Pods -->|logs| Kubectl[kubectl logs]
    Grafana -->|dashboard| User[👁️ Monitor]
