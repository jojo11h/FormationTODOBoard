from Database.base_repository import BaseRepository
from Entities.user_entity import UserEntity


class UserRepository(BaseRepository):
     def get_users(self) -> list[UserEntity]:
         # Création d'un cursor et exécution d'une requête
         connection = self.connect()
         try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users")
            results = cursor.fetchall()

            users = []
            for row in results:
                users.append(UserEntity(
                    row["Id"], 
                    row["FirstName"], 
                    row["LastName"], 
                    row["Email"]
                    ))

            # Fermeture du cursor et de la connexion
            cursor.close()
            
         finally:
            connection.close()