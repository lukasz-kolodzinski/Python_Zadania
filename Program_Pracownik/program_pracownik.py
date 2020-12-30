def nr_telefonu() -> int:
    """
    Funkcja przyjmuje input od użytkownika (nr telefonu)
    Następnie konwertuje input na int
    :return: nr telefonu pracownika
    :rtype: int
    """
    while True:
        try:
            nr_telefonu = (input("Podaj swój numer telefonu:\n "))
            nr_telefonu = nr_telefonu.replace('-','')
            nr_telefonu = nr_telefonu.replace(' ', '')
            nr_telefonu = nr_telefonu.strip()
            return int(nr_telefonu)
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
    nazwisko = nazwisko.strip()
    miejsce_zamieszkania = input("Twoje miejsce zamieszkania:\n ")
    miejsce_zamieszkania = miejsce_zamieszkania.strip()
    nmr_telefonu = nr_telefonu()
    #print("{}\n{}\n{}".format(nazwisko, miejsce_zamieszkania, nmr_telefonu))

dane_pracownikow()