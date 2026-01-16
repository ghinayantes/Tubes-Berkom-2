import time
import random
import string


try:
    import qrcode
    HAS_QRCODE_LIB = True
except ImportError:
    HAS_QRCODE_LIB = False


# menampilkan daftar vendor dan menu
catatan = ""
DAFTAR_VENDOR = [
    {
        "id": 1,
        "nama": "Pojok Pas Minang",
        "menu": [
            {"id": 1, "nama": "Nasi Rendang", "harga": 25000, "ketersediaan":True},
            {"id": 2, "nama": "Nasi Ayam Bakar", "harga": 15000, "ketersediaan":True},
            {"id": 3, "nama": "Nasi Ayam Korma", "harga": 15000, "ketersediaan":True},
            {"id": 4, "nama": "Nasi Ayam Pop", "harga": 15000, "ketersediaan":True},
            {"id": 5, "nama": "Ikan Goreng", "harga": 15000, "ketersediaan":True},
            {"id": 6, "nama": "Ikan Balado", "harga": 15000, "ketersediaan":True},
            {"id": 7, "nama": "Sate Padang Komplit", "harga": 24000, "ketersediaan":True},
            {"id": 8, "nama": "Lontong Sayur Padang", "harga": 12000, "ketersediaan":True},
            {"id": 9, "nama": "Perkedel", "harga": 4000, "ketersediaan":True},
        ]
    },
    {
        "id": 2,
        "nama": "Lentera Moza",
        "menu": [
            {"id": 1, "nama": "Nasi Bakar Komplit", "harga": 20000, "ketersediaan":True},
            {"id": 2, "nama": "Bakmi Yamin", "harga": 18000, "ketersediaan":True},
            {"id": 3, "nama": "Dimsum Kuah Creamy", "harga": 20000, "ketersediaan":True},
            {"id": 4, "nama": "Dimsum", "harga": 13000, "ketersediaan":True},
            {"id": 5, "nama": "Spaghetti Lumer", "harga": 15000, "ketersediaan":True},
            {"id": 6, "nama": "Pempek", "harga": 12000, "ketersediaan":True},
            {"id": 7, "nama": "Lumpia Spesial", "harga": 15000, "ketersediaan":True},
            {"id": 8, "nama": "Baso Tahu Endolita", "harga": 12000, "ketersediaan":True},
            {"id": 9, "nama": "Pisang Keju", "harga": 12000, "ketersediaan":True},
        ]
    },
    {
        "id": 3,
        "nama": "Toony",
        "menu": [
            {"id": 1, "nama": "Mie Bakso", "harga": 15000, "ketersediaan":True},
            {"id": 2, "nama": "Mie Ayam", "harga": 15000, "ketersediaan":True},
            {"id": 3, "nama": "Indomie Telur", "harga": 12000, "ketersediaan":True},
            {"id": 4, "nama": "Batagor Bumbu Kacang", "harga": 12000, "ketersediaan":True},
            {"id": 5, "nama": "Batagor Kuah", "harga": 12000, "ketersediaan":True},
            {"id": 6, "nama": "Cilok Goang", "harga": 12000, "ketersediaan":True},
            {"id": 7, "nama": "Cilok Kuah", "harga": 12000, "ketersediaan":True},
            {"id": 8, "nama": "Basreng", "harga": 10000, "ketersediaan":True},
            {"id": 9, "nama": "Seblak", "harga": 12000, "ketersediaan":True},
        ]
    },
    {
        "id": 4,
        "nama": "Sate Madu",
        "menu": [
            {"id": 1, "nama": "Nasi Sate Taichan", "harga": 18000, "ketersediaan":True},
            {"id": 2, "nama": "Nasi Sate Kacang", "harga": 18000, "ketersediaan":True},
            {"id": 3, "nama": "Nasi Ayam Bumbu Hitam", "harga": 18000, "ketersediaan":True},
            {"id": 4, "nama": "Nasi Ayam Sambal Bakar", "harga": 18000, "ketersediaan":True},
            {"id": 5, "nama": "Nasi Soto Ayam", "harga": 18000, "ketersediaan":True},
            {"id": 6, "nama": "Nasi Soto Sapi", "harga": 18000, "ketersediaan":True},
            {"id": 7, "nama": "Nasi Tongseng Ayam", "harga": 18000, "ketersediaan":True},
            {"id": 8, "nama": "Nasi Tongseng Sapi", "harga": 18000, "ketersediaan":True},
            {"id": 9, "nama": "Nasi Telor Kuah Gule", "harga": 15000, "ketersediaan":True},
        ]
    },
    {
        "id": 5,
        "nama": "Rengganis",
        "menu": [
            {"id": 1, "nama": "Nasi Goreng Kencur", "harga": 15000, "ketersediaan":True},
            {"id": 2, "nama": "Nasi Goreng Rendang", "harga": 15000, "ketersediaan":True},
            {"id": 3, "nama": "Nasi Goreng Kampung", "harga": 15000, "ketersediaan":True},
            {"id": 4, "nama": "Nasi Goreng Kari", "harga": 15000, "ketersediaan":True},
            {"id": 5, "nama": "Nasi Goreng Mawut", "harga": 15000, "ketersediaan":True},
            {"id": 6, "nama": "Mie Tek-Tek", "harga": 13000, "ketersediaan":True},
            {"id": 7, "nama": "Kwetiaw", "harga": 13000, "ketersediaan":True},
            {"id": 8, "nama": "Nasi Rawon", "harga": 18000, "ketersediaan":True},
            {"id": 9, "nama": "Nasi Soto Bandung", "harga": 18000, "ketersediaan":True},
        ]
    },
    {
        "id": 6,
        "nama": "Kedai Hijau",
        "menu": [
            {"id": 1, "nama": "Juice Apel", "harga": 10000, "ketersediaan":True},
            {"id": 2, "nama": "Juice Mangga", "harga": 12000, "ketersediaan":True},
            {"id": 3, "nama": "Juice Jeruk", "harga": 8000, "ketersediaan":True},
            {"id": 4, "nama": "Jus Pisang", "harga": 10000, "ketersediaan":True},
            {"id": 5, "nama": "Pisang Ijo Melon", "harga": 10000, "ketersediaan":True},
            {"id": 6, "nama": "Pisang Ijo Strawberry", "harga": 10000, "ketersediaan":True},
            {"id": 7, "nama": "Mojito Sirup Lyche", "harga": 10000, "ketersediaan":True},
            {"id": 8, "nama": "Mojito Sirup Melon", "harga": 10000, "ketersediaan":True},
            {"id": 9, "nama": "Susu Soda", "harga": 10000, "ketersediaan":True},
        ]
    },
    {
        "id": 7,
        "nama": "Nata Rasa D'Manzanie",
        "menu": [
            {"id": 1, "nama": "Espresso", "harga": 7000, "ketersediaan":True},
            {"id": 2, "nama": "Flat White", "harga": 15000, "ketersediaan":True},
            {"id": 3, "nama": "Japanese", "harga": 20000, "ketersediaan":True},
            {"id": 4, "nama": "Kopi Susu Gula Aren", "harga": 18000, "ketersediaan":True},
            {"id": 5, "nama": "Machiato Caramel", "harga": 18000, "ketersediaan":True},
            {"id": 6, "nama": "Latte", "harga": 15000, "ketersediaan":True},
            {"id": 7, "nama": "Matcha", "harga": 17000, "ketersediaan":True},
            {"id": 8, "nama": "Coklat", "harga": 17000, "ketersediaan":True},
            {"id": 9, "nama": "Redvelvet", "harga": 17000, "ketersediaan":True},
        ]
    },
    {
        "id": 8,
        "nama": "Kantin Bagas",
        "menu": [
            {"id": 1, "nama": "Nasi Soto Ayam", "harga": 12000, "ketersediaan":True},
            {"id": 2, "nama": "Nasi Telur Gimbal", "harga": 10000, "ketersediaan":True},
            {"id": 3, "nama": "Nasi Ayam Kipas", "harga": 15000, "ketersediaan":True},
            {"id": 4, "nama": "Nasi Ayam Lada Garam", "harga": 15000, "ketersediaan":True},
            {"id": 5, "nama": "Nasi Ayam Wijen", "harga": 15000, "ketersediaan":True},
            {"id": 6, "nama": "Nasi Ayam Krisbar", "harga": 17000, "ketersediaan":True},
            {"id": 7, "nama": "Nasi Ayam Suwir", "harga": 12000, "ketersediaan":True},
            {"id": 8, "nama": "Nasi Cokot Cakalang", "harga": 12000, "ketersediaan":True},
            {"id": 9, "nama": "Nasi Cumi Pedas", "harga": 12000, "ketersediaan":True},
        ]
    },
    {
        "id": 9,
        "nama": "Krenzzz Fried Chicken",
        "menu": [
            {"id": 1, "nama": "Nasi Chicken Katsu", "harga": 18000, "ketersediaan":True},
            {"id": 2, "nama": "Nasi Dadar Sambal", "harga": 12000, "ketersediaan":True},
            {"id": 3, "nama": "Nasi Ayam Geprek", "harga": 18000, "ketersediaan":True},
            {"id": 4, "nama": "Nasi BBQ Chicken", "harga": 18000, "ketersediaan":True},
            {"id": 5, "nama": "Nasi Black Pepper Chicken", "harga": 18000, "ketersediaan":True},
            {"id": 6, "nama": "Kebab Jumbo", "harga": 15000, "ketersediaan":True},
            {"id": 7, "nama": "Spaghetti Karage", "harga": 15000, "ketersediaan":True},
            {"id": 8, "nama": "Rice Bowl Katsu", "harga": 18000, "ketersediaan":True},
            {"id": 9, "nama": "Burger", "harga": 15000, "ketersediaan":True},
        ]
    },
    {
        "id": 10,
        "nama": "Licon",
        "menu": [
            {"id": 1, "nama": "LeMinerale", "harga": 5000, "ketersediaan":True},
            {"id": 2, "nama": "Teh Pucuk Harum", "harga": 6000, "ketersediaan":True},
            {"id": 3, "nama": "Soft Drink 1", "harga": 7000, "ketersediaan":True},
            {"id": 4, "nama": "Soft Drink 2", "harga": 7000, "ketersediaan":True},
            {"id": 5, "nama": "Soft Drink 3", "harga": 7000, "ketersediaan":True},
            {"id": 6, "nama": "Snack 1", "harga": 3000, "ketersediaan":True},
            {"id": 7, "nama": "Snack 2", "harga": 3000, "ketersediaan":True},
            {"id": 8, "nama": "Snack 3", "harga": 3000, "ketersediaan":True},
            {"id": 9, "nama": "Snack 4", "harga": 3000, "ketersediaan":True},
        ]
    }
]


