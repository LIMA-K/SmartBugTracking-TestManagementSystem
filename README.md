# 🐞 Smart Bug Tracking & Test Management System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![Database](https://img.shields.io/badge/Database-SQLite-blue.svg)
![Frontend](https://img.shields.io/badge/Frontend-Bootstrap-7952b3.svg)

A web-based platform to manage bugs, test cases, and team collaboration with role-based dashboards for Admins, Testers, and Developers.

---

## 📖 Table of Contents
- Project Overview  
- Objectives  
- Existing vs Proposed System  
- User Roles  
- Modules  
- Technology Stack  
- Database Design  
- System Architecture  
- Features  
- Future Enhancements  
- Installation & Setup  
- Usage  
- Screenshots  
- Contributors  
- License  

---

## 📌 Project Overview
The **Smart Bug Tracking & Test Management System** is a Django-based web application that streamlines the software testing and bug resolution process. It provides a centralized platform where testers can create and execute test cases, report bugs, and developers can manage assigned defects – all with full traceability. Admins have oversight of users, projects, and overall system health.

The system supports manual testing workflows and is designed for easy extension to automation testing.

---

## 🎯 Objectives
- Centralize bug tracking and test management  
- Provide role-based access control  
- Enable test case creation and execution  
- Allow developers to manage and resolve bugs  
- Improve team communication  
- Support future automation integration  

---

## 📊 Existing vs Proposed System

| Feature | Existing System | Proposed System |
|--------|----------------|----------------|
| Centralized platform | ❌ Spreadsheets/emails | ✅ Web-based dashboard |
| Test case management | ❌ None | ✅ Full CRUD & execution |
| Role-based access | ❌ None | ✅ Admin/Tester/Developer |
| Real-time bug status | ❌ No | ✅ Live updates |
| Traceability | ❌ No | ✅ Full tracking |
| Communication | ❌ Scattered | ✅ Integrated |
| Reporting | ❌ Manual | ✅ Analytics |

---

## 👥 User Roles

### 🔧 Admin
- Manage users and roles  
- Monitor projects and bugs  
- Assign testers and developers  

### 🧪 Tester
- Create and execute test cases  
- Report bugs with severity & priority  
- Track bug status  

### 💻 Developer
- View assigned bugs  
- Update bug status  
- Upload fixes and add comments  

---

## 🧩 Modules

### 🔐 Authentication Module
- Login & registration  
- Role-based access  

### 🧪 Test Management Module
- Create test cases  
- Execute and track results  

### 🐛 Bug Tracking Module
- Report bugs  
- Assign and track lifecycle  

### 📊 Dashboard Module
- Role-based dashboards  
- Statistics and reports  

### 🗨️ Communication Module
- Bug comments  
- Team chat system  

---

## 🛠️ Technology Stack
- **Backend:** Django 4.2 (Python 3.10+)  
- **Frontend:** Bootstrap 5, HTML, CSS  
- **Database:** SQLite  
- **Charts:** Chart.js  
- **Version Control:** Git & GitHub  

---

## 🗄️ Database Design

| Model | Description |
|------|------------|
| User | Django built-in |
| Profile | Role management |
| Project | Project details |
| Scenario | Testing scenarios |
| TestCase | Test cases |
| Bug | Bug details |
| BugComment | Bug discussions |
| Report | Bug reports |
| TeamChatMessage | Team chat |

---

## 🏗️ System Architecture
Three-tier architecture:

- **Presentation Layer:** HTML + Bootstrap  
- **Business Logic:** Django Views & Forms  
- **Data Layer:** SQLite via Django ORM  

---

## ✨ Features
- User authentication & role-based dashboards  
- Test case management  
- Bug lifecycle tracking  
- Developer fix upload  
- Inline comments & chat  
- Analytics & charts  
- Responsive UI  

---

## 🔮 Future Enhancements
- Automation testing (Selenium/PyTest)  
- Email notifications  
- REST API  
- Advanced analytics  
- Real-time updates  

---

## 💻 Installation & Setup

### Prerequisites
- Python 3.10+
- Git

### Steps
  
```bash
git clone https://github.com/LIMA-K/SmartBugTracking-TestManagementSystem.git
cd SmartBugTracking-TestManagementSystem
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
http://127.0.0.1:8000/

## 🚀 Usage

### 👨‍💼 Admin
- Log in using superuser credentials  
- Access the admin panel or dashboard  
- Manage users, assign roles, and create projects  
- Assign testers and developers  
- Monitor system-wide bug and test statistics  

### 🧪 Tester
- Log in as a tester  
- Access the tester dashboard  
- Create scenarios and test cases  
- Execute test cases (Pass / Fail / Blocked)  
- Report bugs with severity and priority  
- Track bug status and participate in discussions  

### 💻 Developer
- Log in as a developer  
- View assigned bugs  
- Update bug status (Open → In Progress → Resolved → Closed)  
- Upload fix files  
- Add comments and collaborate with testers  

---

## 📸 Screenshots

### Admin Dashboard
![Admin Dashboard](static/images/admin_dashboard.png)

### Tester Dashboard
![Tester Dashboard](static/images/tester_dashboard.png)

### Developer Dashboard
![Developer Dashboard](static/images/developer_dashboard.png)

### Team Chat
![Team Chat](static/images/team_chat.png)

---

## 👩‍💻 Contributors

**LIMA**  
MCA Student  
Project Lead – Backend & Frontend Development  

Special thanks to faculty mentors and peers for their guidance.

---

## 📄 License
This project is for academic and learning purposes only.  
It is not licensed for commercial use.  
All code is original and developed as part of the MCA final year project.



