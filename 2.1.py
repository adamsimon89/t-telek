"""A program számolja össze, hogy hány darab 'A' vagy 'a' betűvel kezdődő szó van az adott listában (amely a 'Próbáld ki!' gombra kattintva elérhető)! 
A képernyőre írja is ki a feltételnek megfelelő szavakat!"""

szavak=["alma", "deszka", "asztal", "körte", "ablak"]
helyes_szavak=[]

for szo in szavak:
    if szo.startswith("a"):
        (helyes_szavak).append(szo)
    if szo.startswith("A"):
        (helyes_szavak).append(szo)
    
print(helyes_szavak)