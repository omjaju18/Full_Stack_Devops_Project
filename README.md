# 🏏 Full Stack DevOps Project — IPL Team Voter

![CI Pipeline](https://github.com/omjaju18/Full_Stack_Devops-Project/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-omjaju18%2Fipl--voter-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5?logo=kubernetes)
![License](https://img.shields.io/badge/License-MIT-green)

> A production-grade, end-to-end DevOps project built from scratch using industry-standard tools.  
> Real app. Real pipeline. Real infrastructure. 100% Free.

---

## 📌 Project Overview

This project demonstrates a complete DevOps lifecycle — from writing application code to deploying it on Kubernetes with GitOps, monitoring it with Prometheus & Grafana, and provisioning cloud infrastructure with Terraform.

The application itself is an **IPL Team Voter** — users can vote for their favourite IPL team in real time, with a live leaderboard and persistent vote storage.

---

## 🏗️ Architecture

```
Developer → Git Push → GitHub
                          ↓
                   GitHub Actions CI
                          ↓
              Build Multi-Stage Docker Image
                          ↓
                 Push to Docker Hub
                          ↓
                  ArgoCD (GitOps)
                  watches GitHub repo
                          ↓
             Deploy to Kubernetes (Minikube)
             via Helm Chart
                          ↓
              Prometheus scrapes /metrics
                          ↓
             Grafana Dashboards (CPU, Memory,
             Request Rate, Error Rate)
                          ↓
              Terraform provisions AWS
              Free Tier infrastructure
```

---

## 🛠️ Tech Stack

| Category | Tool | Purpose |
|---|---|---|
| **Language** | Python 3.12 + Flask | REST API + UI |
| **Database** | SQLite → PostgreSQL | Vote persistence |
| **Version Control** | Git + GitHub | Source control |
| **Containerization** | Docker | Multi-stage image build |
| **Registry** | Docker Hub | Container image storage |
| **CI** | GitHub Actions | Auto build + push on every commit |
| **CD** | ArgoCD | GitOps, auto-deploy on git push |
| **Packaging** | Helm | Kubernetes app packaging |
| **Orchestration** | Kubernetes (Minikube) | Container orchestration |
| **Monitoring** | Prometheus | Metrics scraping |
| **Dashboards** | Grafana | Live observability dashboards |
| **Alerting** | Alertmanager | Alert on CPU/memory/errors |
| **IaC** | Terraform | AWS infrastructure as code |
| **Cloud** | AWS Free Tier | EC2, S3, VPC |

---

## ✅ Production Best Practices Used

- **Multi-stage Dockerfile** — builder stage + minimal runtime stage
- **Non-root user** inside container — security hardened
- **Gunicorn** as WSGI server — never Flask dev server in production
- **Conventional Commits** — `feat()`, `fix()`, `chore()` on every commit
- **GitHub Actions Secrets** — zero hardcoded credentials anywhere
- **Image tagging** — `:latest` + `:commit-SHA` for full traceability
- **Health endpoints** — `/health` (liveness) + `/ready` (readiness) for Kubernetes
- **Prometheus metrics** — `/metrics` endpoint baked in from day one
- **Persistent storage** — SQLite with Kubernetes PersistentVolumeClaim
- **Helm values.yaml** — single file controls all config, no hardcoded YAML
- **GitOps with ArgoCD** — git is the single source of truth for deployments
- **Resource limits** — CPU and memory limits on every Kubernetes pod

---

## 📁 Project Structure

```
Full-Stack-Devops-Project/
│
├── app/                          # Application code
│   ├── app.py                    # Flask API + routes
│   ├── requirements.txt          # Python dependencies
│   ├── Dockerfile                # Multi-stage Docker build
│   └── templates/
│       └── index.html            # Dark-themed voting UI
│
├── k8s/                          # Kubernetes manifests
│   └── helm/
│       └── ipl-voter/
│           ├── Chart.yaml        # Helm chart metadata
│           ├── values.yaml       # All config in one place
│           └── templates/
│               ├── deployment.yaml
│               ├── service.yaml
│               ├── ingress.yaml
│               └── pvc.yaml      # Persistent volume claim
│
├── argocd/                       # ArgoCD application manifest
│   └── application.yaml
│
├── monitoring/                   # Prometheus + Grafana
│   ├── prometheus-values.yaml
│   └── grafana-dashboard.json
│
├── terraform/                    # AWS Infrastructure as Code
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions CI pipeline
│
├── .gitignore
└── README.md
```

---

## 🚀 Phases

### ✅ Phase 1 — Application (Complete)
- Python Flask REST API
- 10 IPL teams with real-time voting
- SQLite persistence — votes survive container restarts
- Live leaderboard with vote percentage bars
- Routes: `/`, `/ui`, `/vote/<team>`, `/results`, `/health`, `/ready`, `/metrics`

### ✅ Phase 2 — Docker (Complete)
- Multi-stage Dockerfile
- Non-root user for security
- Gunicorn production server
- Image: `omjaju18/ipl-voter:latest`

### ✅ Phase 3 — CI Pipeline (Complete)
- GitHub Actions on every push to `main`
- Auto build + push to Docker Hub
- Tags: `:latest` + `:commit-sha`

### 🔄 Phase 4 — CD with Kubernetes + Helm (In Progress)
- Helm chart for Kubernetes deployment
- Deploy to Minikube locally
- PersistentVolumeClaim for SQLite storage
- Liveness + readiness probes configured

### ⏳ Phase 5 — GitOps with ArgoCD (Upcoming)
- ArgoCD installed on Minikube
- Watches GitHub repo automatically
- Every git push = automatic Kubernetes deployment
- No manual `kubectl apply` ever

### ⏳ Phase 6 — Monitoring (Upcoming)
- `kube-prometheus-stack` Helm chart
- Prometheus scrapes pod metrics
- Grafana dashboard — CPU, memory, request rate, error rate
- Alertmanager → Slack/email alerts

### ⏳ Phase 7 — Infrastructure as Code (Upcoming)
- Terraform provisions AWS Free Tier
- VPC + EC2 t2.micro + Security Groups + S3
- LocalStack for local AWS simulation (zero cost)

---

## ⚙️ Local Setup

### Prerequisites
- Docker
- Python 3.12+
- Minikube
- Helm 3
- kubectl
- Git

### Run locally (without Docker)
```bash
cd app
pip install -r requirements.txt
python app.py
# Visit http://localhost:5000/ui
```

### Run with Docker
```bash
docker build -t ipl-voter:local ./app
docker run -p 5000:5000 ipl-voter:local
# Visit http://localhost:5000/ui
```

### Deploy to Minikube with Helm
```bash
# Start Minikube
minikube start --cpus=2 --memory=4096
minikube addons enable ingress

# Deploy using Helm
helm install ipl-voter ./k8s/helm/ipl-voter

# Check pods
kubectl get pods
kubectl get svc

# Access the app
minikube service ipl-voter --url
```

### Install ArgoCD
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Get admin password
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d

# Access UI
kubectl port-forward svc/argocd-server -n argocd 8080:443
# Visit https://localhost:8080
```

### Install Prometheus + Grafana
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace

# Access Grafana
kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80
# Visit http://localhost:3000 (admin / prom-operator)
```

---

## 🔁 CI/CD Flow

```
git push origin main
       ↓
GitHub Actions triggers
       ↓
pip install dependencies
       ↓
docker build (multi-stage)
       ↓
docker push → Docker Hub
  omjaju18/ipl-voter:latest
  omjaju18/ipl-voter:<sha>
       ↓
ArgoCD detects change in repo
       ↓
helm upgrade → Kubernetes
       ↓
New pods rolling deployed ✅
```

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | App info + team list |
| GET | `/ui` | Voting UI |
| POST | `/vote/<team>` | Cast a vote |
| GET | `/results` | Leaderboard + winner |
| GET | `/health` | Liveness probe |
| GET | `/ready` | Readiness probe |
| GET | `/metrics` | Prometheus metrics |

---

## 💰 Cost

| Tool | Cost |
|---|---|
| GitHub + GitHub Actions | $0 |
| Docker Hub | $0 |
| Minikube (local) | $0 |
| ArgoCD (self-hosted) | $0 |
| Prometheus + Grafana (self-hosted) | $0 |
| AWS Free Tier (12 months) | $0 |
| LocalStack (local AWS simulation) | $0 |
| **Total** | **$0** |

---

## 🔗 Links

- **GitHub Repo:** https://github.com/omjaju18/Full_Stack_Devops-Project
- **Docker Hub:** https://hub.docker.com/r/omjaju18/ipl-voter

---

## 👨‍💻 Author

**Om Jaju** — Building in public, one DevOps tool at a time.

Follow the journey on LinkedIn for Part 2 (CD + ArgoCD + Monitoring)!

---

## 📄 License

MIT License — feel free to fork and build your own version!
