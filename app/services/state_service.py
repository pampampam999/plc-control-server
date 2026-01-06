# Import konfigurasi mapping dari config.py
from config import COIL_MAPPING
# Import fungsi-fungsi Modbus untuk berinteraksi dengan PLC
from services.modbus_service import read_coils, write_coil

# Fungsi untuk mendapatkan state terkini dari PLC
def get_state():
    # Membaca coils (output) dari PLC, sesuai jumlah coils yang ada di COIL_MAPPING
    bits = read_coils(0, len(COIL_MAPPING))
    # Mengembalikan dictionary dengan nama lampu sebagai key dan status coil sebagai value
    return {lamp: bits[addr] for lamp, addr in COIL_MAPPING.items()}

# Fungsi untuk mengubah state lampu di PLC
def set_state(lamp, value):
    # Menulis state baru ke PLC sesuai dengan lampu yang dipilih (lamp) dan nilai state (value)
    write_coil(COIL_MAPPING[lamp], value)
