# Import ModbusTcpClient dari pymodbus untuk komunikasi dengan PLC menggunakan Modbus TCP
from pymodbus.client.sync import ModbusTcpClient
# Import konfigurasi IP dan port PLC dari config.py
from config import PLC_IPS, PLC_PORT

# Dictionary untuk menyimpan koneksi client per grup
clients = {}

# Fungsi untuk membuat koneksi Modbus TCP berdasarkan grup
def get_client(group):
    # Cek apakah client untuk grup ini sudah ada
    if group in clients:
        print(f"[modbus_service.py] [get_client()] Using existing connection for group: {group}")
        return clients[group]
    else:
        print(f"[modbus_service.py] [get_client()] Tidak ada dapat koneksi sebelumnya pada clients")
    
    # Mendapatkan IP sesuai dengan grup yang diberikan
    plc_ip = PLC_IPS.get(group)
    print(f"[modbus_service.py] [get_client()] modbus getclient plc_ip ",plc_ip)
    if plc_ip:
        client = ModbusTcpClient(plc_ip, port=PLC_PORT)
        print("[modbus_service.py] [get_client()] isi client sebelum connect ",client)
        client.connect()  # Koneksi ke PLC berdasarkan IP grup
        print("[modbus_service.py] [get_client()] client ",plc_ip," connected")
        print("[modbus_service.py] [get_client()] setelah connect isi client :",client,"isi Clients :",clients)
        clients[group]=client
        print("[modbus_service.py] [get_client()] setelelah client di masukkan ke clients ",clients)
        return client
    else:
        raise ValueError(f"[modbus_service.py] [get_client()] IP untuk grup {group} tidak ditemukan!")
    
# Fungsi untuk membaca status coil dari PLC
def read_coils(group, start, count):
    client = get_client(group)  # Mendapatkan client berdasarkan grup
    # Membaca 'count' jumlah coil dimulai dari alamat 'start' pada PLC
    rr = client.read_coils(start, count)
    # Jika terjadi error, mengembalikan list False sebanyak 'count' coil
    if rr.isError():
        return [False] * count
    # Mengembalikan nilai bit yang terbaca dari coil PLC
    return rr.bits[:count]

# Fungsi untuk menulis status coil ke PLC
def write_coil(group, address, value):
    client = get_client(group)  # Mendapatkan client berdasarkan grup
    client.write_coil(address, value)
