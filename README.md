# E-Learning Platform

## 📌 Overview
This E-Learning Platform provides a structured online learning experience with mentorship, job opportunities, and a community forum. The platform allows users to register as mentors, mentees, or participants, enroll in courses, complete quizzes, track progress, and earn certificates.

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
## 🌍 Deployment Plan

### 🏗️ **Infrastructure Setup**
- **Frontend Deployment**: HTML, CSS, JavaScript served via **Azure Static Web Apps**
- **Backend Deployment**: Django running on **Azure App Service**
- **Database**: **Azure MySQL** for data storage
- **Cache**: **Redis** for caching sessions and user progress
- **File Storage**: **AWS S3** for storing course materials
- **Task Queue**: **Celery with Redis** for handling background tasks
- **CI/CD Pipeline**: **GitHub Actions** → Docker → **Azure Web App for Containers**
- **Monitoring & Logging**: **Prometheus + Grafana**, ELK Stack (**Elasticsearch, Logstash, Kibana**)
- **Security**: **SSL/TLS (Let's Encrypt), IAM Roles, Firewall Rules**

### 🚀 **Deployment Steps**
#### 1️⃣ **Backend Deployment (Django + MySQL)**
```sh
# SSH into the Azure VM
ssh azureuser@your-server-ip

# Clone latest updates from GitHub
cd /var/www/hustle-platform
git pull origin main

# Activate Virtual Environment
source myenv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Apply Migrations
python manage.py migrate

# Restart Gunicorn & Nginx
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

#### 2️⃣ **Frontend Deployment**
```sh
# Deploy to Azure Static Web Apps
az staticwebapp create -n hustle-platform -g resource-group --source . --location centralus
```

#### 3️⃣ **CI/CD Pipeline (GitHub Actions)**
- **Push to `main` branch → GitHub Actions triggers build → Docker image pushed to Azure → Auto-deployed**

#### 4️⃣ **Monitoring & Maintenance**
```sh
# Check Application Logs
journalctl -u gunicorn -f

# Monitor Performance (Prometheus)
curl http://localhost:9090/metrics
```

---
## 🤝 Contribution Guidelines
1. Fork the repository
2. Create a new branch (`feature-branch-name`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-branch-name`)
5. Create a pull request

---
## 📄 License
This project is licensed under the **MIT License**.

