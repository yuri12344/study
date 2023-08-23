from hotel.db.models import DBBooking, DBRoom, to_dict 
from hotel.db.engine import DBSession
from pydantic import BaseModel
from typing import Optional
from datetime import date

class IvalidDateError(Exception):
    pass

class BookingCreateData(BaseModel):
    room_id: int
    customer_id: int
    from_date: date
    to_date: date

class BookingUpdateData(BaseModel):
    room_id: Optional[int]
    customer_id: Optional[int]
    from_date: Optional[date]
    to_date: Optional[date]

def read_all_bookings():
    session = DBSession()
    bookings = session.query(DBBooking).all()
    return [to_dict(b) for b in bookings]

def read_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).filter(DBBooking.id == booking_id).first()
    return to_dict(booking)

def create_booking(data: BookingCreateData):
    session = DBSession()
    
    room = session.query(DBRoom).filter(DBRoom.id == data.room_id).first()
    
    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise IvalidDateError("Invalid dates")
    
    booking_dict = data.dict()
    booking_dict["price"] = room.price * days
    
    booking = DBBooking(**booking_dict)
    session.add(booking)
    session.commit()
    return to_dict(booking)

def delete_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).filter(DBBooking.id == booking_id).first()
    session.delete(booking)
    session.commit()
    return to_dict(booking)

def update_booking(booking_id: int, data: BookingUpdateData):
    session = DBSession()
    booking = session.query(DBBooking).filter(DBBooking.id == booking_id).first()
    for key, value in data.dict(exclude_none=True).items():
        setattr(booking, key, value)
    session.commit()
    return to_dict(booking)