def randomize_ketersediaan(list_data_vendor):
    for vendor in list_data_vendor:
        for x in vendor['menu']:
            sedia = random.randrange(0,2)
            if sedia == 0:
                x['ketersediaan'] = False
            else:
                pass


def login_website():
    while True:
        if input("Masuk link website (KantinGKU2.com): ") == "KantinGKU2.com":
            break
        else:
            print("")


# ==========================================
# BAGIAN 2: FUNGSI UNTUK VENDOR
# ==========================================


# Menampilkan semua vendor yang ada di data
def tampilkan_daftar_vendor(list_data_vendor):
    print("\n=== DAFTAR VENDOR KANTIN GKU 2 ===")
    for v in list_data_vendor:
        print(f"{v['id']}. {v['nama']}")
    print("==================================")


# Meminta user memilih nomor vendor
def minta_input_vendor(list_data_vendor):
    while True:
        try:
            pilih = int(input("Pilih nomor vendor (1–10): "))
            # Cek apakah nomor ada di rentang list (1 sampai jumlah vendor)
            if 1 <= pilih <= len(list_data_vendor):
                return list_data_vendor[pilih - 1]
            else:
                print("Nomor vendor tidak valid.")
        except ValueError:
            print("Masukkan angka saja.")


# ==========================================
# BAGIAN 3: FUNGSI UNTUK MENU
# ==========================================


