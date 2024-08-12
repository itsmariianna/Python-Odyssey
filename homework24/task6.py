# 6. Գրել ծրագիր, որը օգտագործողից կստանա մուտքային արժեք(int) և կհաշվի արդյոք այդ թիվը պարզ է, թե՝ ոչ։

number = int(input("Enter number to check if it is prime or not: "))

if number <= 1:
    print(f"{number} is not prime")

elif number == 2:
    print(f"{number} is prime")

elif number > 2:
    for i in range(3, int(number ** 0.5)+ 1, 2):
        if number % i == 0:
            print(f"{number} is not prime")
            break
    print(f"{number} is prime")
