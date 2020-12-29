def nr_telefonu() -> int:
    """
    Funkcja przyjmuje input od użytkownika (nr telefonu)
    Następnie konwertuje input na int
    :return: nr telefonu pracownika
    :rtype: int
    """
    while True:
        try:
            # TODO: trim, ignorowanie myślnikówm białych znaków
            nr_telefonu = int(input("Podaj swój numer telefonu:\n "))
            return nr_telefonu
        except ValueError:
            print("Podano błędną wartość. Spróbuj jeszcze raz.")

def dane_pracownikow():
    """
    Funkcja ktora umożliwia przechowywanie i
    zarządzanie danymi pracowników
    :return: pracownik{}
    """
    pracownik = {}
    powitanie = print("Wprowadź kolejno wymienione poniżej dane")
    nazwisko = input("Twoje nazwisko:\n ")
    miejsce_zamieszkania = input("Twoje miejsce zamieszkania:\n ")
    nr_telefonu()

dane_pracownikow()