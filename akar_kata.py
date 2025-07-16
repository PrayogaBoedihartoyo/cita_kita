def ganti_kata_akar(kataAkar, kalimat):
    kata_kata = kalimat.split()
    hasil = []
    
    for kata in kata_kata:
        kata_diganti = False
        
        for akar in kataAkar:
            if akar in kata:
                if kata == akar:
                    hasil.append(kata)
                    kata_diganti = True
                    break
                
                elif kata.startswith(akar):
                    hasil.append(akar)
                    kata_diganti = True
                    break
                
                elif akar in kata:
                    hasil.append(akar)
                    kata_diganti = True
                    break
        
        if not kata_diganti:
            hasil.append(kata)
    
    return " ".join(hasil)

while True:
    print("\n" + "="*50)
    print("Ingin coba lagi? (y/n): ", end="")
    pilihan = input().lower()
    
    if pilihan == 'n' or pilihan == 'no':
        print("Program selesai. Terima kasih!")
        break
    elif pilihan == 'y' or pilihan == 'yes':
        print("\nMasukkan kata-kata akar (pisahkan dengan koma):")
        input_kata_akar = input().strip()
        kata_akar_list = [kata.strip() for kata in input_kata_akar.split(',')]
        
        print("\nMasukkan kalimat yang akan diproses:")
        input_kalimat = input().strip()
        
        print(f"\nData Input:")
        print(f"kataAkar = {kata_akar_list}")
        print(f"kalimat = \"{input_kalimat}\"")
        
        hasil = ganti_kata_akar(kata_akar_list, input_kalimat)
        print(f"\nHasil: \"{hasil}\"")
    else:
        print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")