# 🏏 Full Stack DevOps Project — IPL Team Voter

![CI Pipeline](https://github.com/omjaju18/Full_Stack_Devops_Project/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-omjaju18%2Fipl--voter-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5?logo=kubernetes)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-orange?logo=argo)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-F46800?logo=grafana)
![License](https://img.shields.io/badge/License-MIT-green)

> A production-grade, end-to-end DevOps project built from scratch using industry-standard tools.
> Real app. Real pipeline. Real infrastructure. 100% Free.

---

## 📌 Project Overview

This project demonstrates a complete DevOps lifecycle — from writing application code to deploying it on Kubernetes with GitOps and monitoring it with Prometheus, Grafana, and Alertmanager.

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
                          ↓
             Alertmanager → Email alerts
             (HighCPU, HighMemory, PodDown)
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
| **Alerting** | Alertmanager | Email alerts on CPU/Memory/Pod health |

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
- **Alertmanager** — real-time email alerts on infrastructure anomalies

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
│   ├── argocd/
│   │   └── application.yaml      # ArgoCD app manifest
│   └── monitoring/
│       ├── servicemonitor.yaml        # Prometheus scrape config
│       ├── alertmanager-config.yaml   # Email route config
│       └── alert-rules.yaml          # CPU/Memory/Pod alert rules
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

![App UI] <img width="677" height="371" alt="newui" src="https://github.com/user-attachments/assets/192a5a2e-b3d2-48fc-8080-b2ddf290357f" />


---

### ✅ Phase 2 — Docker (Complete)

- Multi-stage Dockerfile
- Non-root user for security
- Gunicorn production server
- Image: `omjaju18/ipl-voter:latest`

![Docker Hub]<img width="709" height="303" alt="docker imahge" src="https://github.com/user-attachments/assets/0db903b8-d61d-4ede-9f0f-24f3ec46a81d" />


---

### ✅ Phase 3 — CI Pipeline (Complete)

- GitHub Actions on every push to `main`
- Auto build + push to Docker Hub
- Tags: `:latest` + `:commit-sha`

![CI Pipeline]<img width="958" height="359" alt="ci pipeline" src="https://github.com/user-attachments/assets/3cf4b98d-0e75-45a7-92f6-dae675a55200" />


---

### ✅ Phase 4 — Helm + Kubernetes (Complete)

- Helm chart with `_helpers.tpl`, `deployment.yaml`, `service.yaml`
- Liveness probe → `/health`, Readiness probe → `/ready`
- NodePort `30007` for local access
- Resource limits: CPU `500m`, Memory `256Mi`
- Deployed to Minikube — 2 pods running

![Helm]<img width="563" height="147" alt="helm" src="https://github.com/user-attachments/assets/61e6359a-cd5c-413f-838d-3a20f898e03e" />

![K8s Pods]<img width="665" height="302" alt="k8final" src="https://github.com/user-attachments/assets/594cc45a-db30-46af-b654-ceea249c37c2" />


---

### ✅ Phase 5 — GitOps with ArgoCD (Complete)

- ArgoCD v3.4.3 installed on Minikube
- Connected to GitHub repo — auto-sync enabled
- Every `git push` = automatic Kubernetes deployment
- `selfHeal: true` — drift auto-corrected
- `prune: true` — removed resources cleaned up

![ArgoCD]<img width="959" height="453" alt="argocdui" src="https://github.com/user-attachments/assets/5a2a323b-4166-41ca-87ab-9d0dcec84120" />


---

### ✅ Phase 6 — CI/CD Pipeline Upgrade (Complete)

- `test` job → flake8 lint + pytest unit tests
- `security-scan` job → Trivy CVE scan on Docker image
- `build` job → Docker build + push (`:latest` + `:sha`)
- `helm-validate` job → helm lint + helm diff
- `update-image-tag` job → updates `values.yaml`, triggers ArgoCD
- `notify` job → Email notification on success/failure

![CI/CD]<img width="956" height="319" alt="cicd" src="https://github.com/user-attachments/assets/ad432288-bbf4-42c6-a6d8-1cfc2106439a" />

![Email Notify]<img width="743" height="290" alt="email" src="https://github.com/user-attachments/assets/522db835-42df-4f60-a613-c136528069a5" />


---

### ✅ Phase 7 — Monitoring + Alerting (Complete)

- `kube-prometheus-stack` Helm chart installed
- Prometheus scrapes `/metrics` from pods via ServiceMonitor
- Grafana dashboard — CPU, Memory, Request Rate, Error Rate
- Alertmanager with Gmail SMTP email alerts
- 3 alert rules: `HighCPUUsage`, `HighMemoryUsage`, `PodNotReady`

![Grafana Dashboard]<img width="959" height="364" alt="grafana" src="https://github.com/user-attachments/assets/bd395ef3-4742-474c-92e3-f806b26ead5a" />

![Prometheus Metrics]<img width="955" height="386" alt="metrics" src="https://github.com/user-attachments/assets/089fd9fb-1056-4f22-88ed-714cd075f91b" />

![Alert Rules]<img width="958" height="441" alt="alerts" src="https://github.com/user-attachments/assets/b571c47c-be5d-4931-b81c-ec053a8971f5" />

![Alert Firing]<img width="958" height="427" alt="alert firing" src="https://github.com/user-attachments/assets/f7d44a04-db75-431c-8d66-b9624000e643" />

![Alert Email]<img width="954" height="404" alt="alert emsil" src="https://github.com/user-attachments/assets/5d26e865-05fb-4938-9ebb-423ad973ea61" />


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
Email Notification 📧
```

---

## 📊 Monitoring Stack

```
Flask App (/metrics)
       ↓
ServiceMonitor (Prometheus scrape every 15s)
       ↓
Prometheus (evaluates alert rules)
       ↓ threshold breached
Alertmanager (routes to email)
       ↓
Gmail alert → omjaju03@gmail.com 📧
```

### Alert Rules

| Alert | Condition | Severity |
|---|---|---|
| `HighCPUUsage` | CPU rate > 0.008 for 1m | warning |
| `HighMemoryUsage` | Memory > 90MB for 1m | warning |
| `PodNotReady` | Pod ready == 0 for 1m | critical |

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

### Install Monitoring Stack

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring --create-namespace

# Apply monitoring configs
kubectl apply -f k8/monitoring/servicemonitor.yaml
kubectl apply -f k8/monitoring/alertmanager-config.yaml
kubectl apply -f k8/monitoring/alert-rules.yaml
```

### Port Forwards (all terminals)

```bash
# App
kubectl port-forward svc/ipl-voter-ipl-voter 8080:80

# Grafana
kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80

# Prometheus
kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus 9090:9090

# ArgoCD
kubectl port-forward svc/argocd-server -n argocd 8081:443
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
| Alertmanager (self-hosted) | $0 |
| **Total** | **$0** |

---

## 🔗 Links

- **GitHub Repo:** https://github.com/omjaju18/Full_Stack_Devops_Project
- **Docker Hub:** https://hub.docker.com/repository/docker/omjaju18/ipl-voter/

---

## 👨‍💻 Author

**Om Jaju** — Building in public, one DevOps tool at a time.

---

## 📄 License

MIT License — feel free to fork and build your own version!
