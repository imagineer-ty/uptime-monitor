import time

from .database import SessionLocal
from . import models
from .monitor import check_website


def run_monitor():
    while True:
        db = SessionLocal()

        websites = db.query(models.Website).all()

        for website in websites:
            result = check_website(website.url)

            check = models.CheckResult(
                website_id=website.id,
                status=result["status"],
                status_code=result["status_code"],
                response_time_ms=result["response_time_ms"]
            )

            db.add(check)

            print(
                f"{website.name}: {result['status']}"
            )

        db.commit()
        db.close()

        time.sleep(60)


if __name__ == "__main__":
    run_monitor()
