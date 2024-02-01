class Zadanie:
  def __init__(self, opis, pytanie):
    self.opis = opis
    self.pytanie = pytanie
    
  def myfunc(self):
    print("opis " + self.opis)

  def wykonaj(self, bohater):
    print("name: " + bohater.name)
    print("zadanie: " + self.opis)