# Menampilkan menu dari vendor yang sudah dipilih
def tampilkan_menu_spesifik(vendor_terpilih):
    input("Dine in atau Take away: ")
    print(f"\n=== MENU {vendor_terpilih['nama'].upper()} ===")
    for item in vendor_terpilih["menu"]:
        stock = ""
        if not item['ketersediaan']:
            stock = "(HABIS)"
        print(f"{item['id']}. {item['nama']} \t- Rp {item['harga']} \t{stock}")
    print("====================================")


catatan = ""


# Proses memilih makanan (looping sampai user ketik 'selesai')
def minta_input_pesanan(vendor_terpilih):
    keranjang = []
    while True:
        pilih_id = input("\nMasukkan Nomor Menu yang dipesan (atau ketik 'selesai' atau  ketik 'kembali'): ")
       
        if pilih_id.lower() == 'selesai':
            if not keranjang:
                print("Keranjang kosong. Silakan pesan minimal satu.")
                continue
            else:
                break
        elif pilih_id.lower() == 'kembali':
            return [],""


        # Validasi input harus angka
        if pilih_id.isdigit():
            id_menu = int(pilih_id)
            menu_ditemukan = None
           
            # Cari menu sesuai ID
            for item in vendor_terpilih['menu']:
                if item['id'] == id_menu and item['ketersediaan']:
                    menu_ditemukan = item
                    break
           
            if menu_ditemukan:
                keranjang.append(menu_ditemukan)
                print(f"✅ {menu_ditemukan['nama']} masuk keranjang.")
            else:
                print("❌ Nomor menu tidak ada atau habis.")
        else:
            print("❌ Input tidak valid.")
   
    if keranjang:
        catatan = str(input("Catatan tambahan: "))
    else:
        catatan = ""


    return keranjang, catatan


