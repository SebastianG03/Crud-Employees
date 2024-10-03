from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from database.database import Base, engine
import core.employee_controller as emp

from entities.employee import Employee, EmployeeUpdate

Base.metadata.create_all(bind = engine)

def create_app() -> FastAPI:
    application = FastAPI()
    application.add_middleware(GZipMiddleware)
    application.include_router(emp.router)
    return application

app = create_app()

