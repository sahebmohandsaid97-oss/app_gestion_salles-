from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# 1. Tester la connexion
connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion à la base de données réussie.")
connexion.close()

# 2. Ajouter une salle
salle1 = Salle("A101", "Salle Informatique", "Laboratoire", 30)
dao.insert_salle(salle1)
print("Salle ajoutée.")

# 3. Rechercher une salle par son code
salle_trouvee = dao.get_salle("A101")
if salle_trouvee:
    print("Salle trouvée :")
    salle_trouvee.afficher_infos()

# 4. Modifier une salle
salle1.libelle = "Salle Informatique Modifiée"
salle1.type = "Classe"
salle1.capacite = 35
dao.update_salle(salle1)
print("Salle modifiée.")

# 5. Récupérer et afficher toutes les salles
print("Liste des salles :")
salles = dao.get_salles()
for salle in salles:
    salle.afficher_infos()
    print("--------------------")

# 6. Supprimer une salle
dao.delete_salle("A101")
print("Salle supprimée.")