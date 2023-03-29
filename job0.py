import Personne
from Personne import Personne

names = ["Paul", "Ringo", "John", "George"]
lastnames = ["McCartney", "Starr", "Lenon", "Harrison"]
message = ["Bonjour je me présente", "je suis le"]
iterateur =  1

for name, lastname in zip(names, lastnames):
        new = Personne(lastname, name)
        if iterateur == 1:
            new.SePresenter(message[0])
        else:
            new.SePresenter((message[1]+ " "+ str(iterateur) +" éme Beatles"))
        
        iterateur +=1