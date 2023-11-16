import tkinter as tk
from Services.configuration_database_service import ConfigurationDatabaseService
from Services.configuration_file_service import ConfigurationFileService
from Views.login_window import LoginWindow

from Views.todolist_window import TodoListWindow

if __name__ == "__main__":
    
    configFile = ConfigurationFileService().load_config()
    print("Démarrage de l'app. Client=" + configFile.client_name)
    
    configurationEntity = ConfigurationDatabaseService().get_singleton()
    if not configurationEntity:
        print("Chargement de la configuration en base de données impossible... Fermeture de l'app.")     
        exit()
    
    print("Chargement de la configuration en base de données OK ! Démarrage de l'app !")
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
