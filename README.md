# ptero-memcheck

**ptero-memcheck** is a simple Python script that monitors the **RAM usage** of a specific Pterodactyl server and automatically triggers a defined **scheduler** when a predefined memory limit is exceeded.

## 📌 Features

- Fetch current RAM usage via the **Pterodactyl API**
- Compare usage against a predefined memory limit
- Automatically execute a configured **scheduler** (e.g., to restart the server)
- Easy configuration via variables in the script


## 🚀 Requirements

- Python **3.x**
- **requests** module (`pip install requests`)
- A valid **API key** from your Pterodactyl panel (with access to the target server)
- Server ID and scheduler ID from your Pterodactyl panel


## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/crackscout123/ptero-memcheck.git
cd ptero-memcheck
```

2. **Install dependencies**

```bash
pip install requests
```

3. **Configure the script** (`ptero-memcheck.py`):

```python
PANEL_URL = "https://your-panel.com"      # Your panel URL
API_KEY = "YOUR_API_KEY"                  # Your API key
SERVER_ID = "your-server-id"              # Server ID
SCHEDULE_ID = "your-scheduler-id"         # Scheduler ID
RAM_LIMIT_MB = 20480-(1024*1)             # Memory limit in MB
```


## ▶️ Usage

Run the script with:

```bash
python main.py
```

The script will:

- Check RAM usage every **5 minutes**
- Print the current usage to the terminal
- Trigger the scheduler once the set limit is reached or exceeded


## 🛠 Customization

- **Check interval**: Change the `time.sleep(60*5)` value in seconds (`60*5 = 5 minutes`) as needed
- **RAM limit**: Adjust the `RAM_LIMIT_MB` value in the script


## 📄 License

This project is licensed under the **MIT License**.
