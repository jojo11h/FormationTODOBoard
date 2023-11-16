import uuid
from Database.todo_repository import TodoRepository
from Entities.todo_entity import TodoEntity


class TodoService:
    
    def get_by_id(self, id:uuid) -> TodoEntity:
        return TodoRepository().get_by_id(id)
    
    def get_all(self) -> list[TodoEntity]:
        return TodoRepository().get_all()
            
    def update(self, todoEntity:TodoEntity)-> bool:
        return TodoRepository().update(todoEntity)
    
    def insert(self, todoEntity:TodoEntity)-> bool:
        return TodoRepository().insert(todoEntity)
    
    def delete_by_id(self, id:uuid) -> bool:
        return TodoRepository().delete_by_id(id)