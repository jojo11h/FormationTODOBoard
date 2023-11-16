import tkinter as tk
from tkinter import Toplevel, messagebox

from Views.todolist_window import TodoListWindow

class LoginWindow:

    def __init__(self, root : tk.Tk):
        
        self.root = root
        root.title("Fenêtre de Connexion")
        #set window size
        root.geometry("350x120")
        root.resizable(False, False)
        # Création des éléments de l'interface
        self._label_username = tk.Label(root, text="Nom d'utilisateur :")
        self._label_username.pack()

        self._entry_username = tk.Entry(root)
        
        self._entry_username.pack()

        self._label_password = tk.Label(root, text="Mot de passe :")
        self._label_password.pack()

        self._entry_password = tk.Entry(root, show="*")  # Le paramètre show="*" cache le mot de passe
        self._entry_password.pack()

        self._button_login = tk.Button(root, text="Connexion", command=self.login)
        self._button_login.pack()
        
        #Pour tester !
        self._entry_username.insert(0, "Formation")
        self._entry_password.insert(0, "Admin")
        
        
    def login(self):
        username = self._entry_username.get()
        password = self._entry_password.get()

        if password != "Admin":
            messagebox.showerror("Échec", "Mot de passe incorrect.")
            return None
        
        self.root.destroy();#ferme la fenetre de connexion
        newRoot = tk.Tk()
        app = TodoListWindow(newRoot) # Ouvre la fenêtre TodoList
        #initialize content
        app.reload()
        
        
       


