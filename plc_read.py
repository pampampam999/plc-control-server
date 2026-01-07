from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# Set IP address dan port Modbus TCP
client = ModbusClient('192.168.1.150', port=502)

# Connect ke PLC
client.connect()

# Mengakses Q0.1 (Coil) (contoh alamat 0x0001 untuk Q0.1)
coil_status = client.read_coils(0x0001, 1)
print("Q0.1 Status:", coil_status.bits[0])

# Mengakses MW (Memori Word) (contoh alamat 0x0100 untuk MW)
mw_value = client.read_holding_registers(0x0100, 1)
print("MW Value:", mw_value.registers[0])

# Mengakses RTC (real-time clock, contoh alamat 0x0200 untuk RTC)
rtc_value = client.read_input_registers(0x0200, 3)
print("RTC Value:", rtc_value.registers)

# Disconnect setelah selesai
client.close()
