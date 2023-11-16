import uuid
from Database.base_repository import BaseRepository
from Entities.todo_entity import TodoEntity


class TodoRepository(BaseRepository):
    def get_by_id(self, id:uuid) -> TodoEntity:
         # Création d'un cursor et exécution d'une requête
         connection = self.connect()
         try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM todos WHERE ID = %s "
            parameters = (id,)
            cursor.execute(query, parameters)
            results = cursor.fetchall()
            todos = []
            for row in results:
               todoEntity = self.create_entity_from_row(row)
               todos.append(todoEntity)
            # Fermeture du cursor et de la connexion
            cursor.close()
            
            # take first element or None if not exists
            return next((todoEntity for todoEntity in todos), None)
            
         finally:
            connection.close()
    
    def get_all(self) -> TodoEntity:
         # Création d'un cursor et exécution d'une requête
         connection = self.connect()
         try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM todos")
            results = cursor.fetchall()
            todos = []
            for row in results:
               todoEntity = self.create_entity_from_row(row)
               todos.append(todoEntity)
            # Fermeture du cursor et de la connexion
            cursor.close()
            
            return todos
            
         finally:
            connection.close()
            
    def create_entity_from_row(self, row) -> TodoEntity:
       return TodoEntity(
          row["Id"], 
          row["Label"], 
          row["IsProcessed"], 
          row["CreationUserId"], 
          row["CreationDate"], 
          row["ModificationUserId"], 
          row["ModificationDate"]
          )
    
    def update(self, todoEntity:TodoEntity)-> bool:
         # Création d'un cursor et exécution d'une requête
         connection = self.connect()
         try:
            cursor = connection.cursor()
            query = """update todos 
                           set 
                           Id=%s, 
                           Label=%s, 
                           IsProcessed=%s, 
                           CreationUserId=%s,
                           CreationDate=%s,
                           ModificationUserId=%s,
                           ModificationDate=%s
                           where Id=%s"""
            parameters = (todoEntity.id, 
                          todoEntity.label, 
                          todoEntity.isProcessed, 
                          todoEntity.creationUserId,
                          todoEntity.creationDate,
                          todoEntity.modificationUserId,
                          todoEntity.modificationDate,
                          todoEntity.id)
            
            cursor.execute(query, parameters)
            connection.commit()

            # Fermeture du cursor
            cursor.close()
            
            print(f"Updated todo count : {cursor.rowcount}")
            return cursor.rowcount > 0
            
         finally:
            #fermeture de la connexion
            connection.close()
    
    def insert(self, todoEntity:TodoEntity)-> bool:
         # Création d'un cursor et exécution d'une requête
         connection = self.connect()
         try:
            cursor = connection.cursor()
            query = """insert into todos 
                        (
                           Id, 
                           Label, 
                           IsProcessed, 
                           CreationUserId,
                           CreationDate,
                           ModificationUserId,
                           ModificationDate
                        )
                        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            parameters = (str(todoEntity.id), 
                          todoEntity.label, 
                          todoEntity.isProcessed, 
                          todoEntity.creationUserId,
                          todoEntity.creationDate,
                          todoEntity.modificationUserId,
                          todoEntity.modificationDate)
            
            cursor.execute(query, parameters)
            connection.commit()

            # Fermeture du cursor
            cursor.close()
            
            print(f"inserted todo count : {cursor.rowcount}")
            return cursor.rowcount > 0
            
         finally:
            #fermeture de la connexion
            connection.close()
            
    def delete_by_id(self, id:uuid) -> bool:
         # Création d'un cursor et exécution d'une requête
         connection = self.connect()
         try:
            cursor = connection.cursor()
            query = "DELETE FROM todos WHERE ID = %s "
            parameters = (id,)
            cursor.execute(query, parameters)
            cursor.close()
            print(f"Deleted todo count : {cursor.rowcount}")
            connection.commit()
            
            return cursor.rowcount>0
            
         finally:
            connection.close()