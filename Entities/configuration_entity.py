import datetime
import uuid


class ConfigurationEntity:
    def __init__(self, id:uuid, todoBackgroundColor:str, creationUserId:uuid, creationDate:datetime, modificationUserId:uuid, modificationDate:datetime):
        self.id = id
        self.todoBackgroundColor = todoBackgroundColor
        self.creationUserId = creationUserId
        self.creationDate = creationDate
        self.modificationUserId = modificationUserId
        self.modificationDate = modificationDate