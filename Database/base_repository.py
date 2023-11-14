import mysql.connector

from Services.configuration_file_service import ConfigurationFileService

class BaseRepository:
    
    def __init__(self):
        config = ConfigurationFileService().load_config()
        # Chaîne de connexion
        self._connectionStringParams = self.parse_connection_string(config.connection_string)
    
    def parse_connection_string(self, conn_str):
        params = {}
        for param in conn_str.split(';'):
            key, value = param.split('=')
            params[key] = value
        return params
    
    def connect(self):
        # Connexion à la base de données
        connection = mysql.connector.connect(**self._connectionStringParams)
        return connection;
    