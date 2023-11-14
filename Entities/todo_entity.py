import datetime
import uuid


class TodoEntity:
    def __init__(self, id:uuid, label:str, isProcessed:bool, creationUserId:uuid, creationDate:datetime, modificationUserId:uuid, modificationDate:datetime):
        self.id = id
        self.label = label
        self.isProcessed = isProcessed
        self.creationUserId = creationUserId
        self.creationDate = creationDate
        self.modificationUserId = modificationUserId
        self.modificationDate = modificationDate
        
    