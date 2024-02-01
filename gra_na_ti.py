from bohater import Postac
from zadanie import Zadanie
import random
kasa = 1000
i = 0
bohater = Postac("Zdziś", 2)
wrog1 = Postac("Voldemort", random.randrange(2,4))
wrog2 = Postac("Terminator", random.randrange(4,6))
wrog3 = Postac("Shrek", random.randrange(6,8))
wrog4 = Postac("Janusz",random.randrange(8,10))
wrog5 = Postac("Mała syrenka", random.randrange(10,12))
wrog6 = Postac("Gandalf", random.randrange(12,14))
wrog7 = Postac("Walter W.", random.randrange(14,16))
wrog8 = Postac("John Wick", random.randrange(16,20))
z1 = Zadanie("Jakiś opis",5,5,3,3,bohater,wrog1)
z2 = Zadanie("Jakiś opis", 5,5,3,3,bohater,wrog2)
z3 = Zadanie("Jakiś opis", 5,5,3,3,bohater,wrog3)
z4 = Zadanie("Jakiś opis", 5,5,3,3,bohater,wrog4)
z5 = Zadanie("Jakiś opis", 5,5,3,3,bohater,wrog5)
z6 = Zadanie("Jakiś opis", 5,5,3,3,bohater,wrog6)
z7 = Zadanie("Jakiś opis", 5,5,3,3,bohater,wrog7)
z8 = Zadanie("Jakiś opis", 5,5,3,3,bohater,wrog8)
bohater.mana=4000
lista_zadan = [z1, z2, z3, z4, z5, z6, z7, z8]
for z in lista_zadan:
    i += 1
    wspolczynnik = round((random.randrange(-20,20))/100*bohater.hp);
    z.wrog.hp = bohater.hp + wspolczynnik;

    print("==================")
    print(f'== RUNDA {i} ==')
    print("==================")
    print(f'Bohater {z.bohater.name} jest na poziomie {z.bohater.poziom} i walczy z wrogiem na poziomie {z.wrog.poziom}, którym jest {z.wrog.name}')
    print(f' {bohater.name} ma {bohater.hp} hp.')
    print(f' {z.wrog.name} ma {z.wrog.hp} hp.')
    while True:
        obstawiono=input("obstaw kto wygra. bohater czy wrog?(B/W):")
        if (obstawiono == 'W' or obstawiono == 'B'):
            break;
        else:
            print("wprowadzono niepoprawny znak. dozwolone jest B lub W")

    while True:
        kwota_int = None
        while kwota_int is None:
            try:
                kwota_int=int(input(f'posiadasz {kasa} dolarow. ile obstawiasz?: '))
            except ValueError:
                print("Wprowadź poprawną kwotę - liczba całkowita.")
            
        if (kwota_int <= kasa):
           break;
        else:
           print("nie masz tyle kabony")

    kasa -= kwota_int
    hpprzed = bohater.hp 

    if(z.zwyciezca() == bohater):
        print("bohater wygral")
        print(f'Po walce bohater ma many: {bohater.mana}')
        print(f'Po walce bohater ma hp: {bohater.hp}')
        if(obstawiono == 'B'):
            if(z.bohater.poziom<z.wrog.poziom):
                kasa += (kwota_int)*abs(z.bohater.poziom - z.wrog.poziom)+2*kwota_int
            else:
                kasa += 2*kwota_int
            print("GRATULACJE DOBRZE OBSTAWILES!")
        else:
            print(f'PRZEGRALES {kwota_int}$')
       
    else:
        if(obstawiono == 'W'):
            if(z.bohater.poziom>z.wrog.poziom):
                kasa += (kwota_int)*abs(z.bohater.poziom - z.wrog.poziom)+2*kwota_int
            else:
                kasa += 2*kwota_int
            print("GRATULACJE DOBRZE OBSTAWILES!")
        else:
            print(f'PRZEGRALES {kwota_int}$')
        bohater.hp = hpprzed*round((bohater.poziom)/3)
        bohater.mana += 5

    print(f'twoje pieniadze po rundzie to {kasa}')

    if(kasa == 0):
        break
    bohater.poziom += 2

print(f'koniec gry, dziekuje twoje pieniadze na koncu to: {kasa}')

        

  
      