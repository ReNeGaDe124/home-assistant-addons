from threading import Thread
from web import app
from scanner import start_scheduler

print("[subsro] Starting add-on")

Thread(target=start_scheduler, daemon=True).start()
app.run(host="0.0.0.0", port=8999)
