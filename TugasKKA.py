print("Nama: Faatihah Ahmad Raihan Ilmihi")
print("Kelas: XI RPL 2")
print("Absen: 10")

# === 1. Variabel dan Tipe Data ===
# a. Buat 3 variabel bertipe data: int, float, str, dan list
angka_int = 10
angka_float = 3.14
teks = "Hello Python"
daftar = [1, 2, 3]

# b. Tampilkan tipe datanya dengan fungsi type()
print("=== Variabel dan Tipe Data ===")
print("Tipe data angka_int:", type(angka_int))
print("Tipe data angka_float:", type(angka_float))
print("Tipe data teks:", type(teks))
print("Tipe data daftar:", type(daftar))


# === 2. List dan Manipulasi ===
print("\n=== List dan Manipulasi ===")
# a. Buat list belanja
belanja = ["beras", "minyak", "telur"]

# b. Tambahkan gula dan kopi dengan fungsi
belanja.append("gula")
belanja.append("kopi")

# c. Tampilkan semua item dengan perulangan
for item in belanja:
    print(item)


# === 3. Dictionary ===
print("\n=== Dictionary ===")
# a. Buat dictionary harga belanjaan
harga = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}

# b. Hitung total harga
total_harga = sum(harga.values())
print("Total harga belanja:", total_harga)


# === 4. Fungsi ===
print("\n=== Fungsi (Persegi Panjang) ===")
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

# Contoh penggunaan
p, l = 10, 5
luas, keliling = hitung_persegi_panjang(p, l)
print(f"Luas persegi panjang ({p}x{l}): {luas}")
print(f"Keliling persegi panjang ({p}x{l}): {keliling}")


# === 5. Percabangan ===
print("\n=== Percabangan (Kategori Usia) ===")
usia = int(input("Masukkan usia: "))

if 0 <= usia <= 13:
    kategori = "Anak"
elif 14 <= usia <= 24:
    kategori = "Remaja"
elif 25 <= usia <= 49:
    kategori = "Dewasa"
elif usia > 50:
    kategori = "Lansia"
else:
    kategori = "Usia tidak valid"

print("Kategori usia:", kategori)


#Modul Lanjutan

str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is",
type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is",
type(str_numbers_to_int))

integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is",
type(integer_to_str))

num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))
num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))

# Equal to
8 == 8
# Not equal to
8 != 9
# Greater than
8 > 9
# Less than
8 < 9
# Less than
8 <= 9
# Less than
9 >= 9

a = True
b = True
print(a and b)
print(a or b)
print(not b)
#logic
5 > 6 and 6 < 7

e = 8
f = 2
# Summation
sum = e + f
print(f"The sum of e with f is : {sum}\n")
# Reduction
red = e - f
print(f"The reduction of e with f is : {red}\n")
# Multiplication
multi = e * f
print(f"The multipication of e with f is : {multi}\n")
# Division
divi = e / f
print(f"The quotient of e with f is : {divi}\n")
# Modulo
mod = e % f
print(f"The remainder of e with f is : {mod}\n")
# Power
pow = e ** f
print(f"The power of e of f is : {pow}\n")

name = str(input("What is your name : "))
age = int(input("What's your age : "))
print("Name: ", name)
print("Age: ", age)

# normal print
print('Hi all! I am', name, 'age', age, 'years old')
# format print
print(f'Hi all! I am {name} age {age} years old')
# format print
print(f'Hi all! I am %s age %d years old'%(name, age))
# fortmat output
print(30*"=")
print("Temperature Calculator Program")
print(30*"=")

# Using If-Else
try:
    your_GPA = float(input("Enter your GPA: "))
    if 4.0 >= your_GPA >= 0.0:
        if 4.0 >= your_GPA >= 3.80:
            print(f"Damn you've got a magna cumlaude with your {your_GPA} GPA")
        elif 3.50 <= your_GPA < 3.80:
            print(f"Cool! You've got a cumlaude with your {your_GPA} GPA")
        elif 3.00 <= your_GPA < 3.50:
            print(f"You've got a stable GPA tho with {your_GPA}")
        elif your_GPA < 3.0:
            print(f"You need a stable GPA")
    else:
        print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
except:
    print("Please enter a valid GPA")


# Using match case
try:
    status_code = int(input("Enter your status code: "))
    print("Your code means:")
    match status_code:
        case 200:
            print("Success!")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 402:
            print("Payment Required")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
except:
    print("Please enter a valid status code")
