from fastapi import FastAPI

from models import get_calendar, GetCalendarInput

app = FastAPI()

inputs = GetCalendarInput(year=2022, month=12, day=1)
output = get_calendar(inputs)

print(output.calendar)
