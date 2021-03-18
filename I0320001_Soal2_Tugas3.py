# Data diri hobi, sosmed, lagu kesukaan, dan makanan kesukaan
dict = {'Nama':'Adhiatmaka','Hobi1':'Basket','Hobi2':'Futsal','Hobi3':'Main game', 'Hobi4': 'Mancing',
        'Sosmed1':'ig:@adhiatmaka','Sosmed2':'ig2:@adhiyo','Sosmed3':'line:@adhiatmaka_',
        'Sosmed4':'twitter:@adhiap','Lagu1':'Hope','Lagu2':'Mood','Lagu3':'Robbery',
        'Lagu4': 'Gods Plan' ,'Makanan1':'Nasi Goreng','Makanan2':'Indomie Aceh','Makanan3':'Mie Ayam',
        'Makanan4': 'Sate Kambing'}

# Mengubah salah satu hobi dan sosmed, hapus 2 makanan, dan tambah 1 hobi
dict['Hobi4'] = 'Memasak'
dict['Sosmed2'] = 'tiktok : @adhikaliye'
del dict['Makanan2']
del dict['Makanan4']
dict['Hobi5'] = 'Riding'

# Menampilkan dictionary
print (dict)
