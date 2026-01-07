# Import Flask dan SocketIO dari Flask
from flask import Flask, render_template
from flask_socketio import SocketIO

# Import fungsi dari controllers/socket_controller untuk inisialisasi WebSocket
from controllers.socket_controller import init_socket

# Membuat instance Flask
#print(__name__)
app = Flask(__name__)

# Membuat instance SocketIO untuk mendukung komunikasi real-time
socketio = SocketIO(app, cors_allowed_origins="*")

# Route utama untuk halaman index (front-end)
@app.route("/")
def index():
    # Render file index.html
    return render_template("index.html")

# Inisialisasi WebSocket dengan menghubungkan fungsi socket_controller
init_socket(socketio)

# Menjalankan aplikasi Flask di host 0.0.0.0 dan port 5000
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
