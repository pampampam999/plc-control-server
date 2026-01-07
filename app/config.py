# Mapping IP untuk setiap grup
PLC_IPS = {
    "tugu": "192.168.100.150",
    #"umkma": "192.168.100.151",
    "umkmb": "192.168.100.152",
}

PLC_PORT = 502

COIL_MAPPING = {

    "tugu1": 0,
    "tugu2": 1,
    "tugu3": 2,
    "tugu4": 3,
    "tugu5": 4,
    "tugu6": 5,
    "tugu7": 6,
    "tugu8": 7,


    "umkma1": 0,
    "umkma2": 1,
    "umkma3": 2,
    "umkma4": 3,
    "umkma5": 4,
    "umkma6": 5,
    "umkma7": 6,


    "umkmb1": 0,
    "umkmb2": 1,
    "umkmb3": 2,
    "umkmb4": 3,
    "umkmb5": 4,
}

# Menyimpan konfigurasi untuk setiap grup
GROUPS = {
    "tugu": ["tugu1", "tugu2", "tugu3", "tugu4", "tugu5", "tugu6", "tugu7", "tugu8"],
    #"umkma": ["umkma1", "umkma2", "umkma3", "umkma4", "umkma5", "umkma6", "umkma7"],
    "umkmb": ["umkmb1", "umkmb2", "umkmb3", "umkmb4", "umkmb5"],
}