from services.service_salle import ServiceSalle
from models.salle import Salle


service = ServiceSalle()


print("Liste des salles :")
salles = service.recuperer_salles()

for salle in salles:
    salle.afficher_infos()


nouvelle_salle = Salle("B101", "Salle Test", "Classe", 40)

succes, message = service.ajouter_salle(nouvelle_salle)
print(message)


nouvelle_salle.libelle = "Salle Test Modifiee"

succes, message = service.modifier_salle(nouvelle_salle)
print(message)


succes, message = service.supprimer_salle("B101")
print(message)