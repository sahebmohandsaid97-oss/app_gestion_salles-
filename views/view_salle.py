import customtkinter as ctk
from tkinter import ttk
from services.service_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()

        # Cadre Informations Salle
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

        # Cadre Actions
        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

        ctk.CTkButton(
            self.frame_actions,
            text="Ajouter",
            command=self.ajouter_salle
        ).grid(row=0, column=0, padx=5)

        ctk.CTkButton(
            self.frame_actions,
            text="Modifier",
            command=self.modifier_salle
        ).grid(row=0, column=1, padx=5)

        ctk.CTkButton(
            self.frame_actions,
            text="Supprimer",
            command=self.supprimer_salle
        ).grid(row=0, column=2, padx=5)

        ctk.CTkButton(
            self.frame_actions,
            text="Rechercher",
            command=self.rechercher_salle
        ).grid(row=0, column=3, padx=5)

        # Cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "libelle", "type", "capacite"),
            show="headings"
        )

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")

        self.treeList.column("code", width=50)
        self.treeList.column("libelle", width=150)
        self.treeList.column("type", width=100)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        # Étape 8.3
        self.lister_salles()

    def ajouter_salle(self):

        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            int(self.entry_capacite.get())
        )

        self.service_salle.ajouter_salle(salle)

        # Étape 8.4
        self.lister_salles()

    def modifier_salle(self):

        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            int(self.entry_capacite.get())
        )

        self.service_salle.modifier_salle(salle)

        # Étape 8.5
        self.lister_salles()

    def supprimer_salle(self):

        code = self.entry_code.get()
        self.service_salle.supprimer_salle(code)

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

    def lister_salles(self):

        self.treeList.delete(*self.treeList.get_children())

        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))