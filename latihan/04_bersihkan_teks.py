teks = " Belajar Python itu menyenangkan "
teks = teks.strip()
while "  " in teks:
 teks = teks.replace("  ", " ")
print(teks.capitalize())
