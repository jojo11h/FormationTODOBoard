import tkinter as tk
from tkinter import Toplevel, colorchooser
from Services.configuration_database_service import ConfigurationDatabaseService
from Services.configuration_file_service import ConfigurationFileService

class ConfigWindow:

    def __init__(self):
        print("init configuration")
        # Charger la config
        self._configurationDatabaseService = ConfigurationDatabaseService()

    def open_configuration(self, parent) -> Toplevel :
        print("open_configuration")
        
        config_window = tk.Toplevel(parent)
        config_window.title("Configuration")
        # Permet de rendre modal
        # config_window.grab_set()
        label_color = tk.Label(config_window, text=f"Loading...")
        label_color.pack(pady=15, padx=15)

        tk.Button(
            config_window, 
            text="Configurer la couleur", 
            command=lambda: self.__configure_color(config_window, label_color)
            ).pack(pady=15, padx=15)
        
        configurationEntity = self._configurationDatabaseService.get_singleton()
        self.__refreshColor(configurationEntity, label_color)
        return config_window
   
    def __configure_color(self, window, label_color):
        color = colorchooser.askcolor(parent=window)[1]
        if color:
            configurationEntity =  self._configurationDatabaseService.get_singleton()
            configurationEntity.todoBackgroundColor = color
            self._configurationDatabaseService.update_configuration(configurationEntity)
            self.__refreshColor(configurationEntity, label_color)
            
    def __refreshColor(self, configurationEntity, label_color):
        label_color.config(text=f"Couleur actuelle : {configurationEntity.todoBackgroundColor}")
