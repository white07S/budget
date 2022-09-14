from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP,ForeignKey
from sqlalchemy.ext.mutable import MutableList
from .session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)



class Share(Base):
    __tablename__ = "shared"
    id = Column(Integer,primary_key=True,nullable=False)
    share = Column(MutableList.as_mutable(ARRAY(String)))
    name = Column(String,nullable=False)


class Budget(Base):
    __tablename__ = "budget"
    id = Column(Integer,primary_key=True,nullable=False)
    amount = Column(Integer,nullable=False)
    # category either its income or expense
    category = Column(String,nullable=False)
    # like milk,bread etc
    on_what = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    budget_id = Column(Integer,ForeignKey("user.id", ondelete="CASCADE"),nullable=False)
