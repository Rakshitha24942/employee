
# 🚀 Automated Employee Onboarding System Using CI/CD Pipeline

## 📌 Project Overview

This project simulates a real-world DevOps workflow for deploying a simple web application that helps HR personnel onboard new employees. The system is built using Python (Flask) and integrates a fully automated CI/CD pipeline for testing, containerization, deployment, and notifications.

## 🧰 Tech Stack

- **Backend**: Python (Flask)
- **Version Control**: Git & GitHub
- **CI/CD Tools**: GitHub Actions / Jenkins
- **Containerization**: Docker, Docker Hub
- **Deployment**: Kubernetes (Minikube/Kind) / Docker Compose
- **Notifications**: Slack Webhook / SMTP Email

## 💻 Running the App Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/employee-onboarding.git
   cd employee-onboarding
   ```

2. **Set up the environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```

Access the app at: [http://localhost:5000](http://localhost:5000)

## 🔁 CI/CD Pipeline

This project uses GitHub Actions for continuous integration and delivery. The pipeline executes on every push to the `main` branch and includes:

- ✅ **Code Linting**: Using `pylint` to maintain code quality.
- ✅ **Unit Testing**: Ensures application starts and endpoints respond.
- ✅ **Docker Build**: Creates a Docker image of the app.
- ✅ **Docker Push**: Uploads the image to Docker Hub.
- ✅ **Deployment**: Deploys to a local Kubernetes cluster or via Docker Compose.
- ✅ **Notifications**: Sends alerts to Slack or Email about build/deploy status.

Workflow File: `.github/workflows/main.yml`

## 🐳 Docker Deployment

1. **Build and run the app**
   ```bash
   docker-compose up --build
   ```

2. **Access** the app at [http://localhost:5000](http://localhost:5000)

## ☸️ Kubernetes Deployment

1. **Start Minikube**
   ```bash
   minikube start
   ```

2. **Apply Kubernetes manifests**
   ```bash
   kubectl apply -f k8s-deployment.yaml
   kubectl apply -f k8s-service.yaml
   ```

3. **Expose the app**
   ```bash
   minikube service onboarding-service
   ```

## 🔔 Notification System Setup

### Slack Webhook Integration

1. Create a **Slack webhook URL** from your workspace.
2. Go to your GitHub repository > **Settings > Secrets**, and add:
   - `SLACK_WEBHOOK_URL`

3. Add this step to your GitHub Actions workflow file:
   ```yaml
   - name: Send Slack Notification
     run: |
       curl -X POST -H 'Content-type: application/json' \
       --data '{"text":"✅ Deployment successful on GitHub Actions!"}' \
       ${{ secrets.SLACK_WEBHOOK_URL }}
   ```

### Email Notifications (Optional)

You can also set up SMTP-based email alerts using tools like Python's `smtplib` or GitHub Actions’ `mailer` plugins.

---

## 📎 Sample Slack Message

```text
✅ Deployment Success!
New version deployed to Kubernetes at http://localhost:30000
```

---

## 📝 Author

- **Name**: Rakshitha H L
- **Role**: DevOps Developer

---

## ✅ Project Status

✔️ CI/CD fully functional  
✔️ Docker image builds & deploys  
✔️ Notification system integrated  
✔️ Deployed successfully via Docker/Kubernetes

---

