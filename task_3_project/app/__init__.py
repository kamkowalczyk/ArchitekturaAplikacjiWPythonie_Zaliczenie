from .database import Base, engine
from .models import user, order, cart, product

Base.metadata.create_all(engine)