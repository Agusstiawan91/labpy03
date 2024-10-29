# Modal awal
modal_awal = 100_000_000

# Persentase laba per bulan
laba_bulan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]  # Persentase laba untuk bulan 1-8

# Total laba
total_laba = 0

# Menghitung laba per bulan
for bulan in range(8):
    laba = modal_awal * laba_bulan[bulan]
    total_laba += laba
    print(f"Laba bulan ke-{bulan + 1} sebesar: {laba:.1f}")

# Menampilkan total laba
print(f"\nTotal laba adalah: {total_laba:.1f}")
