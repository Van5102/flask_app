from sqlalchemy import Column, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, TEXT, BIGINT
db = SQLAlchemy()

class Project(db.Model):
  __tablename__ = 'projects'
  id = Column(INTEGER, primary_key = True)
  customer_name = Column(NVARCHAR(100))
  estimate_shop_time = Column(BIGINT)
  code = Column(NVARCHAR(100), nullable = False)
  deadline = Column(BIGINT)
  price_condition = Column(NVARCHAR(255))
  progress = Column(NVARCHAR(100))
  description = Column(TEXT)
  status = Column(INTEGER)
  time_start = Column(BIGINT, nullable = False)
  time_end = Column(BIGINT)

  def __init__(self, customer_name, estimate_shop_time, code, deadline, price_condition, progress, description, status, time_start, time_end):
    self.customer_name = customer_name
    self.estimate_shop_time = estimate_shop_time
    self.code = code
    self.deadline = deadline
    self.price_condition = price_condition
    self.progress = progress
    self.description = description
    self.status = status
    self.time_start = time_start
    self.time_end = time_end

class Task(db.Model):
  __tablename__ = 'tasks'
  id = Column(INTEGER, primary_key = True)
  project_id = Column(INTEGER, ForeignKey(Project.id), nullable = False)
  task_name = Column(NVARCHAR(100), nullable = False)
  unit = Column(NVARCHAR(255))
  quantity = Column(INTEGER)
  deadline = Column(BIGINT)
  estimate_unit_price = Column(BIGINT)
  time_created = Column(BIGINT, nullable = False)
  time_finished = Column(BIGINT)
  sale_description = Column(TEXT)
  other_description = Column(TEXT)
  status = Column(INTEGER)

  def __init__(self, project_id, task_name, unit, quantity, deadline, estimate_unit_price, time_created, time_finished, sale_description, other_description, status):
    self.project_id = project_id
    self.task_name = task_name
    self.unit = unit
    self.quantity = quantity
    self.deadline = deadline
    self.estimate_unit_price = estimate_unit_price
    self.time_created = time_created
    self.time_finished = time_finished
    self.sale_description = sale_description
    self.other_description = other_description
    self.status = status
