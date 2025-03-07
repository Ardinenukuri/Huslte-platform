# **Hustle Platform**

## 📌 **Overview**
Hustle Platform is an **online learning and mentorship platform** that provides users with **structured courses, mentorship programs, job opportunities, and a community forum**. The platform enables users to **enroll in courses, complete quizzes, track progress, earn certificates**, and **connect with mentors** for guidance.

## 🚀 **Key Features**
- ✅ **User Authentication** (Mentors, Mentees, Participants, Admins)
- ✅ **Course Management** (Upload courses, chapters, quizzes)
- ✅ **Mentorship System** (Mentor-mentee pairing, messaging)
- ✅ **Progress Tracking** (Chapters, quizzes, final course completion)
- ✅ **Job Opportunities** (Apply for internships, job postings)
- ✅ **Community Forum** (Discussions, Q&A, support groups)
- ✅ **AI Quiz Generation** (Uses **Gemini AI** to generate quizzes)
- ✅ **Email Notifications** (Users receive **automated emails** for updates)
- ✅ **Multi-language Support** (Translations using **Google Translate API**)
- ✅ **Deployed on Render** (Auto-deployments from GitHub)
- ✅ **SQLite3 Database** (For easy local storage & lightweight deployment)

---

## 🛠️ **Setup Instructions**

### 1⃣ **Clone the Repository**
```sh
git clone https://github.com/Ardinenukuri/Huslte-platform.git
cd Huslte-platform
```

### 2⃣ **Set Up Virtual Environment**
```sh
python -m venv myenv
source myenv/bin/activate  # For Linux/macOS
myenv\Scripts\activate    # For Windows
```

### 3⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4⃣ **Configure Environment Variables**
Create a `.env` file in the root directory:
```
SECRET_KEY='your-secret-key'
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # ✅ Using SQLite3 for lightweight storage
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='your-email@gmail.com'
EMAIL_HOST_PASSWORD='your-email-password'
```

### 5⃣ **Apply Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### 6⃣ **Create Superuser (For Admin Access)**
```sh
python manage.py createsuperuser
```

### 7⃣ **Run the Server**
```sh
python manage.py runserver
```
🥽 **Access the platform at:** **http://127.0.0.1:8000/**

---

# 🚀 **Deployment Plan**

## **🏰 Infrastructure Setup**

### ✅ **Deployed on Render**
- **Frontend:** Static site hosting on Render
- **Backend:** Django application deployed as a Web Service on Render
- **Database:** SQLite3 (Lightweight & auto-managed)
- **CI/CD:** Auto-deployments from **GitHub to Render**
- **Security:** **SSL/TLS certificates** via Let's Encrypt (Auto-provisioned by Render)

---

## 🚀 **Deployment Steps**

### 1⃣ **Deploy Django Backend on Render**
1. **Log in to Render** and **create a new Web Service**.
2. **Connect GitHub repository** to Render.
3. **Set the build command:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set the start command:**
   ```sh
   gunicorn Hustle.wsgi:application
   ```
5. **Configure environment variables** in the Render dashboard (e.g., `DATABASE_URL`, `EMAIL_HOST`, `SECRET_KEY`).
6. **Run migrations after deployment:**
   ```sh
   python manage.py migrate
   ```

---

### 2⃣ **Deploy Frontend on Render**
1. **Create a new Static Site** on Render.
2. **Connect to GitHub repository** (if separate frontend repo exists).
3. **Set the build command** (if applicable).
4. **Deploy the static files**.

---

### 3⃣ **Automated CI/CD Pipeline**
- **On every push to the `main` branch**, Render **automatically triggers a build and deployment**.
- **Optional:** Use **GitHub Actions** for **pre-deployment testing**.

---

## 📩 **Email Notifications**
✅ Users receive **automated email notifications** for:
- **Course Completion** → Email with **certificate download link**.
- **Mentorship Requests** → Mentor receives **email notifications**.
- **New Comments, Threads & Votes** → Users get notified **via email** and **dashboard**.
- **etc...**

---

## 🌍 **Multi-Language Support**
✅ **Translations integrated using Google Translate API**  
- Users can **switch languages dynamically**.
- Supports **English, French, Spanish, Swahili**.

---

## 🤖 **AI-Powered Quiz Generation (Gemini)**
✅ **Automated quiz generation** using **Gemini AI API**  
- Instructors can **auto-generate quiz questions** from course materials.
- Supports **multiple-choice, short answers, and document-based questions**.

---

## 🚀 **GitHub Repository**
👉 **[Hustle Platform GitHub Repo](https://github.com/Ardinenukuri/Huslte-platform)**

---

## 📜 **Project Schema**
👉 **[Database Schema](https://drive.google.com/file/d/1k_WE9_2RY-QUunSFpTm-XDA9FpMIgj_M/view?usp=sharing)**

---

## 🎨 **Figma UI Design**
👉 **[Figma Link](https://www.figma.com/design/yWNk3qBfrRcBgWTraBCbpo/Hustle-Platform?node-id=11-161&t=lLQtFwR3sOn4T14o-1)**

---

##  **🌍Live Deployment**
👉 **[Hustle-platform](https://huslte-platform.onrender.com)**

---



## 🎥 **Demo Video**
👉 **[Initial Software](https://youtu.be/cijsDEU4_FE)**

👉 **[Final Software](https://youtu.be/cI6usJ8-iHA)**

---

## 🤝 **Contribution Guidelines**
1. **Fork the repository**.
2. **Create a new branch** (`feature-branch-name`).
3. **Commit your changes** (`git commit -m "Added new feature"`).
4. **Push to GitHub** (`git push origin feature-branch-name`).
5. **Create a pull request**.

---

🎉 **Enjoy Learning with Hustle Platform! 🚀🔥**
