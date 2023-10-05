from hotel.operations.customers import read_all_customers, read_customer, create_customer, update_customer, CustomerCreateData, CustomerUpdateData
from fastapi import APIRouter

router = APIRouter()

@router.get("/customers")
def api_read_all_customers():
    return read_all_customers()

@router.get("/customers/{customer}")
def api_read_customer(customer_id: int):
    return read_customer(customer_id)

@router.post("/customer")
def api_create_customer(customer: CustomerCreateData):
    return create_customer(customer)

@router.post("/customer/{customer_id}")
def api_update_customer(customer_id: int, customer: CustomerUpdateData):
    return update_customer(customer_id, customer)