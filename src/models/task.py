from  sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String,nullable=False)
    due_date = Column(DateTime,nullable=False)
    priority = Column(Integer,nullable=False)

    def __repr__(self):
        return f'<Task(id={self.id}, description={self.description}, due_date={self.due_date}, priority={self.priority})>'