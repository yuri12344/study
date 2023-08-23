from hotel.operations.bookings import (
    read_all_bookings,
    read_booking,
    create_booking,
    update_booking,
    delete_booking,
    BookingCreateData,
    BookingUpdateData   
)
from fastapi import APIRouter

router = APIRouter()

@router.get("/bookings")
def api_read_all_bookings():
    return read_all_bookings()

@router.get("/bookings/{booking}")
def api_read_booking(booking_id: int):
    return read_booking(booking_id)

@router.post("/booking")
def api_create_booking(booking: BookingCreateData):
    return create_booking(booking)

@router.post("/booking/{booking_id}")
def api_update_booking(booking_id: int, booking: BookingUpdateData):
    return update_booking(booking_id, booking)

@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int):
    return delete_booking(booking_id)