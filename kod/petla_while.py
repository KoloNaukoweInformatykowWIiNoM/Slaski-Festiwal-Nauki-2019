imie = "ala"
zdanie = "ala ma kota"

print("\nPo pętli: ")
print("Imię: ", imie, ", zdanie: ", zdanie, "\n")

while len(imie) < len(zdanie):
    print("Ala jest krótsza od zdania...")
    imie += "x"

print("\nPo pętli: ")
print("Imię: ", imie, ", zdanie: ", zdanie)
