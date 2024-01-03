# In squid game season 2 este un joc matematic cu media a 5 numere si numarul cel ai apropiat de medie
# Jocul poarta denumirea de king of diamonds

# creem 5 numere ca reprezeinta variabilele de intrare ale jucatorilor
numberlist = [] # creem o lista in care adaugam numerele

# creem 5 numere ca reprezeinta variabilele de intrare ale jucatorilor
number1 = int(input("Enter your number between 1 and 100: "))
if number1 < 0 or number1 > 100:
    print("Error, the number must be between 1 and 100. Please try again.")
else:
    numberlist.append(number1)

number2 = int(input("Enter your number between 1 and 100:  "))
if number2 < 0 or number2 > 100:
    print("Error, the number must be between 1 and 100. Please try again.")
else:
    numberlist.append(number2)

number3 = int(input("Enter your number between 1 and 100: "))
if number3 < 0 or number3 > 100:
    print("Error, the number must be between 1 and 100. Please try again.")
else:
    numberlist.append(number3)

number4 = int(input("Enter your number between 1 and 100: "))
if number4 < 0 or number4 > 100:
    print("Error, the number must be between 1 and 100. Please try again.")
else:
    numberlist.append(number4)

number5 = int(input("Enter your number between 1 and 100: "))
if number5 < 0 or number5 > 100:
    print("Error, the number must be between 1 and 100. Please try again.")
else:
    numberlist.append(number5)


# afisam lista cu numerele primite de la jucatori
print("Your list of numbers is: ", numberlist)

#Afisam media celor 5 numere primite
numberaverage = float((number1+number2+number3+number4+number5)/5)
print("Media numerelor primite este: ", numberaverage)


# compararea mediei numerelor cu fiecare numar in parte
# vom folosi round pentru a obtine 2 zecimale

diff1 = numberaverage - number1
print("Diferenta dintre medie si primul numar este: ", round(diff1,2))
if diff1 < 0:
    print("Numarul 1 este peste medie. ")
elif diff1 == 0:
    print("Numarul 1 este egal cu media.")
else:
    print("Numaul 1 este sub medie")

diff2 = numberaverage - number2
print("Diferenta dintre medie si al doilea numar este: ", round(diff2,2))
if diff2 < 0:
    print("Numarul 2 este peste medie. ")
elif diff2 == 0:
    print("Numarul 2 este egal cu media.")
else:
    print("Numaul 2 este sub medie")

diff3 = numberaverage - number3
print("Diferenta dintre medie si al treilea numar este: ", round(diff3,2))
if diff3 < 0:
    print("Numarul 3 este peste medie. ")
elif diff3 == 0:
    print("Numarul 3 este egal cu media.")
else:
    print("Numaul 3 este sub medie")

diff4 = numberaverage - number4
print("Diferenta dintre medie si al patrulea numar este: ", round(diff4,2))
if diff4 < 0:
    print("Numarul 4 este peste medie. ")
elif diff4 == 0:
    print("Numarul 4 este egal cu media.")
else:
    print("Numaul 4 este sub medie")

diff5 = numberaverage - number5
print("Diferenta dintre medie si al cincilea numar este: ", round(diff5,2))
if diff5 < 0:
    print("Numarul 5 este peste medie. ")
elif diff5 == 0:
    print("Numarul 5 este egal cu media.")
else:
    print("Numarul 5 este sub medie")

# Stocam diferentele intr-o lista separata

diff_list = []
diff_list.append(diff1)
diff_list.append(diff2)
diff_list.append(diff3)
diff_list.append(diff4)
diff_list.append(diff5)

# afisam lista cu diferenta
print("Diferentele dintre medie si numere au fost stocate in lista de mai jos: \n",diff_list)

# pentru a afla care numar este cel mai apropiat de medie, putem folosi functia min si functia lambda
closestnumber = min(diff_list, key=lambda x: abs(x))

print("Numarul cel mai apropiat de 0 este:", closestnumber)

print("Jucatorul care va fi eliminat este cel care are", closestnumber, "ca diferenta dintre medie si numarul sau. ")

print("Multumesc pentru ai aruncat o privire peste implementarea jocului vazut de mine intr-un serial. :) ")