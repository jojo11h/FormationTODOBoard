from Database.base_repository import BaseRepository
from Entities.configuration_entity import ConfigurationEntity


class ConfigurationRepository(BaseRepository):
    def get_singleton(self) -> ConfigurationEntity:
         # Création d'un cursor et exécution d'une requête
         connection = self.connect()
         try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM configurations")
            results = cursor.fetchall()

            configurations = []
            for row in results:
               configurations.append(
                  ConfigurationEntity(
                     row["Id"],
                     row["TodoBackgroundColor"],
                     row["CreationUserId"],
                     row["CreationDate"],
                     row["ModificationUserId"],
                     row["ModificationDate"]
                     )
               )
            # Fermeture du cursor et de la connexion
            cursor.close()
            
            # take first element or None if not exists
            return next((configurationEntity for configurationEntity in configurations), None)
            
         finally:
            connection.close()
            
            
    def update(self, configurationEntity:ConfigurationEntity) -> bool:
         # Création d'un cursor et exécution d'une requête
         connection = self.connect()
         try:
            cursor = connection.cursor()
            query = """update configurations 
                           set 
                           Id=%s, 
                           TodoBackgroundColor=%s, 
                           CreationUserId=%s,
                           CreationDate=%s,
                           ModificationUserId=%s,
                           ModificationDate=%s
                           where Id=%s""";
            parameters = (configurationEntity.id, 
                          configurationEntity.todoBackgroundColor, 
                          configurationEntity.creationUserId,
                          configurationEntity.creationDate,
                          configurationEntity.modificationUserId,
                          configurationEntity.modificationDate,
                          configurationEntity.id)
            
            cursor.execute(query, parameters)
            connection.commit()

            # Fermeture du cursor
            cursor.close()
            
            print(f"Updated todo count : {cursor.rowcount}")
            return cursor.rowcount > 0
            
         finally:
            #fermeture de la connexion
            connection.close()
    
