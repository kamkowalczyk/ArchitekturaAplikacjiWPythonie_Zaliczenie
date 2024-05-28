from pydantic import BaseModel, ConfigDict

class OrderBase(BaseModel):
    status: str

class OrderCreate(OrderBase):
    user_id: int

class OrderRead(OrderBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)