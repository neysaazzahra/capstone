
stok = [{'Nama':'Beras', 'Jumlah':150, 'Lorong':5, 'Rak': 7, 'Harga':12000, 'Status Makanan': True},
        {'Nama':'Kacang', 'Jumlah':70, 'Lorong':2, 'Rak': 3, 'Harga': 9000, 'Status Makanan': True},
        {'Nama':'Ketan', 'Jumlah':30, 'Lorong':5, 'Rak': 2, 'Harga': 19000, 'Status Makanan': True},
        {'Nama':'Jagung', 'Jumlah':45, 'Lorong':1, 'Rak': 1, 'Harga': 13000, 'Status Makanan': True},
        {'Nama':'Minyak', 'Jumlah':100, 'Lorong':3, 'Rak':4, 'Harga': 15000, 'Status Makanan': False}]

def header():
    print('''\nStok Barang
Index\t|Nama\t\t|Jumlah(kg)\t|Lorong\t|Rak\t|Harga\t|Status Makanan''')
    
def aStok(idx=99):
    if idx is 99:
        for s in range(len(stok)):
            print("{}\t|{}\t\t|{}\t\t|{}\t|{}\t|{}\t|{}".format(s, stok[s]['Nama'], stok[s]['Jumlah'], stok[s]['Lorong'], stok[s]['Rak'], stok[s]['Harga'], stok[s]['Status Makanan']))
    else:
        print("{}\t|{}\t\t|{}\t\t|{}\t|{}\t|{}\t|{}".format(idx, stok[idx]['Nama'], stok[idx]['Jumlah'], stok[idx]['Lorong'], stok[idx]['Rak'], stok[idx]['Harga'], stok[idx]['Status Makanan']))

def allStok():
    header()
    aStok()
    """_summary_
    """
def cariNama(x):
    for s in stok:
        if s['Nama'].lower() == x.lower():
            return stok.index(s)
        else:
            continue
    return 'none'
    
        
def update(namakey,indx):
    if namakey not in ('Nama','Jumlah','Lorong','Rak','Harga', 'Status Makanan'):
        print('Data tidak bisa diupdate. Tidak ada data mengenai "{}"'.format(namakey))
        return None
    new = input('Masukkan {} baru untuk {}: '.format(namakey,stok[indx]['Nama']))
    tanya = input('Anda yakin ingin mengupdate {} untuk {}?\n(y/n)\n'.format(namakey,stok[indx]['Nama']))
    if tanya == 'y':
        if namakey in ('Jumlah','Lorong','Rak','Harga'):
            while True:
                try:
                    new = int(new)
                    break
                except:
                    new = input('Input harus berupa angka bulat. Masukkan {} baru untuk {}: '.format(namakey,stok[indx]['Nama']))
        elif namakey == 'Status Makanan':
            while True:
                if new.lower() not in ('false, true'):
                    print('Status makanan harus berupa True atau False')
                    new = input('Masukkan {} baru untuk {}: '.format(namakey,stok[indx]['Nama']))
                    continue
                else:
                    break
            if new.lower() == 'false':
                new = bool('')
            elif new.lower() == 'true':
                new = bool(new)
                
        stok[indx][namakey] = new
    else:
        print("Data'{}' tidak jadi diupdate.".format(stok[indx]['Nama']))

