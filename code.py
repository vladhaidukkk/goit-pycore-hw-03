import random
import re
from datetime import datetime, timedelta
from typing import TypedDict


# Task 1:
def get_days_from_today(date: str) -> int:
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    dates_diff = datetime.now().date() - date_obj
    return dates_diff.days


# Task 2:
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1 or max > 1000 or min > max or max + 1 - min < quantity:
        return []
    return sorted(random.sample(range(min, max + 1), k=quantity))


# Task 3:
def normalize_phone(phone_number: str) -> str:
    plain_number = re.sub(r"\D", "", phone_number)
    number_without_code = plain_number[-10:]
    return f"+38{number_without_code}"


# Task 4:
class User(TypedDict):
    name: str
    birthday: str


class UpcomingBirthday(TypedDict):
    name: str
    congratulation_date: str


def get_upcoming_birthdays(users: list[User]) -> list[UpcomingBirthday]:
    current_date = datetime.now().date()
    upcoming_birthdays: list[UpcomingBirthday] = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        current_year_birthday = datetime(
            year=current_date.year,
            month=birthday.month,
            day=birthday.day,
        ).date()

        if current_year_birthday >= current_date:
            next_birthday = current_year_birthday
        else:
            next_birthday = datetime(
                year=current_date.year + 1,
                month=birthday.month,
                day=birthday.day,
            ).date()

        dates_diff = next_birthday - current_date
        if dates_diff.days > 7:
            continue

        congratulation_date = next_birthday
        if congratulation_date.isoweekday() == 6:  # Saturday -> Monday
            congratulation_date += timedelta(days=2)
        elif congratulation_date.isoweekday() == 7:  # Sunday -> Monday
            congratulation_date += timedelta(days=1)

        upcoming_birthdays.append(
            {
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            }
        )

    return upcoming_birthdays
