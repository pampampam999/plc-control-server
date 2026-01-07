# ===============================================
# File stand alone
# Untuk mencoba setiap ip secara direct apa bisa
# ===============================================

from flask import Flask, render_template_string
import socket
from pymodbus.client.sync import ModbusTcpClient

app = Flask(__name__)

# Fungsi untuk menghubungkan Modbus TCP ke IP tertentu
def connect_modbus(ip):
    client = ModbusTcpClient(ip)
    client.connect()
    return client

# Fungsi untuk menulis status coil ke alamat 0
def write_modbus_command(client, value):
    try:
        # Menulis status coil pada alamat 0 (1 = ON, 0 = OFF)
        rr = client.write_coil(0, value)
        return "Coil berhasil diubah!"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Modbus TCP Control</title>
    </head>
    <body>
        <h1>Modbus TCP Control</h1>
        <form method="POST" action="/button1_on">
            <button type="submit">Button 1 - ON (IP 192.168.100.150)</button>
        </form>
        <form method="POST" action="/button1_off">
            <button type="submit">Button 1 - OFF (IP 192.168.100.150)</button>
        </form>
        <form method="POST" action="/button2_on">
            <button type="submit">Button 2 - ON (IP 192.168.100.152)</button>
        </form>
        <form method="POST" action="/button2_off">
            <button type="submit">Button 2 - OFF (IP 192.168.100.152)</button>
        </form>
    </body>
    </html>
    ''')

@app.route('/button1_on', methods=['POST'])
def button1_on():
    client1 = connect_modbus('192.168.100.150')
    status = write_modbus_command(client1, True)  # Menulis status ON (True)
    client1.close()
    return f'<h1>Status coil ON pada IP 192.168.100.150: {status}</h1><a href="/">Kembali</a>'

@app.route('/button1_off', methods=['POST'])
def button1_off():
    client1 = connect_modbus('192.168.100.150')
    status = write_modbus_command(client1, False)  # Menulis status OFF (False)
    client1.close()
    return f'<h1>Status coil OFF pada IP 192.168.100.150: {status}</h1><a href="/">Kembali</a>'

@app.route('/button2_on', methods=['POST'])
def button2_on():
    client = connect_modbus('192.168.100.152')
    status = write_modbus_command(client, True)  # Menulis status ON (True)
    client.close()
    return f'<h1>Status coil ON pada IP 192.168.100.152: {status}</h1><a href="/">Kembali</a>'

@app.route('/button2_off', methods=['POST'])
def button2_off():
    client = connect_modbus('192.168.100.152')
    status = write_modbus_command(client, False)  # Menulis status OFF (False)
    client.close()
    return f'<h1>Status coil OFF pada IP 192.168.100.152: {status}</h1><a href="/">Kembali</a>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
