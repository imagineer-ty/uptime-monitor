from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

from .database import Base


class Website(Base):
    __tablename__ = "websites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    url = Column(String)


class CheckResult(Base):
    __tablename__ = "check_results"

    id = Column(Integer, primary_key=True, index=True)
    website_id = Column(Integer, ForeignKey("websites.id"))
    status = Column(String)
    status_code = Column(Integer, nullable=True)
    response_time_ms = Column(Integer, nullable=True)
    checked_at = Column(DateTime, default=datetime.utcnow)
