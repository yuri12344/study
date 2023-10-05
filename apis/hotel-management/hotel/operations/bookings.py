from hotel.db.models import DBBooking, DBRoom, to_dict 
from hotel.db.engine import DBSession
from pydantic import BaseModel
from interface import DataInterface, DataObject
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

def read_all_bookings(bookind_interface: DataInterface) -> list[DataObject]:
    return bookind_interface.read_all()

def read_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.read_by_id(booking_id)

def create_booking(data: BookingCreateData, booking_interface: DataInterface, room_interface: DataInterface) -> DataObject:
    room = room_interface.read_by_id(data.room_id)
    days = (data.to_date - data.from_date).days

    if days <= 0:
        raise IvalidDateError("Invalid dates")

    booking_dict = data.dict()
    booking_dict["price"] = room["price"] * days
    return booking_interface.create(booking_dict)

def delete_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.delete(booking_id)

