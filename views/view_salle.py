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

