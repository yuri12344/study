from typing import Protocol

DataObject = dict(str, any)

class DataInterface(Protocol):        
    def read_all(self) -> list[DataObject]:
        ...
        
    def create(self, data: DataObject) -> DataObject:
        ...
        
    def update(self, id: int, data: DataObject) -> DataObject:
        ...
    
    def delete(self, id: int) -> DataObject:
        ...