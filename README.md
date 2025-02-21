# Hustle Platform

## 📌 Overview
This Hustle Platform provides a structured online learning experience with mentorship, job opportunities, and a community forum. The platform allows users to register as mentors, mentees, or participants, enroll in courses, complete quizzes, track progress, and earn certificates.

## 🚀 Features
- **User Authentication** (Mentors, Mentees, Participants, Admins)
- **Course Management** (Upload courses, chapters, quizzes)
- **Mentorship System** (Mentor-mentee pairing, messaging)
- **Progress Tracking** (Chapters, quizzes, final course completion)
- **Job Opportunities** (Apply for internships, job postings)
- **Community Forum** (Discussions, Q&A, support groups)
- **Auto-deployment** using **GitHub Actions, Docker, and Azure**

---
## 🛠️ Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Ardinenukuri/e-learning-platform.git
cd e-learning-platform
```

### 2️⃣ Set Up Virtual Environment
```sh
python -m venv myenv
source myenv/bin/activate  # For Linux/macOS
myenv\Scripts\activate    # For Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory:
```
SECRET_KEY='your-secret-key'
DEBUG=True
DATABASE_URL=mysql://username:password@localhost/db_name
AWS_ACCESS_KEY_ID='your-aws-key'
AWS_SECRET_ACCESS_KEY='your-aws-secret'
REDIS_URL=redis://localhost:6379
```

### 5️⃣ Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser (For Admin Access)
```sh
python manage.py createsuperuser
```

### 7️⃣ Run the Server
```sh
python manage.py runserver
```
Access the platform at: **http://127.0.0.1:8000/**

---
# Deployment Plan

## 🏗️ Infrastructure Setup

- **Frontend Deployment:**  
  - HTML, CSS, and JavaScript hosted via Render's Static Sites.

- **Backend Deployment:**  
  - Django application deployed as a Web Service on Render.

- **Database:**  
  - MySQL



- **CI/CD Pipeline:**  
  - GitHub repository integrated with Render for automatic builds and deployments (optionally, using GitHub Actions for pre-deployment testing).


- **Security:**  
  - Render auto-provisions SSL/TLS certificates (via Let's Encrypt). Manage environment-specific security settings like IAM roles and firewall rules as needed.

---

## 🚀 Deployment Steps

### 1️⃣ Backend Deployment (Django + MySQL)

1. **Configure Render Web Service:**
   - Log in to your Render dashboard.
   - Create a new **Web Service** and connect your GitHub repository.
   - Set your build command:
     ```bash
     pip install -r requirements.txt
     ```
   - Set your start command:
     ```bash
     gunicorn yourproject.wsgi:application
     ```
   - Configure necessary environment variables (e.g., `DATABASE_URL`, `REDIS_URL`, `SECRET_KEY`, etc.).

2. **Run Migrations:**
   - After deployment, use Render’s one-off command feature to apply migrations:
     ```bash
     python manage.py migrate
     ```

---

### 2️⃣ Frontend Deployment

1. **Configure Render Static Site:**
   - Log in to your Render dashboard.
   - Create a new **Static Site**.
   - Connect your GitHub repository containing your static site (HTML, CSS, JavaScript).
   - Specify a build command if needed (or leave blank if you’re directly deploying static files).
   - Set the publish directory (e.g., `build/` if using a build step or the directory containing your static files).

---

### 3️⃣ CI/CD Pipeline

- **Automated Deployments:**
  - On every push to the main branch, Render automatically triggers a build and deployment for both your backend and frontend.
  - Optionally, integrate GitHub Actions to run tests or build Docker images before code reaches Render.

---

### 4️⃣ Monitoring & Maintenance

- **Check Application Logs:**
  - Access logs directly in the Render dashboard for real-time insights.

- **Monitor Performance:**
  - Utilize Render's integrated metrics.
  - For deeper monitoring, set up external tools like Prometheus and Grafana, or the ELK Stack.

- **Scaling & Updates:**
  - Adjust service settings, environment variables, and scaling options directly from the Render dashboard as your project grows.
---

## 🚀 Github Link
- **Link**: https://github.com/Ardinenukuri/Huslte-platform 

---


## 🚀 Schemas
- **Link**: https://drive.google.com/file/d/1k_WE9_2RY-QUunSFpTm-XDA9FpMIgj_M/view?usp=sharing

---

## 🚀 Figma Link
- **Link**: https://www.figma.com/design/yWNk3qBfrRcBgWTraBCbpo/Hustle-Platform?node-id=11-161&t=lLQtFwR3sOn4T14o-1

---


## 🚀 Video Link
- **Link**: https://youtu.be/cijsDEU4_FE

---

## 🤝 Contribution Guidelines
1. Fork the repository
2. Create a new branch (`feature-branch-name`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-branch-name`)
5. Create a pull request

---

