# Import fungsi dari services/state_service untuk mendapatkan dan mengubah state lampu
from services.state_service import get_state, set_state

# Fungsi untuk inisialisasi dan menangani event WebSocket
def init_socket(socketio):

    # Event ketika client terhubung ke server (WebSocket connection)
    @socketio.on("connect")
    def handle_connect():
        # Mengirim state terkini dari PLC ke client yang terhubung
        socketio.emit("state_update", get_state())

    # Event ketika client mengirimkan data untuk mengubah state (misalnya klik checkbox)
    @socketio.on("toggle")
    def handle_toggle(data):
        # Mengambil data yang dikirimkan client (lampu yang dikontrol dan state baru)
        lamp = data["lamp"]
        state = data["state"]

        # Mengubah state lampu di PLC berdasarkan input dari client
        set_state(lamp, state)

        # Mengirimkan kembali state terkini kepada semua client yang terhubung
        socketio.emit("state_update", get_state())
