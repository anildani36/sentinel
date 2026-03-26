# 🔔 SENTINEL | Eco-system Notification Service

A notification service for [LEAF](https://github.com/anildani36/leaf.git) eco-system. This service sends notification via Email 
and Team notification in channel.

---

## ✨ Features

- **High-Entropy Generation**
  - Uses Python’s `secrets` module (cryptographically secure)
  - Avoids predictable pseudo-random generators

- **Real-Time UI Updates**
  - Password regenerates instantly as you adjust length or options

- **Modern Slider Experience**
  - Custom-styled range slider
  - Dynamic fill line for clear visual feedback

- **One-Click Copy**
  - Clipboard API integration
  - Smooth slide-up & fade notification animation

- **Responsive MVC Design**
  - Mobile-friendly layout
  - Clean separation of Models, Views, and Controllers
  - Built with Bootstrap 4.4

---

## 🛠 Tech Stack

**Backend**
- Python 3.13
- FastAPI

---

## 📂 Project Structure

```

sentinel/
├── main.py              
├── docs/                
│   └── adrs/
│       └── adr_v1.md
├── src/                 
│   ├── config/
│   │   ├── app_config.py
│   │   └── secrets_manger_services.py
│   ├── constants/
│   │   └── aws_secrets_service_key_names.py
│   ├── controllers/
│   │   └── notification_controller.py
│   ├── enums/
│   │   ├── env_enum.py
│   │   └── notification_type_enum.py
│   ├── exceptions/
│   │   └── exception_handler.py
│   ├── injection/
│   │   └── container.py
│   ├── model/
│   │   ├── notification_model.py
│   │   ├── notification_request_model.py
│   ├── routes/
│   │   ├── actuator_routes.py
│   │   └── notification_routes.py
│   ├── service/
│   │   ├── sentinel_service.py
│   │   └── notification
│   │       ├── base_notification_service.py
│   │       ├── email_notification_service.py
│   │       └── teams_notification_service.py
│   └── templates/
│       ├── email
│       │   ├── job_success.py
│       │   └── job_failure.py
│       └── teams
│           ├── job_success.py
│           └── job_failure.py
└── README.md 

````

---

## 🚀 Getting Started

### Prerequisites
- Python **3.13+**
- **uv** (Fast Python package manager)

---

### Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/anildani36/sentinel.git
cd sentinel
````

2️⃣ **Install dependencies**

```bash
uv sync
```

3️⃣ **Run the application**

```bash
uv run main.py
```

4️⃣ **Open in browser**

```
http://127.0.0.1:5000
```
or
```
http://localhost:5000
```

---

## Architecture

To be added

---

## 💡 How It Works

1. **Select Length**

   * Use the slider to choose password length (8–25 characters)

2. **Customize Characters**

   * Toggle:

     * Uppercase
     * Lowercase
     * Numbers
     * Symbols

3. **Instant Feedback**

   * Password updates immediately via Fetch API calls

4. **Security First**

   * Passwords generated using `secrets.choice()`
   * Resistant to brute-force predictability

---

## 🔒 Security Notes

* No passwords are stored or logged
* All generation occurs server-side using secure entropy
* No external APIs involved

---

## 👨‍💻 Author

**[Anil Dani](htttps://www.linkedin.com/in/anildani)**

---

## 📜 License

This project is licensed under the **[GNU GPL V3 License](LICENSE)** — feel free to use, modify, and distribute.

---

⭐ If you find this project useful, consider starring the repository!