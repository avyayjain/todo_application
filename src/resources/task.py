from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from src.common.utils.user_defined_errors import UserErrors
from src.common.utils.generate_error_details import generate_details
from src.common.utils.generate_logs import logging
from src.db.functions.item import add_task_detail, get_task_detail, \
    delete_task, update_task_detail, get_task_detail_by_id
from src.resources.token import UserBase, get_current_active_user

# creating a router for task
task_router = APIRouter()


# pydantic models for request and response
class TaskBase(BaseModel):
    task_name: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None


class UpdateTask(BaseModel):
    task_name: str
    deadline: Optional[datetime] = None
    description: Optional[str] = None
    status: Optional[str] = "pending"


# routes for adding task in todo list
@task_router.post("/add_task_details")
def add_task_details(
        data: TaskBase, current_user: UserBase = Depends(get_current_active_user)
):
    """
    route to add task in todo list
    :param data: task details
    task_name: name of the task
    description: description of the task
    deadline: deadline of the task
    :param current_user: data of the current user
    :return: task_id of the added task
    """
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
    return {"message": "task Added", "task": task}


# routes for updating task details
@task_router.put("/update_task_details/{task_id}")
def update_task_details(
        task_id, data: UpdateTask, current_user: UserBase = Depends(get_current_active_user)
):
    """
    route to update task details
    :param task_id: task_id of the task to be updated
    :param data: data to be updated
    task_name: name of the task
    description: description of the task
    deadline: deadline of the task
    :param current_user: data of the current user
    :return: task details after updating
    """
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


# routes for getting task details
@task_router.get("/get_task_details")
def get_task_details(current_user: UserBase = Depends(get_current_active_user)):
    """
    route to get task details
    :param current_user: data of the current user
    :return: details of the task
    """
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


# routes for getting task details by task_id
@task_router.get("/get_task_details/{task_id}")
def get_task_details(
        task_id, current_user: UserBase = Depends(get_current_active_user)
):
    """
    route to get task details by task_id
    :param task_id: task_id of the task to be searched
    :param current_user: data of the current user
    :return: details of the task
    """
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


# routes for deleting task details
@task_router.delete("/delete_task_details/{task_id}")
def delete_task_details(
        task_id, current_user: UserBase = Depends(get_current_active_user)
):
    """
    route to delete task details
    :param task_id: task_id of the task to be deleted
    :param current_user: data of the current user
    :return: message of task deleted successfully
    """
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
