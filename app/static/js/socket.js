// Membuat koneksi WebSocket ke server
const socket = io();

// Menambahkan event listener untuk semua checkbox dengan class 'lamp' (lampu 1, 2, 3, dst.)
document.querySelectorAll(".lamp").forEach(el => {
    el.addEventListener("change", () => {
        // Mengirimkan event 'toggle' ke server dengan ID lampu dan status terbaru checkbox
        socket.emit("toggle", {
            lamp: el.id,  // ID lampu (misalnya tugu1, umkma2)
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
