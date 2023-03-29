import Personne
from Personne import Personne
from Personne import Auteur

oeuvres = ["L'appel de Cthulhu", "Dagon", "Démons et merveilles"]
nameBook = ""
newAuteur = Auteur("Howard", "Lovecraft", oeuvres, nameBook)
newAuteur.SePresenter("Je suis ")
newAuteur.titre("Celui qui chuchotait dans les ténébres.")
nameBook = "Celui qui chuchotait dans les ténébres."
newAuteur.set_oeuvre(nameBook)
newAuteur.Lister_Oeuvre()