# ==========================================
# BAGIAN 4: PEMBAYARAN & LOGIKA LAIN
# ==========================================


def hitung_total_biaya(keranjang,catatan):
    print("\n--- RINCIAN PESANAN ---")
    total_biaya = 0
    for item in keranjang:
        harga = item['harga']
        total_biaya += harga
        print(f"{item['nama']} \t: Rp {harga}")


    if catatan != "":
        print(f"Catatan: {catatan}")
   
    print("-----------------------")
    print(f"TOTAL BAYAR \t: Rp {total_biaya}")
    return total_biaya


def proses_pembayaran_akhir(total_biaya):
    while True:
        print("\n--- METODE PEMBAYARAN ---")
        print("1. Cash (Tunai)")
        print("2. QRIS (Scan)")
       
        pilihan = input("Pilih metode (1/2): ")


        if pilihan == "1":
            print(f"\nSilakan bayar tunai sebesar Rp {total_biaya} di kasir.")
            print("Menunggu konfirmasi kasir...", end="")
            time.sleep(2)
            print(" LUNAS!")
            return True


        elif pilihan == "2":
            # Generate kode string acak
            kode_random = 'KANTIN-GKU2-' + ''.join(random.choices(string.digits, k=8))
           
            print("\nGenerating QR Code...", end="")
            time.sleep(1.0)
            print("\n========== QRIS ==========")
           
            # --- FITUR QRCODE (JIKA LIBRARY TERINSTALL) ---
            if HAS_QRCODE_LIB:
                # Membuat object QR Code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=1,  # Ukuran kecil agar muat di terminal
                    border=2,
                )
                qr.add_data(f"Bayar Rp{total_biaya} ke {kode_random}")
                qr.make(fit=True)
               
                # Print ke terminal
                print("Scan QR di bawah ini:")
                qr.print_ascii(invert=True)
            else:
                # Fallback jika tidak install library
                print("Scan kode ini untuk bayar (Versi Teks):")
                print(f"   [ {kode_random} ]   ")
           
            print(f"Nominal: Rp {total_biaya}")
            print("==========================")
           
            if not HAS_QRCODE_LIB:
                print("\n(TIPS: Install library 'qrcode' agar muncul gambar QR asli!)")
                print("Ketik di terminal: pip install qrcode")


            input("Tekan ENTER jika sudah transfer...")
            print("Mengecek pembayaran...", end="")
            time.sleep(2)
            print(" BERHASIL DITERIMA!")
            return True
        else:
            print("Pilihan tidak valid, coba lagi.")


