# Playwright Python Test Automation Project

This project contains **UI and API automated tests** written in **Python** using **Playwright** and **Pytest**.

The tests cover:

* UI testing of the **Swag Labs** login functionality
* API testing using **Reqres API** (GET and POST requests)
* Schema validation and response time checks

---

## 🛠️ Tech Stack

* Python 3.9+
* Playwright (sync API)
* Pytest
* Requests
* JSON Schema validation

---

## 📂 Project Structure

```
project-root/
├── tests/
│   ├── api/
│   │   ├── test_create_user.py
│   │   ├── test_get_users.py
│   │   └── test-data/
│   │       └── users.json
│   └── ui/
│       └── test_login.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install Playwright browsers (required)

```bash
playwright install
```

---

## ▶️ Running Tests

### Run all tests

```bash
pytest
```

### Run only UI tests

```bash
pytest tests/ui
```

### Run only API tests

```bash
pytest tests/api
```

### Run tests with detailed output

```bash
pytest -v
```

---

## 🧪 Test Descriptions

### UI Tests – Swag Labs

* Successful login with valid credentials
* Error handling for invalid login
* Validation for empty username or password
* Locked-out user login prevention
* Password field masking
* Logout functionality

Target URL:

```
https://www.saucedemo.com/
```

---

### API Tests – Reqres

#### POST /api/users

* Status code validation (201)
* Response time check
* JSON schema validation
* Parameterized tests using external JSON data

#### GET /api/users

* Status code validation
* Pagination validation
* Response structure and data type checks

Target API:

```
https://reqres.in/
```

> ⚠️ Note: If the Reqres API is blocked by Cloudflare, the test will be skipped automatically.

---

## 🧹 Notes

* Virtual environment (`venv/`) is **not included** in the repository
* Cache folders (`__pycache__`, `.pytest_cache`) are ignored
* `.vscode/` settings are local and not tracked

---

## ✅ Author

Test automation implemented by Michal Balik using **Playwright with Python**.

---


