from fastapi import FastAPI
from models import Event

app = FastAPI()

make_event = Event(title="Make FastAPI", description="Make a FastAPI app",
                   start_time="2021-12-01 09:00", end_time="2021-12-01 10:00")

events_list = []


@app.post("/events/")
def create_event(event: Event):
    events_list.append(event)
    return {"event": event}


@app.get("/show-events/")
def read_events():
    return {"events": events_list}


@app.put("/update/{event_id}")
def update_event(event_id: int, event: Event):
    return {"event_id": event_id, "event": event}


@app.delete("/delete/{event_id}")
def delete_event(event_id: int):
    return {"event_id": event_id}