while True:
    while True:
        try:
            menu = int(input('''\nDaftar menu aplikasi gudang:
                     
    1. Daftar barang
    2. Mengubah data barang
    3. Menambah barang baru
    4. Menghapus barang
    5. Mengambil barang
    6. Filter barang
    99. Keluar dari aplikasi

    Ketik angka menu yang ingin dijalankan: '''))
            break
        except:
            print('Masukkan angka.')    
        
    if menu == 99:
        print('Terima kasih telah menggunakan aplikasi!')
        quit()
    
    elif menu == 1:
        while True:
            menu1 = int(input('''\nMenu:
1. Seluruh data stok
2. Data salah satu benda
88. Kembali ke menu utama
Data apa yang ingin ditampilkan? '''))
            if menu1 == 1:
                if len(stok) == 0:
                    print('Tidak ada benda di gudang.')
                    continue
                allStok()
                continue
            elif menu1 == 2:
                if len(stok) == 0:
                    print('Tidak ada benda di gudang.')
                    continue
                dataReq = input('Masukkan nama benda yang ingin ditampilkan: ').lower()
                idx = cariNama(dataReq)
                if idx == 'none':
                    print("Tidak ada '{}' di gudang".format(dataReq))
                    continue
                header()
                aStok(idx)
                continue
            elif menu1 == 88:
                break
            else:
                print('Input yang anda masukkan tidak valid. Silakan coba lagi')
    elif menu == 2:
        while True:
            try:
                menu2 = int(input('''\nMenu:
1. Ubah data suatu benda
88.Kembali ke menu utama
Menu yang ingin dijalankan: '''))
                break
            except:
                print('Masukkan angka')
                continue
        if menu2 == 1:
            allStok()
            valChg = input('\nMasukkan nama benda yang ingin diubah: ')
            idv = cariNama(valChg)
            if idv == 'none':
                print("Benda {} tidak ada di gudang.".format(valChg))
                continue
            header()
            aStok(idv)
            quest = input("Anda ingin melanjutkan untuk mengupdate '{}'?\n(y/n)\n".format(valChg))
            while True:
                if quest == 'y':
                    keyChg = input('Masukkan data yang ingin diubah (Nama/Jumlah/Lorong/Rak/Harga/Status Makanan): ').title()
                    update(keyChg,idv)
                    header()
                    aStok(idv)
                    break
                elif quest == 'n':
                    print("Data '{}' tidak jadi diupdate.".format(valChg))
                    header()
                    aStok(idv)
                    break
                else:
                    print("Input tidak dikenali. ketik 'y' jika ingin mengupdate dan 'n' untuk membatalkan")
            
        elif menu2 ==88:
            break
        
        else:
            print('Input yang anda masukkan tidak valid. Silakan coba lagi')
    elif menu == 3:
        while True:
            while True:
                try:
                    menu3 = int(input('''\nMenu:
1. Tambahkan benda baru
88. Kembali ke menu utama
Pilih menu yang ingin dijalankan: '''))
                    break
                except:
                    print('Masukkan angka')
                    continue
            if menu3 == 88:
                break
            elif menu3 == 1:
                allStok()
                newNama = input('Masukkan nama barang baru: ').capitalize()
                cek3 = cariNama(newNama)
                if cek3 != 'none':
                    print('Barang sudah ada. Jika ingin mengubah data benda, kembali ke menu utama dan pilih menu nomor 2 untuk mengubah benda.')
                    continue
                while True:
                    try:
                        newJumlah = int(input('Masukkan jumlah {} (dalam kg): '.format(newNama)))
                        break
                    except:
                        print('Masukkan angka')
                        continue
                while True:
                    try:
                        newLorong = int(input('Masukkan lorong tempat {}: '.format(newNama)))
                        break
                    except:
                        print('Masukkan angka')
                    continue
                while True:
                    try:
                        newRak = int(input('Masukkan rak tempat {}: '.format(newNama)))
                        break
                    except:
                        print('Masukkan angka')
                        continue
                while True:
                    try:    
                        newHarga = int(input('Masukkan harga {} (per kg): '.format(newNama)))
                        break
                    except:
                        print('Masukkan angka')
                    continue
                while True:
                    while True:
                        try:
                            newStat = (int(input('Apakah {} adalah makanan?\nKetik \'1\' jika ya, ketik \'0\' jika tidak: '.format(newNama))))
                            break
                        except:
                            print('Masukkan angka')
                    if newStat in (1,0):
                        if newStat == 1:
                            newStat = True
                        else:
                            newStat = False
                        break
                    else:
                        print('Masukkan 0 atau 1')
                ndict = {'Nama': newNama, 'Jumlah':newJumlah, 'Lorong':newLorong, 'Rak': newRak, 'Harga':newHarga, 'Status Makanan': newStat}
                quest = input('''Anda yakin ingin menambahkan {} ke gudang?\n(y/n)\n'''.format(newNama))
                if quest == 'y':
                    stok.append(ndict)
                    print('Benda berhasil ditambahkan!')
                    allStok()
                    continue
                print("Data '{}' tidak tersimpan".format(newNama))
                allStok()
                
            else:
                print('Input yang anda masukkan tidak valid. Silakan coba lagi')
    elif menu == 4:
        while True:
            while True:
                try:
                    menu4 = int(input('''\nMenu:
1. Hapus benda
88. Kembali ke menu utama
Pilih menu yang ingin dijalankan: '''))
                    break
                except:
                    print('Masukkan angka sesuai menu.')
            if menu4 == 88:
                break
            elif menu4 == 1:
                allStok()
                deleted = input('Masukkan nama barang yang ingin dihapus: ')
                cek4 = cariNama(deleted)
                if cek4 == 'none':
                    print("Barang '{}' tidak ada dalam gudang.".format(deleted))
                    continue
                quest = input("Anda yakin ingin menghapus '{}'?\n(y/n)\n".format(deleted))
                if quest == 'y':
                    del stok[cek4]
                    allStok()
                else:
                    print('Data {} tidak jadi dihapus.'.format(deleted))
                    allStok()
            else:
                print('Input yang anda masukkan tidak valid. Silakan coba lagi')
    elif menu == 5:
        while True:
            while True:
                try:
                    menu5 = int(input('''Pilihan Menu:
1. Ambil Benda
88. Kembali ke menu utama
Menu yang ingin dijalankan: '''))
                    break
                except:
                    print('Masukkan angka sesuai menu.')
            if menu5 == 88:
                break
            elif menu5 == 1:
                ygDiambil =[]
                allStok()
                while True:
                    amblBenda = input('Masukkan nama benda yang ingin diambil: ')
                    idxBenda = cariNama(amblBenda)
                    if idxBenda == 'none':
                        print("Benda '{}' tidak ada di gudang.".format(amblBenda))
                        continue
                    while True:
                        try:
                            jmlBenda = float(input('Masukkan jumlah {} yang ingin diambil: '.format(amblBenda)))
                            break
                        except:
                            print('Anda hanya bisa memasukkan angka.')
                            continue
                    if jmlBenda > stok[idxBenda]['Jumlah'] :
                        print('Jumlah {a} yang ingin diambil terlalu banyak. Sisa {a} di gudang adalah {b} kg.'.format(a=amblBenda,b=stok[idxBenda]['Jumlah']))
                        continue
                    elif jmlBenda < 0:
                        print('Tidak bisa memasukkan angka negatif. Silakan coba lagi.')
                        continue
                    stok[idxBenda]['Jumlah'] = stok[idxBenda]['Jumlah'] - jmlBenda
                    ambl = [stok[idxBenda]['Nama'], jmlBenda, stok[idxBenda]['Lorong'], stok[idxBenda]['Rak']]
                    ygDiambil.append(ambl)
                    tny = input('Ingin mengambil benda lain?\n(y/n)\n')
                    if tny != 'y':
                        break
                weight = 0
                ttlBenda = 0
                print('''Daftar benda yang ingin diambil dari gudang:
Nama\t\t|Jumlah(kg)\t|Lorong\t|Rak''')
                for q in ygDiambil:
                    print(f'{q[0]}\t\t|{q[1]}\t\t|{q[2]}\t|{q[3]}')
                    weight += q[1]
                    ttlBenda += 1
                print('\nBenda yang diambil: {} benda.\nTotal berat benda yang diambil: {} kg.'.format(ttlBenda,weight))
            else:
                print('Input yang anda masukkan tidak valid. Silakan coba lagi')    
    elif menu == 6:
        while True:
            while True:
                try:
                    menu6 = int(input('''\nMenu:
1. Filter berdasarkan harga
2. Filter berdasarkan status makanan
88. Kembali ke menu utama
Masukkan menu yang dipilih: '''))
                    break
                except:
                    print('Masukkan angka sesuai menu.')
            if menu6 == 88:
                break
            elif menu6 == 1:
                while True:
                    try:
                        rntgBwh = int(input('Masukkan batas bawah harga yang ingin difilter: '))
                        break
                    except:
                        print('Masukkan angka bulat.')
                while True:
                    try:
                        rntgAts = int(input('Masukkan batas atas harga yang ingin difilter: '))
                        break
                    except:
                        print('Masukkan angka bulat.')
                listIdx = []
                for w in stok:
                    if (w['Harga'] >= rntgBwh) and (w['Harga'] <= rntgAts):
                        indx = stok.index(w)
                        listIdx.append(indx)
                if len(listIdx) > 0:
                    header()
                    for r in listIdx:
                        aStok(r)
                    continue
                else:
                    print('Tidak ada data yang sesuai filter.')
                    continue
            elif menu6 == 2:
                while True:
                    try:
                        food = int(input('Data apa yang ingin ditampilkan?\n1. Makanan\n2. Bukan Makanan\n'))
                        break
                    except:
                        print('Masukkan angka 1 atau 2.')
                listIdx = []
                for y in stok:
                    if food == 1:
                        if y['Status Makanan'] == True:
                            indx = stok.index(y)
                            listIdx.append(indx)
                    elif food == 2:
                        if y['Status Makanan'] == False:
                            indx = stok.index(y)
                            listIdx.append(indx)
                    else:
                        print('Anda tidak memasukkan angka sesuai menu yang tersedia.')
                        break
                if len(listIdx) > 0:
                    header()
                    for r in listIdx:
                        aStok(r)
                else:
                    print('Tidak ada data yang sesuai filter.')
                    
                        
            else:
                print('Input yang anda masukkan tidak valid. Silakan coba lagi')
    else:
        print('Input yang anda masukkan tidak valid. Silakan coba lagi')
        