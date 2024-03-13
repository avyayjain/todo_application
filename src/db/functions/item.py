from datetime import datetime

from src.common.utils.constants import DB_CONNECTION_LINK
from src.db.database import TaskInformation
from src.db.errors import DataInjectionError, DatabaseErrors, DatabaseConnectionError
from src.db.utils import DBConnection


def add_task_detail(task_name: str, description: str, deadline: datetime, user_id: int):
    try:
        with DBConnection(DB_CONNECTION_LINK, False) as db:
            try:
                task = TaskInformation(
                    task_name=task_name,
                    description=description,
                    deadline=deadline,
                    user_id=user_id,
                    complete_status=False
                )
                db.session.add(task)
                db.session.commit()
                return task.task_id
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


def update_task_detail(task_id: int, task_name: str, description: str, deadline: datetime, status: str):
    try:
        with DBConnection(DB_CONNECTION_LINK, False) as db:
            try:
                task = db.session.query(TaskInformation).filter(TaskInformation.task_id == task_id).first()

                if task:

                    if status == "completed":
                        task.complete_status = True
                    elif status == "pending":
                        task.complete_status = False

                    task.task_name = task_name
                    task.description = description
                    task.deadline = deadline
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
                        "message": "No task found"
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


def get_task_detail(user_id: int):
    try:
        with DBConnection(DB_CONNECTION_LINK, False) as db:
            try:
                task = db.session.query(TaskInformation).filter(TaskInformation.user_id == user_id).all()
                output = []
                if task:
                    for task in task:
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

                        output.append({
                            "task_id": task.task_id,
                            "task_name": task.task_name,
                            "deadline": deadline,
                            "description": description,
                            "user_id": task.user_id,
                            "status": status
                        })
                else:
                    return {
                        "message": "No item found"
                    }

                return output
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


def get_task_detail_by_id(task_id):
    try:
        with DBConnection(DB_CONNECTION_LINK, False) as db:
            try:
                task = db.session.query(TaskInformation).filter(TaskInformation.task_id == task_id).first()

                if task:
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

                    return {
                        "task_id": task.task_id,
                        "task_name": task.task_name,
                        "deadline": deadline,
                        "description": description,
                        "user_id": task.user_id,
                        "status": status
                    }

                else:
                    return {
                        "message": "No item found"
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


def delete_task(task_id):
    try:
        with DBConnection(DB_CONNECTION_LINK, False) as db:
            try:
                task = db.session.query(TaskInformation).filter(TaskInformation.task_id == task_id).first()

                if task:
                    db.session.delete(task)
                    db.session.commit()
                    return {
                        "message": "task deleted successfully"
                    }

                else:
                    return {
                        "message": "No task found"
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
