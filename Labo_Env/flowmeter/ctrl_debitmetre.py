#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ctrl_debitmetre.py: Contrôle d'un débitmètre.

Auteur: Émile Jetzer
Date: 2020-01-08

Interface de lecture du débitmètre.
"""

# Librairies graphiques
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from pathlib import Path
import numpy as np
import pandas as pd

# Librairie de graphiques dans tk
import Graphic


class AffichageDebitmetre(tk.Frame):
    """Classe d'affichage des données du débitmètre."""

    def __init__(self, parent):
        """
        Affichage du débitmètre dans une interface graphique.

        Paramètres
        ----------
        parent :
            Objet parent dans l'afficahge graphique.

        Returns
        -------
        AffichageDebitmetre

        """
        super().__init__(parent)
        self.parent = parent

    def cadre_graphique(self):
        pass
