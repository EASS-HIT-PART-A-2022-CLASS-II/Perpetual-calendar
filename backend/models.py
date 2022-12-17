import calendar
from typing import List

from pydantic import BaseModel


class GetCalendarInput(BaseModel):
    year: int
    month: int
    day: int


class CalendarDay(BaseModel):
    day: int
    day_of_week: int


class GetCalendarOutput(BaseModel):
    calendar: List[CalendarDay]


def get_calendar(inputs: GetCalendarInput) -> GetCalendarOutput:
    # Validate the input dates
    if inputs.year < 1 or inputs.month < 1 or inputs.month > 12 or inputs.day < 1 or inputs.day > 31:
        return {"error": "Invalid date"}

    # Calculate the day of the week for the given date
    # TODO think about using python-dateutil later on

    day_of_week = calculate_day_of_week(inputs.year, inputs.month, inputs.day)

    # Calculate the number of days in the given month
    num_days_in_month = calculate_num_days_in_month(inputs.year, inputs.month)

    # Create the calendar for the given month
    calendar = []
    for i in range(num_days_in_month):
        calendar.append(CalendarDay(day=i+1, day_of_week=day_of_week))
        day_of_week = (day_of_week + 1) % 7

    return GetCalendarOutput(calendar=calendar)


def calculate_day_of_week(year: int, month: int, day: int) -> int:

    # Returns a value between 0 (Sunday) and 6 (Saturday).
    if month == 1 or month == 2:
        month += 12
        year -= 1

    # Calculate day of the week
    k = day
    m = month
    C = year // 100
    Y = year % 100
    day_of_week = (k + ((13*(m+1))//5) + Y + (Y//4) + (C//4) - 2*C) % 7

    # Convert day of the week to range 0 (Sunday) to 6 (Saturday)
    if day_of_week < 0:
        day_of_week += 7

    return day_of_week


def calculate_num_days_in_month(year: int, month: int) -> int:
    """Calculate the number of days in the given month."""
    return calendar.monthrange(year, month)[1]
