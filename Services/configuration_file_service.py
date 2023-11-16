import json
import re

from Models.config_file import ConfigFile

CONFIG_FILENAME = "config.json"

class ConfigurationFileService:
    def __init__(self):
        self.config_data = {}
        self.load_config()

    def load_config(self) -> ConfigFile:
            try:
                with open(CONFIG_FILENAME, 'r') as file:
                    file_content = file.read()
                    # Supprimer les commentaires
                    file_content = re.sub(r'//.*?\n|/\*.*?\*/', '', file_content, flags=re.S)
                    return ConfigFile(json.loads(file_content))
            except json.JSONDecodeError as e:
                raise ValueError(f"Erreur d'analyse JSON : {e}")