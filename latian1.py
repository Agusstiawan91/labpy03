import random

# Meminta input nilai N dari pengguna
N = int(input("Masukkan nilai N: "))
    
# Inisialisasi list untuk menyimpan data
data = []
    
# Menghasilkan N angka acak yang lebih kecil dari 0,5
while len(data) < N:
    nilai_acak = random.random()  # Menghasilkan angka acak antara 0 dan 1
    if nilai_acak < 0.5:
        data.append(nilai_acak)  # Menyimpan angka acak ke dalam list
    
# Menampilkan hasil
for i in range(N):
    print(f"data ke: {i + 1} => {data[i]}")
    
print("Selesai")
