from fastapi import APIRouter

user = APIRouter()

@user.get("/users")
def helloworld():
    """This method represent a test of fastApi"""
    return "hellow World"