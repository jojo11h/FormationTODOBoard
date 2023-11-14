class ConfigFile:
    def __init__(self, config_data):
        self._config_data = config_data

    @property
    def client_name(self):
        return self._config_data.get('client_name', 'Nom par défaut')

    @client_name.setter
    def client_name(self, value):
        self._config_data['client_name'] = value
        
        
    @property
    def connection_string(self):
        return self._config_data.get('connection_string', '')

    @connection_string.setter
    def client_name(self, value):
        self._config_data['connection_string'] = value
        
        
        