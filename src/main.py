from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import models
from database.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

from entities.employee import Employee, EmployeeUpdate


Base.metadata.create_all(engine)

app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/employees", response_model=List[Employee])
def read_task_list(session: Session = Depends(get_session)):
    task_list = session.query(models.EmployeeModel).all()  # Get all tasks

    return task_list

@app.get("/employee/{id}", response_model=Employee)
def read_task(id: str, session: Session = Depends(get_session)):
    task = session.query(models.EmployeeModel).get(id)  # Get item with given id

    if not task:
        raise HTTPException(status_code=404, detail=f"Employee with id {id} not found")

    return task


@app.post("/employee", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_task(employee: Employee, session: Session = Depends(get_session)):
    employee_data = employee.model_dump()
    
    # contact_info_data = employee_data.pop('contact_info')
    # soft_skills_data = employee_data.pop('soft_skills')
    # hard_skills_data = employee_data.pop('hard_skills')
    
    employee_db = models.EmployeeModel(**employee_data)
    # contact_info_db = models.ContactInfoModel(**contact_info_data)
    # employee_db.contact_info = contact_info_db

    session.add(employee_db)
    session.commit()
    session.refresh(employee_db)

    return employee_data


@app.put("/employee/{id}", response_model=Employee)
def update_task(id: int, employee: EmployeeUpdate, session: Session = Depends(get_session)):
    employee_db = session.query(models.EmployeeModel).get(id)  # Get given id

    if employee_db:
        employee_data = employee.model_dump()

        # contact_info_data = employee_data.pop('contact_info')
        # soft_skills_data = employee_data.pop('soft_skills')
        # hard_skills_data = employee_data.pop('hard_skills')

        # employee_db = models.EmployeeModel(**employee_data)
        for key, value in employee_data.items():
            setattr(employee_db, key, value)
        # contact_info_db = models.ContactInfoModel(**contact_info_data)
        # employee_db.contact_info = contact_info_db

        # employee_db = employee_data
        session.commit()
        session.refresh(employee_db)

    if not employee_db:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    return employee_db

@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, session: Session = Depends(get_session)):

    employee_db = session.query(models.EmployeeModel).get(id)

    if employee_db:
        session.delete(employee_db)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    return None

