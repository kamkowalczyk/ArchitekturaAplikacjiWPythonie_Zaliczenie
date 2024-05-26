from pydantic import BaseModel

class OrderBase(BaseModel):
    status: str

class OrderCreate(OrderBase):
    user_id: int

class Order(OrderBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
