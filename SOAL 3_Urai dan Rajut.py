##SOAL 3 - Mengurai dan Merajut Kata
## Mengurai
def urai(string): #Buat function terlebih dahulu
    output = '' #Buat variabel kosong untuk function untuk diisi oleh parameter nanti
    for i in range(len(string)): #Build for loops untuk menjadikannya list agar mudah untuk penambahan huruf dimasing" huruf/kata
        for j in range(0,i+1): #Nested loops untuk menambah kata di output dan panjang loop adalah dimulai dari 0 dan sebanyak i+1
            output+=string[j] #Untuk disetiap Huruf akan urut ditambahkan mulai dari index ke-0 sampai habis 
    return output #Return hasil dari output yang didapat dari looping
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

##Merajut
def rajut(string): #Buat function terlebih dahulu
    output = '' #Buat variabel kosong untuk function untuk diisi oleh parameter nanti
    tampung = 0 #Variabe penampung untuk mengetahui index mana yang akan di tambahkan ke dalam output
    increment = 2 #Variabel yang berguna untuk menambah penampung agar mendapatkan angka kelipatan yang di inginkan (2,5,9 dan seterusnya)
    for i in range(0,len(string)): #Build for loops untuk menjadikannya list agar mudah untuk mengurani huruf dimasing" huruf/kata
        if i == tampung: #Apabila index i sesuai dengan kelipatan  yang di inginkan ( variable penampung ) maka akan menambahkan value string[i] ke output
            output+= string[i] #Menambahkan value string[i] kedalam output
            tampung+=increment #Menambahkan penampung sesuai dengan value increment saat ini agar di looping selanjutnya akan mendapat kelipatan yang di inginkan
            increment+=1 #lalu increment akan ditambah 1 setiap kali masuk ke kondisi ini ( 2 3 4 5  dan seterusnya ) yang akan di pakai untuk menambah penampung kedepannya agar kelipatan sesuai yang diinginkan
    return output #Return hasil dari output yang didapat dari looping

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))