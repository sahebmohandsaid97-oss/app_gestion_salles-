from data.dao_salle import DataSalle


class ServiceSalle:

    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):

        if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
            return False, "Toutes les informations sont obligatoires"

        if salle.capacite < 1:
            return False, "La capacite doit etre >= 1"

        self.dao_salle.insert_salle(salle)

        return True, "Salle ajoutee avec succes"

    def modifier_salle(self, salle):

        if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
            return False, "Toutes les informations sont obligatoires"

        if salle.capacite < 1:
            return False, "La capacite doit etre >= 1"

        self.dao_salle.update_salle(salle)

        return True, "Salle modifiee avec succes"

    def supprimer_salle(self, code):

        if not code:
            return False, "Code obligatoire"

        self.dao_salle.delete_salle(code)

        return True, "Salle supprimee avec succes"

    def rechercher_salle(self, code):

        if not code:
            return None

        return self.dao_salle.get_salle(code)