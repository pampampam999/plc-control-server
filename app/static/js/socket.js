// Membuat koneksi WebSocket ke server
const socket = io();

// Menambahkan event listener untuk semua checkbox dengan class 'lamp' (lampu 1, 2, 3)
document.querySelectorAll(".lamp").forEach(el => {
    el.addEventListener("change", () => {
        // Mengirim event 'toggle' ke server ketika checkbox diubah
        socket.emit("toggle", {
            lamp: el.id,  // ID lampu yang dikontrol (lamp1, lamp2, lamp3)
            state: el.checked  // Status checkbox (ON/OFF)
        });
    });
});

// Menerima update state dari server
socket.on("state_update", state => {
    // Mengupdate checkbox sesuai dengan status state terbaru dari server
    Object.keys(state).forEach(lamp => {
        const el = document.getElementById(lamp);
        if (el) {
            el.checked = state[lamp];  // Menyesuaikan checkbox dengan state lampu
        }
    });
});
