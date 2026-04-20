from data.dao_salle import DataSalle


class ServiceSalle:

    def __init__(self):

        self.dao_salle = DataSalle()


    def ajouter_salle(self, salle):

        if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
            return False, "Toutes les informations sont obligatoires"

        if salle.capacite < 1:
            return False, "Capacite invalide"

        self.dao_salle.insert_salle(salle)

        return True, "Salle ajoutee"


    def modifier_salle(self, salle):

        self.dao_salle.update_salle(salle)

        return True, "Salle modifiee"


    def supprimer_salle(self, code):

        self.dao_salle.delete_salle(code)

        return True, "Salle supprimee"


    def rechercher_salle(self, code):

        return self.dao_salle.get_salle(code)


    def recuperer_salles(self):

        return self.dao_salle.get_salles()