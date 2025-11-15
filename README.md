
project/
│── project/  
│── projectapp/
│── templates/
│── manage.py
│── db.sqlite3
│── static/
```

Here is the **clean, correct, and professional README** based on that structure.
(You can copy-paste directly into README.md)

---

# **Django Contact Form Project**

This project is a basic Django application that includes a contact form where users can submit their details including **first name, last name, email, subject, and message**. The form data is saved into the database through Django models.

---

## Project Folder Structure 

```
project/
│── project/          # Django settings & URLs
│── projectapp/       # App containing models, forms, and views
│── templates/        # HTML templates for frontend
│── static/           # CSS, JS, Images (if added)
│── db.sqlite3        # Default database
│── manage.py         # Django management file
```

---

📝 Features

* Contact form with 5 input fields
* Data stored in SQLite/MySQL
* Clean Django template structure
* Simple and lightweight
* Easy to extend and customize

---

## Model Used

```
class Users(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname  = models.CharField(max_length=50)
    Email     = models.CharField(max_length=50)
    Subject   = models.CharField(max_length=50)
    Message   = models.TextField(max_length=500)
```

---

## **▶️ How to Run the Project**

Run the following commands:

```
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then open the browser at:

```
http://127.0.0.1:8000/
```

---

## **🗂️ Git Commands Used (Your VS Code Terminal Steps)**

These were the exact steps you followed:

```
git init
git add .
git commit -m "Initial project upload"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

---

## ** Successfully Uploaded to GitHub**



* Branch = **main**
* Files = **Successfully pushed**
* .gitignore applied
* No virtual environment files uploaded


