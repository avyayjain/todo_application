from fastapi import APIRouter, Depends
from pydantic import BaseModel
from src.db.functions.add_user import create_user
from src.db.functions.logout import user_logout
from src.resources.token import UserBase, get_current_active_user

# router for sign-up and delete user
add_user_router = APIRouter()


# pydantic model for request body
class AuthAddUser(BaseModel):
    email: str
    password: str
    name: str


# pydantic model for request body
class DeleteUser(BaseModel):
    email: str


# API to ADD Users
@add_user_router.post("/")
def sign_up(
        form_data: AuthAddUser
):
    """
    API to ADD Users
    form_data: AuthAddUser
    form_data: dict
    """
    try:
        # call to function to add user
        create_user(
            user_email=form_data.email,
            password=form_data.password,
            user_name=form_data.name,
        )
        return {"detail": "User Added ,please login to continue"}
    except Exception as e:
        print(e, "error")


@add_user_router.delete("/delete_user")
def delete_user(
        form_data: DeleteUser, current_user: UserBase = Depends(get_current_active_user)
):
    """
    API to Delete Users
    form_data: AuthDeleteUser
    form_data: dict
    """
    try:
        try:
            user_logout(form_data.email)
        except Exception as e:
            print(e)
        return {"detail": "User Delete"}

    except Exception as e:
        print(e)
