import datetime
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from src.models import Project  # Import your model here

DB_USER = "dev-test"
DB_PASS = "aipt2024"
DB_HOST = "192.168.3.2"
DB_NAME = "AIPT_DATA_MANAGEMENT_SYSTEM"
DB_PORT = "3306"

# Database connection setup
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
  # Change according to your database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Current date
today = datetime.date.today()

PROJECT_STATUS = {
  'PENDING': 1,
  'IN_PROGRESS': 2,
  'COMPLETED': 3,
  'CANCELED': 4,
  'EXPIRED': 5,
  'COMPLETED_OVERDUE': 6,
}

# Query to find projects with today as the deadline
projects = session.query(Project).filter(Project.deadline == today).all()

# Update the status of projects whose deadline is today
for project in projects:
    if project.status == (PROJECT_STATUS['PENDING'] or PROJECT_STATUS['IN_PROGRESS']):
        project.status = PROJECT_STATUS['EXPIRED']  # Update status as needed
        session.commit()

session.close()