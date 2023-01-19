import streamlit as st
import requests

st.title("Event Calendar")

# Create event
title = st.text_input("Event Title")
description = st.text_input("Event Description")
start_time = st.date_input("Event Start Time").isoformat()
end_time = st.date_input("Event End Time").isoformat()

event = {"title": title, "description": description,
         "start_time": start_time, "end_time": end_time}

# Send a POST request to the backend to create the event
r = requests.post("http://localhost:8080/events/", json={"event": event})

# Handle the response
if r.status_code == 201:
    st.success("Event created successfully.")
else:
    st.error("Failed to create event.")


# Read events
if st.text_input("Show Events") == "show":
    # Send a GET request to the backend to retrieve the events
    r = requests.get("http://localhost:8080/show-events/")

    events = r.json()["events"]
    st.write("Events:")
    for event in events:
        st.write(event)
