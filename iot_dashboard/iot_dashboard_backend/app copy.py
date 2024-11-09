import time
from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="threading",
    logger=True,
    engineio_logger=True,
)


# Store the current state or command for each LED and servo
device_commands = {
    "LED1": {"action": "off", "color": (0, 0, 0)},
    "LED2": {"action": "off", "color": (0, 0, 0)},
    "servo1": {"action": "stop", "start_angle": 0, "end_angle": 180},
    "servo2": {"action": "stop", "start_angle": 0, "end_angle": 180},
}

# Store connection status of ESP32
esp_connected = False


# Endpoint to update LED or servo command
@app.route("/api/control", methods=["POST"])
def control_device():
    global esp_connected
    data = request.json
    device = data.get("device")
    command = data.get("command")
    if device and command:
        device_commands[device] = command
        socketio.emit("device_update", {device: command})
        return (
            jsonify({"status": "success", "message": f"{device} command updated"}),
            200,
        )
    return jsonify({"status": "error", "message": "Invalid device or command"}), 400


# Endpoint for ESP32 to fetch the latest commands
@app.route("/api/get_commands", methods=["GET"])
def get_commands():
    global esp_connected
    esp_connected = True  # Update the connection status when ESP32 fetches commands
    return jsonify(device_commands)


# Periodic event to check ESP32 connection
@socketio.on("connect")
def on_connect():
    socketio.emit("connection_status", {"esp_connected": esp_connected})


def reset_esp_connection_status():
    global esp_connected
    while True:
        esp_connected = False
        socketio.emit("connection_status", {"esp_connected": esp_connected})
        time.sleep(10)  # Check ESP32 connection every 10 seconds


if __name__ == "__main__":
    socketio.start_background_task(reset_esp_connection_status)
    socketio.run(app, host="0.0.0.0", port=5000)
