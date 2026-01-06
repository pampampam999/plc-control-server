# Import ModbusTcpClient dari pymodbus untuk komunikasi dengan PLC menggunakan Modbus TCP
from pymodbus.client.sync import ModbusTcpClient
# Import konfigurasi IP dan port PLC dari config.py
from config import PLC_IP, PLC_PORT

# Membuat koneksi Modbus ke PLC
client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
client.connect()  # Melakukan koneksi ke PLC

# Fungsi untuk membaca status coil dari PLC
def read_coils(start, count):
    # Membaca 'count' jumlah coil dimulai dari alamat 'start' pada PLC
    rr = client.read_coils(start, count)
    # Jika terjadi error, mengembalikan list False sebanyak 'count' coil
    if rr.isError():
        return [False] * count
    # Mengembalikan nilai bit yang terbaca dari coil PLC
    return rr.bits[:count]

# Fungsi untuk menulis status coil ke PLC
def write_coil(address, value):
    # Menulis nilai 'value' ke coil yang ditunjuk oleh 'address' di PLC
    client.write_coil(address, value)
