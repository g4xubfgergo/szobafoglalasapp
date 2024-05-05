from datetime import datetime, timedelta

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 5000)  

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000) 

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglal(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None

    def lemond(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def listaz_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

def fill_system(szalloda):
    szoba1 = EgyagyasSzoba("101")
    szoba2 = KetagyasSzoba("201")
    szoba3 = EgyagyasSzoba("301")

    szalloda.add_szoba(szoba1)
    szalloda.add_szoba(szoba2)
    szalloda.add_szoba(szoba3)

    szalloda.foglal("101", datetime.now() + timedelta(days=1))
    szalloda.foglal("201", datetime.now() + timedelta(days=2))
    szalloda.foglal("301", datetime.now() + timedelta(days=3))
    szalloda.foglal("101", datetime.now() + timedelta(days=4))
    szalloda.foglal("201", datetime.now() + timedelta(days=5))

def main():
    szalloda = Szalloda("Példa Szálloda")
    fill_system(szalloda)

    while True:
        print("\n1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        choice = input("Válassz egy műveletet: ")

        if choice == "1":
            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                if datum < datetime.now():
                    print("Hibás dátum: a foglalás csak jövőbeli időpontra lehetséges.")
                    continue
                ar = szalloda.foglal(szobaszam, datum)
                if ar is not None:
                    print(f"A foglalás sikeres! Ár: {ar} Ft")
                else:
                    print("Hibás szobaszám.")
            except ValueError:
                print("Hibás dátum formátum.")
        elif choice == "2":
            szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
            datum_str = input("Adja meg a lemondás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                if not szalloda.lemond(szobaszam, datum):
                    print("Nincs ilyen foglalás.")
                else:
                    print("A foglalás sikeresen lemondva.")
            except ValueError:
                print("Hibás dátum formátum.")
        elif choice == "3":
            szalloda.listaz_foglalasok()
        elif choice == "4":
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
