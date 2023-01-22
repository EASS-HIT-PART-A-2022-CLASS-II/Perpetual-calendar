import streamlit as st
import requests
import datetime

# st.title("Event Calendar")
st.set_page_config(page_title="Personal Calendar",
                   page_icon=":calendar:", layout="wide")

st.markdown(
    """
    <h1 style='color: #4169E1; text-align: center; font-size: 50px; font-weight: bold; text-shadow: 2px 2px 4px #000000;'>
    Personal Calendar
    </h1>
    <h2 style='color: #F0F8FF; text-align: center; font-size: 30px; font-weight: bold; text-shadow: 2px 2px 4px #000000;'>
    Create and manage your events
    </h2>
    """,
    unsafe_allow_html=True,
)

# Create event
title = st.text_input("Event Title", key='title',)
description = st.text_input("Event Description", key='description')
event_start = st.date_input("Event Start Time").isoformat()
event_end = st.date_input("Event End Time").isoformat()
start_hour = st.time_input("Event Start Hour").isoformat()
end_hour = st.time_input("Event End Hour").isoformat()

event = {"title": title, "description": description,
         "event_start": event_start, "event_end": event_end, "start_hour": start_hour, "end_hour": end_hour}

# Send a POST request to the backend to create the event
r = requests.post("http://backend:8080/events/", json={"event": event})

# Handle the response
if r.status_code == 200:
    st.success("Event created successfully.")
else:
    st.error("Failed to create event.")


# Read events
if st.text_input("Show Events") == "show":
    # Send a GET request to the backend to retrieve the events
    r = requests.get("http://backend:8080/show-events/")

    events = r.json()["events"]
    st.write("Events:")
    for event in events:
        st.write(event)

if st.button("Save Event"):
    if (r.status_code == 200):
        st.success("Event saved successfully")
        event_title = st.text_input("Event Title", key='title1',)
        event_description = st.text_input(
            "Event Description", key='description1')
        event_start_date = st.date_input("Event Start Date", key='start_date')
        event_end_date = st.date_input("Event End Date", key='end_date')
        event_hour = st.time_input("Event Hour", key='hour')
        pass
    else:
        st.error("Failed to save event")
