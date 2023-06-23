def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def kalkulator():
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("0. Wyjście")

    while True:
        wybor = input("Twój wybór: ")

        if wybor == '1':
            liczba1 = float(input("Podaj pierwszą liczbę: "))
            liczba2 = float(input("Podaj drugą liczbę: "))
            wynik = dodawanie(liczba1, liczba2)
            print("Wynik: ", wynik)
        elif wybor == '2':
            liczba1 = float(input("Podaj pierwszą liczbę: "))
            liczba2 = float(input("Podaj drugą liczbę: "))
            wynik = odejmowanie(liczba1, liczba2)
            print("Wynik: ", wynik)
        elif wybor == '0':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
kalkulator()