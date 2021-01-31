"""
This is the main file that will run the API using uvicorn
"""
import uvicorn
from fastapi import FastAPI

from app.config import config
from app.routers import test_route


# Creating app obj
app = FastAPI()

# Adding routes
app.include_router(test_route.router, prefix="/test")

# Running app using uvicorn
if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=config.host,
        port=config.port,
        reload=config.reload
    )
