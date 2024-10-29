import random

def generate_data(n):
    for i in range(1, n + 1):
        value = random.random()
        print(f"data ke: {i} => {value}")
    print("selesai")

# Masukkan nilai N
N = int(input("Masukkan nilai N: "))
generate_data(N)
