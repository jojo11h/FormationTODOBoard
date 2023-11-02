import tkinter as tk
from tkinter import simpledialog, ttk
from config_window import open_configuration


class Todo:
    def __init__(self, label, done=False):
        self.label = label
        self.done = done

class TodoApp:

    def __init__(self, root):
        self.todos = []
        self.color_var = tk.StringVar(value="black")
        
        # GUI Setup
        self.root = root
        self.root.title("TODO List")

        self.tree = ttk.Treeview(self.root, columns=("Tâche", "Traité"), show="headings")
        self.tree.heading("Tâche", text="Libellé de la tâche")
        self.tree.heading("Traité", text="Traité", command=lambda: self.sort_by_column("Traité", False))
        self.tree.pack(pady=15, padx=15, fill=tk.BOTH, expand=True)

        # Buttons
        frame = tk.Frame(self.root)
        frame.pack(pady=15, padx=15)

        tk.Button(frame, text="Ajouter", command=self.add_todo).pack(side=tk.LEFT)
        tk.Button(frame, text="Supprimer", command=self.delete_todo).pack(side=tk.LEFT)
        tk.Button(frame, text="Mettre à jour", command=self.update_todo).pack(side=tk.LEFT)
        tk.Button(frame, text="Configuration", command=self.show_configuration).pack(side=tk.LEFT)

    def sort_by_column(self, col, reverse):
        """
        Trie le treeview par colonne donnée !
        """
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]
        l.sort(reverse=reverse)

        # réarranger les éléments dans l'ordre trié
        for index, (val, k) in enumerate(l):
            self.tree.move(k, '', index)

        # inverser l'ordre de tri pour le prochain appel
        self.tree.heading(col, command=lambda: self.sort_by_column(col, not reverse))


    def show_configuration(self):
        open_configuration(self.root, self.color_var, self.update_treeview)
        

    def add_todo(self):
        task_dialog = tk.Toplevel(self.root)
        task_dialog.title("Ajouter une tâche")

        label_entry = tk.Entry(task_dialog, width=40)
        label_entry.pack(padx=20, pady=5)

        done_var = tk.BooleanVar(value=False)
        done_check = tk.Checkbutton(task_dialog, text="Traité", variable=done_var)
        done_check.pack(padx=20, pady=5)

        def on_ok():
            if label_entry.get():
                todo = Todo(label_entry.get(), done=done_var.get())
                self.todos.append(todo)
                self.update_treeview()
            task_dialog.destroy()

        tk.Button(task_dialog, text="OK", command=on_ok).pack(side=tk.LEFT, padx=20, pady=5)
        tk.Button(task_dialog, text="Annuler", command=task_dialog.destroy).pack(side=tk.LEFT, padx=20, pady=5)

        task_dialog.bind("<Return>", lambda _: on_ok())

    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for todo in self.todos:
            done = "Oui" if todo.done else "Non"
            self.tree.insert("", tk.END, values=(todo.label, done), tags=('task',))
            self.tree.tag_configure('task', foreground=self.color_var.get())

    def update_todo(self):
        index = self.tree.selection()
        if not index:
            return

        old_task = self.tree.item(index, "values")[0]

        for todo in self.todos:
            if todo.label == old_task:
                task_dialog = tk.Toplevel(self.root)
                task_dialog.title("Mettre à jour la tâche")

                label_entry = tk.Entry(task_dialog, width=40)
                label_entry.insert(0, todo.label)
                label_entry.pack(padx=20, pady=5)

                done_var = tk.BooleanVar(value=todo.done)
                done_check = tk.Checkbutton(task_dialog, text="Traité", variable=done_var)
                done_check.pack(padx=20, pady=5)

                def on_ok():
                    if label_entry.get():
                        todo.label = label_entry.get()
                        todo.done = done_var.get()
                        self.update_treeview()
                    task_dialog.destroy()

                tk.Button(task_dialog, text="OK", command=on_ok).pack(side=tk.LEFT, padx=20, pady=5)
                tk.Button(task_dialog, text="Annuler", command=task_dialog.destroy).pack(side=tk.LEFT, padx=20, pady=5)

                task_dialog.bind("<Return>", lambda _: on_ok())
                break


    def delete_todo(self):
        index = self.tree.selection()
        if index:
            task = self.tree.item(index, "values")[0]
            for i, todo in enumerate(self.todos):
                if todo.label == task:
                    del self.todos[i]
                    break
            self.update_treeview()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
