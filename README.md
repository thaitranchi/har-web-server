# Heritage at Risk (HAR) Web Server

The Heritage at Risk (HAR) web server is a full-stack Django application designed to document and track cultural heritage sites facing various threats. This project demonstrates a robust implementation of user authentication, automatic account provisioning, and secure data ownership.

## 🚀 Key Features

* **Unified Connection Flow:** A seamless "Connection" procedure that merges login and signup into a single interaction. New users are automatically registered upon their first successful form submission.
* **Data Sovereignty:** A strict security model where users can only view, edit, or delete reports they have personally created.
* **Coordinate Precision:** Specialized validation for Latitude, Longitude, and Altitude using frontend regex patterns and backend numeric verification.
* **Chronological Journaling:** Automated timestamping and ordering of heritage reports for better historical tracking and list management.

---

## 🛠️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/thaitranchi/har-web-server
    cd har-web-server
    ```

2.  **Environment Setup:**
    Ensure Django is installed in your environment:
    ```bash
    pip install django
    ```

3.  **Database Configuration:**
    Initialize the SQLite database and apply the `Report` model migrations:
    ```bash
    python manage.py makemigrations report
    python manage.py migrate
    ```

4.  **Run Application:**
    ```bash
    python manage.py runserver
    ```
    Access the application at `http://127.0.0.1:8000/`.

---

## 📁 Architecture Overview

* `har/report/models.py`: Defines the `Report` schema with a `ForeignKey` relationship to the Django `User` model.
* `har/report/views.py`: Contains the core logic for the unified connection flow and authenticated CRUD operations.
* `har/report/forms.py`: Django `ModelForm` and `Form` definitions with custom widgets, placeholders, and regex patterns.
* `har/report/static/css/`: Modular UI styling including `connection.css`, `reports.css`, and `report_update.css`.
* `har/report/templates/`: Django templates using block inheritance, static tag loading, and conditional logic.

---

## 🧪 Quality Assurance

To ensure the project meets the technical requirements of Waypoint 9, run the automated test suite:

```bash
python manage.py test report
```

**Testing coverage includes:**
* Automatic user creation upon first connection.
* Protection of private reports from unauthorized users (Ownership Isolation).
* Anonymous user redirection for protected views via login decorators.
* Frontend and backend form validation for coordinate data.

---

## 📝 Technical Stack

* **Backend:** Python 3.x, Django 5.x
* **Frontend:** HTML5, CSS3 (Flexbox), JavaScript (Vanilla ES6)
* **Database:** SQLite

---

### Author
Tran Chi Thai
