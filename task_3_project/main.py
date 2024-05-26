from fastapi import FastAPI
from app.views import user_view, order_view

app = FastAPI()

app.include_router(user_view.router, prefix="/api/v1")
app.include_router(order_view.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
