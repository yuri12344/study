from typing import Protocol
from hotel.db.models import Base, to_dict
from hotel.db.engine import DBSession

DataObject = dict(str, any)

class DBInterface(Protocol):
    def __init__(self, db_class: type[Base]):
        self.db_class = db_class
        
    def read_by_id(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        return to_dict(result)
        
    def read_all(self) -> list[DataObject]:
        session = DBSession()
        result = session.query(self.db_class).all()
        return [to_dict(r) for r in result]
        
    def create(self, data: DataObject) -> DataObject:
        session = DBSession()
        result = self.db_class(**data.dict())
        session.add(result)
        session.commit()
        return to_dict(result)
        
    def update(self, id: int, data: DataObject) -> DataObject:
        session = DBSession()
        results = session.query(self.db_class).get(id)
        for key, value in data.dict(exclude_none=True).items():
            setattr(results, key, value)
        session.commit()
        return to_dict(results)
    
    def delete(self, id: int) -> DataObject:
        session = DBSession()
        results = session.query(self.db_class).get(id)
        session.commit()
        return to_dict(results)