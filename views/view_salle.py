import customtkinter as ctk
from services.service_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("600x400")

        self.service_salle = ServiceSalle()
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

        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

        self.btn_ajouter = ctk.CTkButton(self.frame_actions, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0, padx=5)

        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=5)

        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=5)

        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=5)
    def ajouter_salle(self):

        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_salle = self.entry_type.get()
        capacite = int(self.entry_capacite.get())

        salle = Salle(code, libelle, type_salle, capacite)

        self.service_salle.ajouter_salle(salle)
        self.btn_ajouter.configure(command=self.ajouter_salle)

