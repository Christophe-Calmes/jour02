class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self, message):
        print(message + " " + self.prenom + " " + self.nom + ".")

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def set_nom(self, new_nom):
        self.nom = new_nom

    def set_prenom(self, new_prenom):
        self.prenom = new_prenom


class Auteur(Personne):
    def __init__(self, nom, prenom, oeuvres, nameBook):
        super().__init__(nom, prenom)
        self.oeuvres = oeuvres
        self.nameBook = nameBook

    def titre(self, nameBook):
        self.nameBook = nameBook
        print("Mon nouveau livre est " + self.nameBook)

    def set_oeuvre(self, new_oeuvre):
        #Equivalent à écrire un livre
        self.oeuvres.append(new_oeuvre)

    def get_oeuvre(self):
        print(self.oeuvres)
    
    def Lister_Oeuvre(self):
        print("Les oeuvre de " + self.nom + " sont :")
        for title in self.oeuvres:
            print(title)

