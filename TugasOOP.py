#Soal 1

num=int(input("Type in a number: "))

def oddoreven(num):
    if num % 2 == 0:
        return "this number is even"
    else:  
        return "this number is odd"
    
#Soal 2

number = int(input("Type in your number: ")) 

def posnegnol(number):
    if num < 0:
        return "This number is negative"   
    if num > 0:
        return "This number is Positive"   
    if num == 0:
        return "This number is 0"   
    
#Soal 3

anagram = str()

def is_anagram():
    str1 = input("Enter the first word: ")
    str2 = input("Enter the second word: ")
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    if sorted(s1) == sorted(s2):
        print(f"'{str1}' and '{str2}' are anagrams.")
    else:
        print(f"'{str1}' and '{str2}' are NOT anagrams.")

is_anagram()

#Soal 4

def factorial():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"{n}! = {result}")

factorial()

#Soal 5

def palindrome():
    text = input("Enter a word: ")
    cleaned = text.replace(" ", "").lower()
    if cleaned == cleaned[::-1]:
        print(f"'{text}' is a palindrome.")
    else:
        print(f"'{text}' is NOT a palindrome.")

palindrome()
