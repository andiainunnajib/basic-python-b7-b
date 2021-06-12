nama_customer = []
umur = []


n = 1
while n != 0 :
    print ("1. masukan data.")
    print ("2. tampilkan data.")
    print ("3. Hapus data.")
    print ("0. exit.")

    n = int(input("masukan pilihan anda : "))
    print('')
    print('')
    print('')
    if n == 1 :
        masukNama = input("masukan nama : ")
        nama_customer.append({'nama' : masukNama})
        masukUmur = input("masukan umur : ")
        umur.append({'umur' : masukUmur})
       
        
    elif n == 2 :
        penentu = True
        for i in range (len(nama_customer)) :
            if penentu :
                print ("Nama customer\tumur")
            print ("Nama {} umur {} tahun".format(nama_customer[i],umur[i]))
            print (nama_customer[i]['nama'], umur[i]['umur'])
            
            penentu = False

    elif n == 3 :
        masukNama = input("masukan nama customer : ")
        for i in range (len(nama_customer)) :
            if masukNama == nama_customer[i]['nama'] :
                print (i)
                del nama_customer[i]
                del umur[i]
                break
            
    

   
    print('')
    print('')
    print('')