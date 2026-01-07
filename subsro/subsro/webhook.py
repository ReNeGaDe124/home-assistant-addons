from flask import Flask, request
import threading
def start_webhook(handler):
    app = Flask(__name__)
    @app.route("/plex", methods=["POST"])
    def hook():
        if request.json and request.json.get("event")=="library.new":
            threading.Thread(target=handler).start()
        return "OK"
    app.run(host="0.0.0.0", port=8999)
