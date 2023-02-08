from fastapi import FastAPI
from models import Event

app = FastAPI()

events = []


@app.post("/events/")
async def create_event(event: Event):
    # Save event to events list
    events.append(event.dict())
    return {"message": "Event created"}


@app.get("/show-events/")
async def show_all_events():
    # Return all events stored in events list
    return {"events": events}


@app.put("/update/{event_id}")
async def update_event(event_id: int, event: Event):
    # Update event in events list with the given event_id
    events[event_id] = event.dict()
    return {"message": "Event updated"}


@app.delete("/delete/{event_id}")
async def delete_event(event_id: int):
    # Delete event from events list with the given event_id
    events.pop(event_id)
    return {"message": "Event deleted"}
