
from sqlalchemy.orm import Session
from app.db.session import get_db
from fastapi import FastAPI, Depends, status, APIRouter
from typing import Optional

budgetrouter= router = APIRouter()

from app.db import schemas
from app.db import models
from app.core.auth import get_current_active_user, get_current_active_superuser



@router.post("/share",status_code=status.HTTP_201_CREATED)
def sharebudget(share:schemas.sharecreate, db: Session = Depends(get_db),current_user: int = Depends(get_current_active_superuser)):
    for_sharing = models.Share(**share.dict())
    email_list=[]
    for i in for_sharing.share:
        email = db.query(models.User).filter(models.User.id == i)

        email_list.append(email)
    print(email_list)
    db.add(for_sharing)
    db.commit()
    db.refresh(for_sharing)
    return for_sharing.share


@router.post("/budget",status_code=status.HTTP_201_CREATED)
def create_budget(budget:schemas.BudgetCreate,db: Session = Depends(get_db),current_user: int = Depends(get_current_active_superuser)):
    new_budget = models.Budget(budget_id=current_user.id,**budget.dict())
    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)
    db.refresh(new_budget)
    return new_budget


@router.get("/budget",status_code=status.HTTP_404_NOT_FOUND)
def get_budget(db:Session = Depends(get_db),current_user: int = Depends(get_current_active_superuser),limit:int = 10):
    # sourcery skip: use-named-expression
    budgets = db.query(models.Budget).filter(models.Budget.budget_id == current_user.id).limit(limit).all()
    return budgets

@router.get("/allbudgets",status_code=status.HTTP_404_NOT_FOUND)
def get_budget(db:Session = Depends(get_db),limit:int = 10,skip: int=0,search: Optional[str]=""):
    budgets = db.query(models.Budget).filter(models.Budget.category.contains(search)).limit(limit).offset(skip).all()
    return budgets