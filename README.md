# 🏫 Kantin Digital GKU 2

Simulasi sistem pemesanan makanan berbasis terminal (CLI) menggunakan Python.  
Project ini meniru sistem kantin digital dengan fitur pemilihan vendor, pemesanan menu, pembayaran (Cash / QRIS), serta status antrean secara real-time.

---

## 📌 Deskripsi Project

**Kantin Digital GKU 2** adalah program berbasis Python yang mensimulasikan proses:

- Login ke website kantin
- Melihat daftar vendor
- Memilih menu
- Menambahkan ke keranjang
- Menambahkan catatan pesanan
- Menghitung total pembayaran
- Pembayaran (Cash / QRIS)
- Simulasi status antrean & memasak
- Notifikasi pesanan siap

Project ini dibuat sebagai latihan pemrograman Python dengan konsep:
- List of Dictionary
- Function modular
- Looping & Validation
- Randomisasi
- Simulasi waktu (time.sleep)
- Optional QR Code generation

---

## 🎯 Fitur Utama

### ✅ 1. Sistem Login Website
User harus memasukkan:
```
KantinGKU2.com
```

---

### ✅ 2. 10 Vendor Kantin

Daftar vendor yang tersedia:

1. Pojok Pas Minang  
2. Lentera Moza  
3. Toony  
4. Sate Madu  
5. Rengganis  
6. Kedai Hijau  
7. Nata Rasa D'Manzanie  
8. Kantin Bagas  
9. Krenzzz Fried Chicken  
10. Licon  

---

### ✅ 3. Random Ketersediaan Menu
Setiap program dijalankan:
- Status menu akan diacak (tersedia / habis)
- Menu habis akan diberi tanda `(HABIS)`

---

### ✅ 4. Sistem Keranjang
- Bisa memilih lebih dari satu menu
- Ketik `selesai` untuk checkout
- Ketik `kembali` untuk kembali ke daftar vendor
- Bisa menambahkan catatan tambahan

---

### ✅ 5. Pembayaran

Tersedia 2 metode:

#### 💵 Cash
Simulasi pembayaran tunai di kasir.

#### 📱 QRIS
- Generate kode pembayaran random
- Jika library `qrcode` terinstall → tampil QR ASCII
- Jika tidak → tampil kode teks saja

---

### ✅ 6. Simulasi Status Pesanan

Setelah pembayaran berhasil:
- Estimasi waktu 15–60 detik
- Bisa masuk antrean dulu atau langsung dimasak
- Countdown real-time
- Notifikasi:

```
TING TUNG! 🔔
PESANAN ANDA SUDAH SIAP!
```

---

## 🛠️ Teknologi yang Digunakan

- Python 3.x
- Library bawaan:
  - time
  - random
  - string
- Optional:
  - qrcode

---

## 📦 Instalasi & Cara Menjalankan

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/kantin-digital-gku2.git
cd kantin-digital-gku2
```

---

### 2️⃣ Install Python (Jika Belum Ada)

Download dari:
https://www.python.org/downloads/

Cek versi:
```bash
python --version
```

---

### 3️⃣ (Opsional) Install Library QR Code

Agar QR tampil dalam bentuk ASCII:

```bash
pip install qrcode
```

Jika tidak diinstall, program tetap berjalan (fallback ke kode teks).

---

### 4️⃣ Jalankan Program

```bash
python nama_file.py
```

Contoh:
```bash
python kantin.py
```

---

## 🧠 Struktur Program

Program dibagi menjadi beberapa bagian:

### 🔹 Bagian 1 – Data Vendor
- DAFTAR_VENDOR
- randomize_ketersediaan()

### 🔹 Bagian 2 – Vendor
- tampilkan_daftar_vendor()
- minta_input_vendor()

### 🔹 Bagian 3 – Menu & Keranjang
- tampilkan_menu_spesifik()
- minta_input_pesanan()

### 🔹 Bagian 4 – Pembayaran
- hitung_total_biaya()
- proses_pembayaran_akhir()
- tampilkan_status_pesanan()

### 🔹 Bagian 5 – Main Program
- main()

---

## 🔄 Alur Program

```
Login Website
      ↓
Tampilkan Vendor
      ↓
Pilih Vendor
      ↓
Tampilkan Menu
      ↓
Pilih Menu
      ↓
Hitung Total
      ↓
Konfirmasi
      ↓
Pembayaran
      ↓
Status Pesanan
      ↓
Selesai
```

---

## 🎓 Konsep Python yang Dipakai

Project ini melatih:

- Function modular programming
- Nested list & dictionary
- Looping (while & for)
- Exception handling (try-except)
- Conditional logic
- Random generator
- Time delay simulation
- ASCII QR Code
- Recursion (pemanggilan ulang main())

---

## 🚀 Pengembangan Selanjutnya (Ide Improvement)

- Sistem login dengan username & password
- Database (SQLite / MySQL)
- Sistem saldo user
- Riwayat transaksi
- Admin panel
- GUI (Tkinter / PyQt)
- Web version (Flask / Django)

---

## 📄 License

Project ini dibuat untuk keperluan pembelajaran.  
Bebas digunakan dan dikembangkan kembali.
