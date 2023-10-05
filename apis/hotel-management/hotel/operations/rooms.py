from hotel.db.engine import DBSession
from hotel.db.models import DBRoom, to_dict

def read_all_rooms():
    session = DBSession()
    rooms = session.query(DBRoom).all()
    return [to_dict(r) for r in rooms]

def read_room(room_id: int):
    session = DBSession()
    room = session.query(DBRoom).filter(DBRoom.id == room_id).first()
    return to_dict(room)