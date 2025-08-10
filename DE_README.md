# ptero-memcheck

**ptero-memcheck** ist ein einfaches Python-Skript, das den **RAM-Verbrauch** eines bestimmten Pterodactyl-Servers überwacht und automatisch einen definierten **Scheduler** ausführt, sobald ein voreingestelltes Speicherlimit überschritten wird.

## 📌 Features

- Abfrage des aktuellen RAM-Verbrauchs über die **Pterodactyl API**
- Vergleich mit einem festgelegten Speicherlimit
- Automatische Ausführung eines konfigurierten **Schedulers** (z. B. zum Neustarten des Servers)
- Einfache Konfiguration über Variablen im Code


## 🚀 Voraussetzungen

- Python **3.x**
- Modul **requests** (`pip install requests`)
- Ein gültiger **API-Key** von deinem Pterodactyl-Panel (mit Zugriff auf den gewünschten Server)
- Server- und Scheduler-ID aus deinem Pterodactyl-Panel


## ⚙️ Installation

1. **Repository klonen**

```bash
git clone https://github.com/crackscout123/ptero-memcheck.git
cd ptero-memcheck
```

2. **Abhängigkeiten installieren**

```bash
pip install requests
```

3. **Konfiguration im Skript anpassen** (`ptero-memcheck.py`):

```python
PANEL_URL = "https://dein-panel.com"       # Deine Panel-URL
API_KEY = "DEIN_API_KEY"                   # Dein API Key
SERVER_ID = "dein-server-id"               # Server-ID
SCHEDULE_ID = "dein-scheduler-id"          # Scheduler-ID
RAM_LIMIT_MB = 20480-(1024*1)              # Speicherlimit in MB
```


## ▶️ Nutzung

Starte das Skript einfach mit:

```bash
python main.py
```

Das Skript:

- prüft alle **5 Minuten** den RAM-Verbrauch,
- gibt den aktuellen Verbrauch im Terminal aus,
- löst den Scheduler aus, sobald das gesetzte Limit erreicht oder überschritten ist.


## 🛠 Anpassungen

- **Prüfintervall**: Ändere den `time.sleep(300)`-Wert in Sekunden (`300 = 5 Minuten`) nach Bedarf.
- **RAM Limit**: Über den Wert `RAM_LIMIT_MB` im Skript einstellbar.


## 📄 Lizenz

Dieses Projekt steht unter der **MIT License**.

