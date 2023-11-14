
from Database.configuration_repository import ConfigurationRepository
from Entities.configuration_entity import ConfigurationEntity


class ConfigurationDatabaseService:
    def get_singleton(self) -> ConfigurationEntity:
        return ConfigurationRepository().get_singleton()
            
            
    def update_configuration(self, configurationEntity:ConfigurationEntity):
        return ConfigurationRepository().update(configurationEntity)