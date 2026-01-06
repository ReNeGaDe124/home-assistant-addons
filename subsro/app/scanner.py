import time
from subtitles import validate_and_fix

def scan_movies():
    print("[subsro] Scanning movies")

def scan_tv():
    print("[subsro] Scanning TV")

def start_scheduler():
    while True:
        scan_movies()
        scan_tv()
        time.sleep(3600)
