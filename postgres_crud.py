import uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Optional, List
from pydantic import BaseModel
from typing import Optional

from sqlalchemy import Boolean, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base


from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

engine = create_engine('postgresql://{username}:{password}@{host}:{port}/{db_name}'.format(username='postgres', password='root', host='localhost', port='5432', db_name='test'))
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
Base.metadata.create_all(bind=engine)

class Memo(Base):
    __tablename__='memos'
    id = Column(String(120), primary_key=True, default=lambda:str(uuid.uuid4()))
    title = Column(String(80), default='No title', nullable=False, index=True)
    content = Column(Text, nullable=True)
    is_favorite = Column(Boolean, nullable = False, default = False)



class RequestMemo(BaseModel):
    title:str
    content:Optional[str] = None
    is_favorite: Optional[bool] = False

class ResponseMemo(BaseModel):
    id:str
    title:str
    content:Optional[str] = None
    is_favorite:bool
    class config:
        orm_mode=True

app = FastAPI()

@app.post('/memos',response_model=ResponseMemo)
async def register_memo(req: RequestMemo, db: Session = Depends(get_db)):
    memo = Memo(**req.dict())
    db.add(memo)
    db.commit()
    return memo

@app.put('/memos/{item_id}', response_model=ResponseMemo)
async def mod_memo(item_id:str, req:RequestMemo, db: Session = Depends(get_db)):
    memo = db.query(Memo).filter_by(id=item_id)
    req_dict = req.dict()
    req_dict['id'] = item_id
    req = {k: v for k, v in req_dict.items()}
    for key, value in req.items():
        setattr(memo, key, value)
    
    db.commit()
    return memo

@app.delete('/memos/{item_id}')
async def del_memo(item_id: str, db: Session = Depends(get_db)):
    memo = db.query(Memo).filter_by(id=item_id).first()
    db.delete(memo)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.get('/memos',response_model=List[ResponseMemo])
async def get_memos(db: Session = Depends(get_db)):
    memos = db.query(Memo).all()
    print(memos)
    return memos

@app.get("/")
def root():
    return {"Hello":"World"}

@app.get("/user/{userno}")
def root():
    return {"Hello":"World"}
