import requests
import time
from datetime import datetime

PANEL_URL = "https://dein-panel.com"          # Panel-URL anpassen!
API_KEY = "DEIN_API_KEY"                      # API Key eintragen!
SERVER_ID = "dein-server-id"                  # Server-ID eintragen
SCHEDULE_ID = "dein-scheduler-id"             # Scheduler-ID eintragen
RAM_LIMIT_MB = 20480-(1024*1)                 # Das RAM-Limit in MB

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

def get_server_resources():
    url = f"{PANEL_URL}/api/client/servers/{SERVER_ID}/resources"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()
    # RAM usage is usually reported in bytes, so convert to MB
    current_ram_mb = data["attributes"]["resources"]["memory_bytes"] // 1024 // 1024
    return current_ram_mb

def execute_scheduler():
    url = f"{PANEL_URL}/api/client/servers/{SERVER_ID}/schedules/{SCHEDULE_ID}/execute"
    resp = requests.post(url, headers=HEADERS)
    if resp.status_code in (202, 204):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Scheduler wurde erfolgreich ausgelöst.")
    else:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fehler beim Ausführen des Schedulers: Status {resp.status_code}, Antwort: {resp.text}")

def main():
    print("done.") # pterodactyls generic python env checks for this when running a script in the panel.
    while True:
        try:
            ram_usage = get_server_resources()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] RAM Nutzung: {ram_usage}MB von {RAM_LIMIT_MB}MB")
            if ram_usage >= RAM_LIMIT_MB:
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] RAM Limit erreicht! Scheduler wird ausgeführt...")
                execute_scheduler()
                break  # Bei Bedarf hier weiter laufen lassen oder abbrechen
        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fehler:", e)
        # Intervall für die Prüfung, z.B. alle 5 Minuten
        time.sleep(60*15)

if __name__ == "__main__":
    main()
