import customtkinter as ctk
from services.service_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("600x400")

        self.service_salle = ServiceSalle()

        # ===============================
        # Frame Informations Salle
        # ===============================

        self.frame_infos = ctk.CTkFrame(self)
        self.frame_infos.pack(pady=10)

        ctk.CTkLabel(self.frame_infos, text="Code").grid(row=0, column=0)
        self.entry_code = ctk.CTkEntry(self.frame_infos)
        self.entry_code.grid(row=0, column=1)

        ctk.CTkLabel(self.frame_infos, text="Libelle").grid(row=1, column=0)
        self.entry_libelle = ctk.CTkEntry(self.frame_infos)
        self.entry_libelle.grid(row=1, column=1)

        ctk.CTkLabel(self.frame_infos, text="Type").grid(row=2, column=0)
        self.entry_type = ctk.CTkEntry(self.frame_infos)
        self.entry_type.grid(row=2, column=1)

        ctk.CTkLabel(self.frame_infos, text="Capacite").grid(row=3, column=0)
        self.entry_capacite = ctk.CTkEntry(self.frame_infos)
        self.entry_capacite.grid(row=3, column=1)

        # ===============================
        # Frame Actions
        # ===============================

        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

        self.btn_ajouter = ctk.CTkButton(
            self.frame_actions,
            text="Ajouter",
            command=self.ajouter_salle
        )
        self.btn_ajouter.grid(row=0, column=0, padx=5)

        self.btn_modifier = ctk.CTkButton(
            self.frame_actions,
            text="Modifier",
            command=self.modifier_salle
        )
        self.btn_modifier.grid(row=0, column=1, padx=5)

        self.btn_supprimer = ctk.CTkButton(
            self.frame_actions,
            text="Supprimer",
            command=self.supprimer_salle
        )
        self.btn_supprimer.grid(row=0, column=2, padx=5)

        self.btn_rechercher = ctk.CTkButton(
            self.frame_actions,
            text="Rechercher",
            command=self.rechercher_salle
        )
        self.btn_rechercher.grid(row=0, column=3, padx=5)

    # ===============================
    # Ajouter salle
    # ===============================

    def ajouter_salle(self):

        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        salle = Salle(code, libelle, type_salle, capacite)

        self.service_salle.ajouter_salle(salle)

    # ===============================
    # Modifier salle
    # ===============================

    def modifier_salle(self):

        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        salle = Salle(code, libelle, type_salle, capacite)

        self.service_salle.modifier_salle(salle)

    # ===============================
    # Supprimer salle
    # ===============================

    def supprimer_salle(self):

        code = self.entry_code.get()

        self.service_salle.supprimer_salle(code)

    # ===============================
    # Rechercher salle
    # ===============================

    def rechercher_salle(self):

        code = self.entry_code.get()

        salle = self.service_salle.rechercher_salle(code)

        if salle:

            self.entry_libelle.delete(0, "end")
            self.entry_type.delete(0, "end")
            self.entry_capacite.delete(0, "end")

            self.entry_libelle.insert(0, salle.libelle)
            self.entry_type.insert(0, salle.type)
            self.entry_capacite.insert(0, salle.capacite)