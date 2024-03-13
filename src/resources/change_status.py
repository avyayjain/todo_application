import logging

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from src.common.utils.generate_error_details import generate_details
from src.common.utils.user_defined_errors import UserErrors
from src.db.functions.task_functions import change_status
from src.resources.token import UserBase, get_current_active_user

change_stat = APIRouter()


class Status(BaseModel):
    stat: str


@change_stat.put("/status_change/{task_id}")
def status_change(task_id,data: Status, current_user: UserBase = Depends(get_current_active_user)):
    try:
        try:
            task = change_status(task_id, status=data.stat)
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
    return {"message": "Task status updated successfully ", "task details": task}

