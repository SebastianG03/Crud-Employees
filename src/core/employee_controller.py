from typing import List
from fastapi import APIRouter, Depends, status
from requests import Session
from database.database import Base, engine, SessionLocal
from entities.employee.employee import Employee, EmployeeUpdate
from database.tables import *
import database.datasource as ds

router = APIRouter(tags=["employees"])
        
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        
#Crud empleados
@router.get(
    "/employee/{id}", 
    status_code=status.HTTP_200_OK,
    # response_model=EmployeeModel
    )
def getEmployeeById(id: int, session: Session = Depends(get_session)):
    return ds.getEmployee(id, session)

@router.get(
    "/employees",
    status_code=status.HTTP_200_OK,
    # response_model=List[EmployeeModel]
    )
def getEmployees(session: Session = Depends(get_session)):
    return ds.getAllEmployees(session)

@router.post(
    "/employees",
    status_code=status.HTTP_201_CREATED,
    )
def createEmployee(employee: Employee, session: Session = Depends(get_session)):
    return ds.createEmployee(employee, session)

@router.put(
    "/employee/{id}",
    status_code=status.HTTP_200_OK,
    )
def updateEmployee(id: int, 
                   employee: EmployeeUpdate, 
                   session: Session = Depends(get_session)):
    return ds.updateEmployee(id, employee, session)

@router.delete(
    "/employee/{id}",
    status_code=status.HTTP_204_NO_CONTENT
    )
def deleteEmployee(id: int, session: Session = Depends(get_session)):
    return ds.deleteEmployee(id, session)


