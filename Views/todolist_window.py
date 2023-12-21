import tkinter as tk
from tkinter import simpledialog, ttk
from tkinter.messagebox import askokcancel, showinfo
import uuid
from Database.user_repository import UserRepository
from Entities.todo_entity import TodoEntity
from Services.configuration_database_service import ConfigurationDatabaseService
from Services.configuration_file_service import ConfigurationFileService
from Services.todo_service import TodoService
from config_window import ConfigWindow
from datetime import datetime


class TodoListWindow:
    def __init__(self, root):

        # GUI Setup
        self.root = root
        self.root.title("Todo List")

        self.tree = ttk.Treeview(self.root, columns=(
            "Id", "Tâche", "Traité"), show="headings")
        self.tree.heading("Tâche", text="Libellé de la tâche",
                          command=lambda: self.sort_by_column("Tâche", False))
        self.tree.heading("Traité", text="Traité",
                          command=lambda: self.sort_by_column("Traité", False))
        self.tree.pack(pady=15, padx=15, fill=tk.BOTH, expand=True)

        # Buttons
        frame = tk.Frame(self.root)
        frame.pack(pady=15, padx=15)

        tk.Button(frame, text="Ajouter",
                  command=self.add_todo).pack(side=tk.LEFT)
        tk.Button(frame, text="Supprimer",
                  command=self.delete_todo).pack(side=tk.LEFT)
        tk.Button(frame, text="Mettre à jour",
                  command=self.update_todo).pack(side=tk.LEFT)
        tk.Button(frame, text="Configuration",
                  command=self.show_configuration).pack(side=tk.LEFT)

    def reload(self):

        configurationEntity = ConfigurationDatabaseService().get_singleton()
        todoEntities = TodoService().get_all()

        # Effacer le contenu de la liste
        self.tree.delete(*self.tree.get_children())

        for todoEntity in todoEntities:
            done = "Oui" if todoEntity.isProcessed else "Non"
            self.tree.insert("", tk.END, values=(
                todoEntity.id, todoEntity.label, done), tags=('task',))
            self.tree.tag_configure(
                'task', foreground=configurationEntity.todoBackgroundColor)

    def sort_by_column(self, col, reverse):
        """
        Trie le treeview par la colonne sélectionnée !
        """
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]
        l.sort(reverse=reverse)

        # réarranger les éléments dans l'ordre trié
        for index, (val, k) in enumerate(l):
            self.tree.move(k, '', index)

        # inverser l'ordre de tri pour le prochain appel
        self.tree.heading(
            col, command=lambda: self.sort_by_column(col, not reverse))

    def show_configuration(self):
        config = ConfigWindow()
        # Open configuration and update treeview on close
        config_window = config.open_configuration(self.root)
        # Capture the close event, and refresh treeview
        config_window.protocol(
            "WM_DELETE_WINDOW", lambda: self.__close_window(config_window, self.reload))

    def __close_window(self, window, callback):
        callback()
        window.destroy()

    def add_todo(self):
        task_dialog = tk.Toplevel(self.root)
        task_dialog.title("Ajouter une tâche")

        label_entry = tk.Entry(task_dialog, width=40)
        label_entry.pack(padx=20, pady=5)

        done_var = tk.BooleanVar(value=False)
        done_check = tk.Checkbutton(
            task_dialog, text="Traité", variable=done_var)
        done_check.pack(padx=20, pady=5)

        def on_ok():
            if label_entry.get():
                todoEntity = TodoEntity(
                    uuid.uuid4(),
                    label_entry.get(),
                    done_var.get(),
                    '3032baba-823a-11ee-ad04-00155d000d32',  # TODO
                    datetime.now(),
                    '3032baba-823a-11ee-ad04-00155d000d32',  # TODO
                    datetime.now())
                # Sauvegarde en base de données
                TodoService().insert(todoEntity)
                self.reload()
            task_dialog.destroy()

        tk.Button(task_dialog, text="OK", command=on_ok).pack(
            side=tk.LEFT, padx=20, pady=5)
        tk.Button(task_dialog, text="Annuler", command=task_dialog.destroy).pack(
            side=tk.LEFT, padx=20, pady=5)

        task_dialog.bind("<Return>", lambda _: on_ok())

    def update_todo(self):
        index = self.tree.selection()
        if not index:
            showinfo("Opération impossible", "Veuillez sélectionner une ligne")
            return

        todo_id: uuid = self.tree.item(index, "values")[0]

        # Recharger le todo complet de la base de données
        todoEntity: TodoEntity = TodoService().get_by_id(todo_id)

        task_dialog = tk.Toplevel(self.root)
        task_dialog.title("Mettre à jour la tâche")

        label_entry = tk.Entry(task_dialog, width=40)
        label_entry.insert(0, todoEntity.label)
        label_entry.pack(padx=20, pady=5)

        done_var = tk.BooleanVar(value=todoEntity.isProcessed)
        done_check = tk.Checkbutton(
            task_dialog, text="Traité", variable=done_var)
        done_check.pack(padx=20, pady=5)

        def on_ok():
            if label_entry.get():
                todoEntity.label = label_entry.get()
                todoEntity.isProcessed = done_var.get()
                todoEntity.modificationDate = datetime.now()
                todoEntity.modificationUserId = '3032baba-823a-11ee-ad04-00155d000d32'  # TODO
                TodoService().update(todoEntity)
                self.reload()
            task_dialog.destroy()

        tk.Button(task_dialog, text="OK", command=on_ok).pack(
            side=tk.LEFT, padx=20, pady=5)
        tk.Button(task_dialog, text="Annuler", command=task_dialog.destroy).pack(
            side=tk.LEFT, padx=20, pady=5)

        task_dialog.bind("<Return>", lambda _: on_ok())

    def delete_todo(self):
        index = self.tree.selection()
        if index:
            answer = askokcancel(
                "Supprimer", "Voulez-vous supprimer la ligne sélectionnée ?")
            if answer:
                todo_id = self.tree.item(index, "values")[0]
                TodoService().delete_by_id(todo_id)
                self.reload()
        else:
            showinfo("Opération impossible", "Veuillez sélectionner une ligne")
