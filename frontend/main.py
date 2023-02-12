import pandas as pd
import streamlit as st
import requests
st.set_page_config(page_title="Personal Calendar",
                   page_icon=":calendar:", layout="wide")

st.markdown(
    """
    <body style='background-color: #FAEBD7;'>
        <h1 style='color: #4169E1; text-align: center; font-size: 50px; font-weight: bold; text-shadow: 2px 2px 4px #000000;'>
        Personal Calendar
        </h1>
        <h2 style='color: #4169E2; text-align: center; font-size: 30px;'>
        Create and manage your events
        </h2>
    </body>
    """,
    unsafe_allow_html=True,
)


def show_events():
    try:
        response = requests.get("http://backend:8080/show_events/").json()
        return response
    except:
        return {"error": "Error retrieving events"}


def create_event(event):
    try:
        response = requests.post(
            "http://backend:8080/create_event/", json=event).json()
        return response
    except:
        return {"error": "Error creating event!"}


def update_event(id, event):
    try:
        response = requests.put(
            f"http://backend:8080/update_event?id={id}", json=event).json()
        return response
    except:
        return {"error": "Error updating event"}


def delete_event(id):
    try:
        response = requests.delete(
            f"http://backend:8080/delete_event?id={id}").json()
        return response
    except:
        return {"error": "Error deleting event"}


mode = st.sidebar.radio("Choose an option", ["Create Event", "Show Events"])

if mode == "Create Event":
    st.header("Create a New Event")
    title = st.text_input("Title", key='title')
    e_description = st.text_input("Description", key='e_description')
    e_start_date = st.date_input("Start Date").isoformat()
    e_end_date = st.date_input("End Date").isoformat()
    if st.button("Save Event"):
        event = {"title": title, "e_description": e_description,
                 "e_start_date": e_start_date, "e_end_date": e_end_date}
        result = create_event(event)
        st.write(result)

if mode == "Show Events":
    st.header("All Events")
    events = show_events()
    if "error" in events:
        st.write(events["error"])
    else:
        for event in events:
            st.write(event)
            # event_id = events['id']
            # if st.button(f"Update Event {event_id}"):
            #     title = st.text_input("title", event['title'])
            #     description = st.text_input(
            #         "Description", event['description'])
            #     start_date = st.date_input("Start Date", event['start_date'])
            #     end_date = st.date_input("End Date", event['end_date'])
            #     if st.button("Save Changes"):
            #         event = {"Title": title, "EventDescription": description,
            #                  "StartDate": start_date, "EndDate": end_date}
            #         result = update_event(event_id, event)
            #         st.write(result)
            #         if st.button(f"Delete Event {event_id}"):
            #             result = delete_event(event_id)
            #             st.write(result)

# if __name__ == "__main__":
#     main()
