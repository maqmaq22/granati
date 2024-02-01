import random

class Zadanie:
  def __init__(self, opis,hp,mana,php,pmana,bohater,wrog):
    self.opis = opis
    self.nagrodahp = hp
    self.nagrodamana = mana
    self.przegranahp = php
    self.przegranamana = pmana
    self.bohater = bohater
    self.wrog = wrog

  def czyzyje (self,postac):
      if(postac.hp<=0):
          return False
      else:
          return True

  def zwyciezca(self):
    manastart=self.bohater.mana
    hpstart=self.bohater.hp

    prog=50
    roznica= self.bohater.poziom - self.wrog.poziom
    prog=prog + 10*roznica
    zmprog = False
    while( self.czyzyje(self.bohater) and self.czyzyje(self.wrog)):
        if(self.bohater.mana==0):
            print("Bohater nie ma many. Walczy wręcz i traci 1 hp!")
            self.bohater.hp-=1
            if(not zmprog):
                prog-=15
                zmprog=True
        else:
            self.bohater.mana-=1
        self.starcie(prog)
    if(self.czyzyje(self.bohater)):
        self.bohater.mana = manastart + self.nagrodamana
        self.bohater.hp = hpstart + self.nagrodahp
        return self.bohater
    else:
        return self.wrog
  
  


  def starcie(self,prog):
      wylosowane = random.randrange(1,100)
      obrazenia = 1
      if(wylosowane <= prog):
          if(wylosowane<=8):
              obrazenia = 3+abs(self.bohater.poziom-self.wrog.poziom)*random.randrange(1,3)
              print("Bohater zadał obrażenie krytyczne!")
          self.wrog.hp -= obrazenia
          #print(f'Wróg stracil {obrazenia} hp. Wrogowi zostało {self.wrog.hp} hp')
      else:
          self.bohater.hp -= obrazenia
          #print(f'Bohater stracił {obrazenia} hp. Bohaterowi zostało {self.bohater.hp} hp')
      print(f'Obrażenia: {obrazenia} hp. {self.bohater.name}: {self.bohater.hp} hp : {self.wrog.name}: {self.wrog.hp} hp')
          


