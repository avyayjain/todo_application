from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from src.common.utils.user_defined_errors import UserErrors
from src.common.utils.generate_error_details import generate_details
from src.common.utils.generate_logs import logging
from src.db.functions.item import add_task_detail, get_task_detail,\
    delete_task, update_task_detail, get_task_detail_by_id
from src.resources.token import UserBase, get_current_active_user

task_router = APIRouter()


class TaskBase(BaseModel):
    task_name: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None


class UpdateTask(BaseModel):
    task_name: str
    deadline: Optional[datetime] = None
    description: Optional[str] = None
    status: Optional[str] = "pending"


@task_router.post("/add_task_details")
def add_task_details(
        data: TaskBase, current_user: UserBase = Depends(get_current_active_user)
):
    try:
        try:
            task = add_task_detail(data.task_name, data.description, data.deadline, current_user.user_id)
        except UserErrors as e:
            error_msg = (
                    "\n task  {} \n ".format(str(data.task_name)) + "\n" + e.message
            )
            logging.warning(error_msg, exc_info=True)
            with open("error.log", "a") as f:
                f.write(
                    "================================================================== \n"
                )
            details = generate_details(e.message, e.type)
            raise HTTPException(status_code=e.response_code, detail=details)
    except UserErrors as e:
        error_msg = (
                "\n task  {} \n ".format(str(data.task_name)) + "\n" + e.message
        )
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details(e.message, e.type)
        raise HTTPException(status_code=e.response_code, detail=details)

    except Exception:
        error_msg = "task" + str(data.task_name) + "\n"
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details("Internal Server Error", "InternalServerError")
        raise HTTPException(status_code=500, detail=details)
    return {"message": "task Added", "task_id": task}


@task_router.put("/update_task_details/{task_id}")
def update_task_details(
        task_id, data: UpdateTask, current_user: UserBase = Depends(get_current_active_user)
):
    try:
        try:
            task = update_task_detail(task_id, data.task_name, data.description, data.deadline, data.status)
        except UserErrors as e:
            error_msg = (
                    "\n task  {} \n ".format(str(task_id)) + "\n" + e.message
            )
            logging.warning(error_msg, exc_info=True)
            with open("error.log", "a") as f:
                f.write(
                    "================================================================== \n"
                )
            details = generate_details(e.message, e.type)
            raise HTTPException(status_code=e.response_code, detail=details)
    except UserErrors as e:
        error_msg = (
                "\n task  {} \n ".format(str(task_id)) + "\n" + e.message
        )
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details(e.message, e.type)
        raise HTTPException(status_code=e.response_code, detail=details)

    except Exception:
        error_msg = "task" + str(task_id) + "\n"
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details("Internal Server Error", "InternalServerError")
        raise HTTPException(status_code=500, detail=details)
    return {"message": "task updated successfully", "task": task}


@task_router.get("/get_task_details")
def get_task_details(current_user: UserBase = Depends(get_current_active_user)):
    try:
        task = get_task_detail(user_id=current_user.user_id)
    except Exception as e:
        error_msg = (
            f"error +  + {e.message}"
        )
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details(e.message, e.type)
        raise HTTPException(status_code=e.response_code, detail=details)

    return {
        "task on auctions :": task
    }


@task_router.get("/get_task_details/{task_id}")
def get_task_details(
        task_id, current_user: UserBase = Depends(get_current_active_user)
):
    try:
        try:
            task = get_task_detail_by_id(task_id)
        except UserErrors as e:
            error_msg = (
                    "\n task  {} \n ".format(str(task_id)) + "\n" + e.message
            )
            logging.warning(error_msg, exc_info=True)
            with open("error.log", "a") as f:
                f.write(
                    "================================================================== \n"
                )
            details = generate_details(e.message, e.type)
            raise HTTPException(status_code=e.response_code, detail=details)
    except UserErrors as e:
        error_msg = (
                "\n task  {} \n ".format(str(task_id)) + "\n" + e.message
        )
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details(e.message, e.type)
        raise HTTPException(status_code=e.response_code, detail=details)

    except Exception:
        error_msg = "task" + str(task_id) + "\n"
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details("Internal Server Error", "InternalServerError")
        raise HTTPException(status_code=500, detail=details)
    return {"message": "your searched task is", task_id: task}


@task_router.delete("/delete_task_details/{task_id}")
def delete_task_details(
        task_id, current_user: UserBase = Depends(get_current_active_user)
):
    try:
        try:
            task = delete_task(task_id)
        except UserErrors as e:
            error_msg = (
                    "\n task  {} \n ".format(str(task_id)) + "\n" + e.message
            )
            logging.warning(error_msg, exc_info=True)
            with open("error.log", "a") as f:
                f.write(
                    "================================================================== \n"
                )
            details = generate_details(e.message, e.type)
            raise HTTPException(status_code=e.response_code, detail=details)
    except UserErrors as e:
        error_msg = (
                "\n task  {} \n ".format(str(task_id)) + "\n" + e.message
        )
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details(e.message, e.type)
        raise HTTPException(status_code=e.response_code, detail=details)

    except Exception:
        error_msg = "task" + str(task_id) + "\n"
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details("Internal Server Error", "InternalServerError")
        raise HTTPException(status_code=500, detail=details)
    return {"message": "task deleted successfully"}
