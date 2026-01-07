# Import konfigurasi mapping dari config.py
from config import COIL_MAPPING, GROUPS
# Import fungsi-fungsi Modbus untuk berinteraksi dengan PLC
from services.modbus_service import read_coils, write_coil

# Fungsi untuk mendapatkan state terkini berdasarkan grup
def get_state():
    state = {}
    # Membaca status coil berdasarkan grup dan lampu
    for group, lamps in GROUPS.items():
        print("[state_service.py][get_state()] ini group ",group," dan punya lampu ",lamps)
        bits = read_coils(group, 0, len(lamps))  # Membaca status coil dari PLC sesuai grup
        print("[state_service.py][get_state()] bits ",bits)
        state[group] = {lamp: bits[COIL_MAPPING[lamp]] for lamp in lamps}
    return state

# Fungsi untuk mengubah state lampu berdasarkan grup
def set_state(lamp, value):
    # Menentukan grup berdasarkan lampu (ID lampu)
    group = next((group for group, lamps in GROUPS.items() if lamp in lamps), None)
    if group:
        # Menulis status baru ke coil (lampu) yang dipilih berdasarkan grup dan IP
        write_coil(group, COIL_MAPPING[lamp], value)