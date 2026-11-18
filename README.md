# Pantau Nusantara

Peta kejadian Indonesia oleh **savemeours**, dibangun dengan HTML, CSS, JavaScript, dan Leaflet untuk GitHub Pages.

Website: https://savemeours.github.io/pantau-nusantara/

## Fitur

- Gempa, titik panas, banjir BNPB, status gunung api, laporan warga, dan peringatan cuaca.
- Peta interaktif, detail kejadian, pencarian, filter kategori dan rentang waktu.
- Tampilan desktop dan panel daftar khusus ponsel.
- Peta terang/gelap dan tombol kembali ke cakupan Indonesia.

## Data

Aplikasi membaca berkas GeoJSON/JSON publik dari https://whatsupindonesia.id/data/live/ langsung saat dibuka dan setiap lima menit. Data tetap mengikuti frekuensi pembaruan sumber. `live.json` merupakan cadangan snapshot; jika sumber tidak terjangkau, aplikasi menampilkan data cadangan dengan waktu sumber dan penanda data lama.

Atribusi agregator: [What'sUpIndonesia](https://whatsupindonesia.id/) oleh Erick Jahja. Sumber primer meliputi BMKG, USGS, NASA FIRMS, BNPB, PVMBG, dan PetaBencana.id. Implementasi antarmuka dan kode aplikasi ini dibuat secara mandiri.

Titik panas bukan konfirmasi kebakaran. Peringatan cuaca dipisahkan dari laporan banjir. Aplikasi bukan layanan peringatan resmi; ikuti kanal resmi untuk keputusan keselamatan.

Tidak ada token, akun, atau backend yang diperlukan. Peta menggunakan OpenStreetMap/CARTO dan Leaflet. Ikon menggunakan Font Awesome Free.

## Menjalankan lokal

Jalankan `python -m http.server 8000` di direktori repositori, kemudian buka http://localhost:8000. Untuk memperbarui snapshot secara manual, jalankan `python sync.py`.
