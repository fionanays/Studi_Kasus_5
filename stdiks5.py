def tarif_kamar(jenis_kamar, durasi_menginap):
    if jenis_kamar == "1":
        harga = 200000
    elif jenis_kamar == "2":
        harga = 350000
    else:
        return 0

    jumlah_pembayaran = harga * durasi_menginap
    return jumlah_pembayaran

def jumlah_pembayaran():
    print("====== JENIS KAMAR HOTEL ======")
    print("1. Kamar Standard")
    print("2. Kamar Deluxe")
    jenis_kamar = input("Masukkan jenis kamar yang ingin dipesan(1/2): ")
    
    lama_menginap = int(input("Masukkan jumlah malam menginap Anda: "))

    hasil = tarif_kamar(jenis_kamar, lama_menginap)

    print("\n====== STRUK PEMBAYARAN ======")
    print("Jenis kamar: ", jenis_kamar)
    print("Waktu menginap: ", lama_menginap, "malam")
    print("Biaya menginap di hotel: Rp", hasil)
    print("Terima kasih telah menginap di hotel kami")

jumlah_pembayaran()