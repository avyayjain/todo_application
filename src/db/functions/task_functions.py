from datetime import datetime

from src.common.utils.constants import DB_CONNECTION_LINK
from src.db.database import TaskInformation, Users
from src.db.errors import DataInjectionError, DatabaseErrors, DatabaseConnectionError
from src.db.utils import DBConnection


def change_status(task_id: int, status: str):
    try:
        with DBConnection(DB_CONNECTION_LINK, False) as db:
            try:
                task = db.session.query(TaskInformation).filter(TaskInformation.task_id == task_id).first()
                if task:
                    if status == "complete":
                        task.complete_status = True
                        db.session.commit()
                        return task.task_id
                    elif status == "incomplete":
                        task.complete_status = False
                        db.session.commit()

                    if not task.complete_status:
                        status = "Pending"
                    else:
                        status = "Completed"

                    if task.deadline is None:
                        deadline = "No Deadline"
                    else:
                        deadline = task.deadline

                    if task.description is None:
                        description = "No Description"
                    else:
                        description = task.description

                    task = {
                        "task_id": task.task_id,
                        "task_name": task.task_name,
                        "description": description,
                        "deadline": deadline,
                        "complete_status": status
                    }
                    return task
                else:
                    return {
                        "message": "Invalid status"
                    }

            except Exception as e:
                print(e)
                raise DataInjectionError
            finally:
                db.session.close()

    except DatabaseErrors:
        raise
    except Exception as e:
        print(e)
        raise DatabaseConnectionError
