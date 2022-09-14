from pydantic import BaseModel
import typing as t
from typing import Optional, List



class UserBase(BaseModel):
    email: str
    is_active: bool = True
    is_superuser: bool = False
    first_name: str = None
    last_name: str = None


class UserOut(UserBase):
    pass


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserEdit(UserBase):
    password: t.Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    permissions: str = "user"


class sharecreate(BaseModel):
    share: List

class sharedout(BaseModel):
    id:int
    share: str


    class Config:
        orm_mode = True


class BudgetCreate(BaseModel):
    amount:int
    category: str
    on_what: str
    

class BudgetOut(BaseModel):
    id: int
    budget_id: int
    amount:int
    category:str
    on_what: str
    

    class Config:
        orm_mode = True

