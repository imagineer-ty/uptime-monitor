from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .database import engine, SessionLocal, Base
from . import models
from .monitor import check_website


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class WebsiteCreate(BaseModel):
    name: str
    url: str


@app.get("/")
def home():
    return {"message": "Uptime Monitor API is running"}


@app.post("/websites")
def create_website(
    website: WebsiteCreate,
    db: Session = Depends(get_db)
):
    new_website = models.Website(
        name=website.name,
        url=website.url
    )

    db.add(new_website)
    db.commit()
    db.refresh(new_website)

    return new_website


@app.get("/websites")
def get_websites(db: Session = Depends(get_db)):
    websites = db.query(models.Website).all()
    return websites


@app.get("/check")
def check(url: str):
    return check_website(url)


@app.get("/results")
def get_results(db: Session = Depends(get_db)):
    results = db.query(models.CheckResult).all()
    return results
