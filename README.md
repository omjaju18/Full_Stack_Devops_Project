# 🏏 Full Stack DevOps Project — IPL Team Voter

![CI Pipeline](https://github.com/omjaju18/Full_Stack_Devops-Project/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-omjaju18%2Fipl--voter-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5?logo=kubernetes)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-orange?logo=argo)
![License](https://img.shields.io/badge/License-MIT-green)

> A production-grade, end-to-end DevOps project built from scratch using industry-standard tools.  
> Real app. Real pipeline. Real infrastructure. 100% Free.

---

## 📌 Project Overview

This project demonstrates a complete DevOps lifecycle — from writing application code to deploying it on Kubernetes with GitOps and monitoring it with Prometheus & Grafana.

The application itself is an **IPL Team Voter** — users can vote for their favourite IPL team in real time, with a live leaderboard and persistent vote storage.

---

## 🏗️ Architecture

```
Developer → Git Push → GitHub
                          ↓
                   GitHub Actions CI
                   ├── Lint (flake8)
                   ├── Tests (pytest)
                   ├── Security Scan (Trivy)
                   ├── Docker Build + Push
                   ├── Helm Lint + Diff
                   └── Update values.yaml (image tag)
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
```

---

## 🛠️ Tech Stack

| Category | Tool | Purpose |
|---|---|---|
| **Language** | Python 3.12 + Flask | REST API + UI |
| **Database** | SQLite | Vote persistence |
| **Version Control** | Git + GitHub | Source control |
| **Containerization** | Docker | Multi-stage image build |
| **Registry** | Docker Hub | Container image storage |
| **CI** | GitHub Actions | Auto build + push on every commit |
| **CD** | ArgoCD | GitOps, auto-deploy on git push |
| **Packaging** | Helm v3.19 | Kubernetes app packaging |
| **Orchestration** | Kubernetes (Minikube v1.37) | Container orchestration |
| **Monitoring** | Prometheus + Grafana | Metrics + Dashboards |

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
- **Helm values.yaml** — single file controls all config, no hardcoded YAML
- **GitOps with ArgoCD** — git is the single source of truth for deployments
- **Resource limits** — CPU and memory limits on every Kubernetes pod
- **Helm lint + diff** — chart validated before every deploy
- **Trivy security scan** — CVE scan on every Docker image before push
- **pytest + coverage** — unit tests run before every build

---

## 📁 Project Structure

```
Full-Stack-Devops-Project/
│
├── app/                          # Application code
│   ├── app.py                    # Flask API + routes
│   ├── requirements.txt          # Python dependencies
│   ├── Dockerfile                # Multi-stage Docker build
│   ├── templates/
│   │   └── index.html            # Dark-themed voting UI
│   └── tests/
│       ├── conftest.py           # pytest fixtures
│       └── test_app.py           # unit tests
│
├── k8/                           # Kubernetes manifests
│   ├── helm/
│   │   └── ipl-voter/
│   │       ├── Chart.yaml        # Helm chart metadata
│   │       ├── values.yaml       # All config in one place
│   │       └── templates/
│   │           ├── _helpers.tpl  # Helm named templates
│   │           ├── deployment.yaml
│   │           └── service.yaml
│   └── argocd/
│       └── application.yaml      # ArgoCD app manifest
│
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions CI/CD pipeline
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

### ✅ Phase 4 — Helm + Kubernetes (Complete)
- Helm chart with `_helpers.tpl`, `deployment.yaml`, `service.yaml`
- Liveness probe → `/health`, Readiness probe → `/ready`
- NodePort `30007` for local access
- Resource limits: CPU `500m`, Memory `256Mi`
- Deployed to Minikube — 2 pods running

### ✅ Phase 5 — GitOps with ArgoCD (Complete)
- ArgoCD v3.4.3 installed on Minikube
- Connected to GitHub repo — auto-sync enabled
- Every `git push` = automatic Kubernetes deployment
- `selfHeal: true` — drift auto-corrected
- `prune: true` — removed resources cleaned up

### ✅ Phase 6 — CI/CD Pipeline Upgrade (Complete)
- `test` job → flake8 lint + pytest unit tests
- `security-scan` job → Trivy CVE scan on Docker image
- `build` job → Docker build + push (`:latest` + `:sha`)
- `helm-validate` job → helm lint + helm diff
- `update-image-tag` job → updates `values.yaml`, triggers ArgoCD
- `notify` job → Slack notification on success/failure

### ⏳ Phase 7 — Monitoring (Upcoming)
- `kube-prometheus-stack` Helm chart
- Prometheus scrapes `/metrics` from pods
- Grafana dashboard — CPU, memory, request rate, error rate
- Alertmanager → Slack/email alerts

---

## 🔁 CI/CD Flow

```
git push origin main
       ↓
Lint + Tests (flake8 + pytest)
       ↓ fail = stop
Trivy Security Scan
       ↓ fail = stop
Docker Build + Push to Hub
  omjaju18/ipl-voter:latest
  omjaju18/ipl-voter:<sha>
       ↓
Helm Lint + Helm Diff
       ↓ fail = stop
Update values.yaml (image tag)
       ↓
ArgoCD detects change
       ↓
helm upgrade → Kubernetes
       ↓
New pods rolling deployed ✅
       ↓
Slack Notification 📢
```

---

## ⚙️ Local Setup

### Prerequisites
- Docker
- Python 3.12+
- Minikube v1.37+
- Helm v3.19+
- kubectl v1.29+
- Git

### Run locally (without Docker)
```bash
cd app
python3 -m venv venv
source venv/bin/activate
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

### Run Tests
```bash
cd app
source venv/bin/activate
pip install pytest pytest-cov
pytest tests/ -v
```

### Deploy to Minikube with Helm
```bash
minikube start
helm install ipl-voter ./k8/helm/ipl-voter
kubectl get pods
kubectl port-forward svc/ipl-voter-ipl-voter 8080:80
# Visit http://localhost:8080/ui
```

### Install ArgoCD
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d
kubectl port-forward svc/argocd-server -n argocd 8081:443
# Visit https://localhost:8081 (admin / <password above>)
```

### Apply ArgoCD Application
```bash
kubectl apply -f k8/argocd/application.yaml
kubectl get application -n argocd
```

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | App info + team list (JSON) |
| GET | `/ui` | Voting UI |
| GET | `/vote/<team>` | Cast a vote |
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
| **Total** | **$0** |

---

## 🔗 Links

- **GitHub Repo:** https://github.com/omjaju18/Full_Stack_Devops-Project
- **Docker Hub:** https://hub.docker.com/r/omjaju18/ipl-voter

---

## 👨‍💻 Author

**Om Jaju** — Building in public, one DevOps tool at a time.

---

## 📄 License

MIT License — feel free to fork and build your own version!