def tampilkan_status_pesanan():
    # 1. Random waktu total antara 15 detik sampai 1 menit (60 detik)
    waktu_total = random.randint(15, 60)
   
    # 2. Random status awal: Apakah masuk antrean dulu atau langsung dimasak
    status_awal = random.choice(['antrean', 'langsung'])
   
    print("\n--- STATUS PESANAN ---")
    print(f"Estimasi total waktu: {waktu_total} detik.")
   
    # KONDISI 1: Masuk Antrean dulu
    if status_awal == 'antrean':
        waktu_antre = int(waktu_total * random.uniform(0.3, 0.5))
        waktu_masak = waktu_total - waktu_antre
       
        print("Status: [MENUNGGU ANTREAN] 🚶‍♂️🚶‍♀️")
        while waktu_antre > 0:
            print(f"Menunggu giliran: {waktu_antre} detik...", end='\r')
            time.sleep(1)
            waktu_antre -= 1
       
        print("\nStatus: [GILIRAN ANDA - SEDANG DIMASAK] 👨‍🍳 🔥")
        while waktu_masak > 0:
            print(f"Sedang menyiapkan: {waktu_masak} detik...", end='\r')
            time.sleep(1)
            waktu_masak -= 1
           
    # KONDISI 2: Langsung Dimasak (Sepi)
    else:
        print("Status: [LANGSUNG DIMASAK (TIDAK ADA ANTREAN)] ⚡👨‍🍳")
        waktu_sisa = waktu_total
        while waktu_sisa > 0:
            print(f"Sedang menyiapkan: {waktu_sisa} detik...", end='\r')
            time.sleep(1)
            waktu_sisa -= 1


    print("\n\n" + "="*30)
    print("       TING TUNG! 🔔")
    print("   PESANAN ANDA SUDAH SIAP!")
    print("Silakan ambil di loket pengambilan.")
    print("="*30)


# ==========================================
# BAGIAN 5: PROGRAM UTAMA (MAIN)
# ==========================================
login_website()


def main():
    print("\n\n" + "="*30)
    print("Selamat Datang di Kantin Digital GKU 2")
   
    randomize_ketersediaan(DAFTAR_VENDOR)


    # 1. Panggil fungsi tampilkan vendor
    tampilkan_daftar_vendor(DAFTAR_VENDOR)
   
    # 2. Minta user memilih vendor
    vendor_dipilih = minta_input_vendor(DAFTAR_VENDOR)
    print(f"\nAnda memilih: {vendor_dipilih['nama']}")
   
    # 3. Tampilkan Menu untuk vendor tersebut
    tampilkan_menu_spesifik(vendor_dipilih)
   
    # 4. Minta user memesan menu
    keranjang_belanja,catatan = minta_input_pesanan(vendor_dipilih)
   
    if not keranjang_belanja:
        print("\nKembali ke daftar vendor...")
        main()
        return
   
    # 5. Hitung Total
    total = hitung_total_biaya(keranjang_belanja, catatan)
   
    # 6. Konfirmasi & Bayar (Prevention Error)
    if total > 0:
        # --- PREVENTION ERROR / KONFIRMASI FINAL ---
        print("\n--- KONFIRMASI PESANAN ---")
        konfirmasi = input(f"Total tagihan Rp {total}. Lanjut ke pembayaran? (y/n): ").lower()
       
        if konfirmasi == 'y':
            bayar_sukses = proses_pembayaran_akhir(total)
           
            # 7. Timer Status (jika bayar sukses)
            if bayar_sukses:
                tampilkan_status_pesanan()
        else:
            print("Pesanan dibatalkan. Terima kasih!")
            main()
            return
           
    else:
        print("Anda tidak memesan apapun. Terima kasih.")


# Eksekusi program
if __name__ == "__main__":
    main()
