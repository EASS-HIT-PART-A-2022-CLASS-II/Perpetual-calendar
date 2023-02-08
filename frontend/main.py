import pandas as pd
import streamlit as st
import requests
import datetime
st.set_page_config(page_title="Personal Calendar",
                   page_icon=":calendar:", layout="wide")

st.markdown(
    """
    <body style='background-color: #FAEBD7;'>
        <h1 style='color: #4169E1; text-align: center; font-size: 50px; font-weight: bold; text-shadow: 2px 2px 4px #000000;'>
        Personal Calendar
        </h1>
        <h2 style='color: #4169E2; text-align: center; font-size: 30px; text-shadow: 2px 2px 4px #000000;'>
        Create and manage your events
        </h2>
    </body>
    """,
    unsafe_allow_html=True,
)


def create_event(event):
    r = requests.post("http://backend:8080/events/", json=event)
    return r.json()


def show_all_events():
    r = requests.get("http://backend:8080/show-events/")
    return r.json()


def update_event(event_id, event):
    r = requests.put(f"http://backend:8080/update/{event_id}", json=event)
    return r.json()


def delete_event(event_id):
    r = requests.delete(f"http://backend:8080/delete/{event_id}")
    return r.json()


def main():
    st.sidebar.title("Personal Calendar")
    page = st.sidebar.selectbox("Select a page", ["Add Event", "Show Events"])

    if page == "Add Event":
        st.title("Add Event")
        title = st.text_input("Title", key='title')
        description = st.text_input("Description", key='description')
        start_time = st.date_input("Event Start Time").isoformat()
        end_time = st.date_input("Event End Time").isoformat()
        if st.button("Save Event"):
            event = {"title": title, "description": description,
                     "start_time": start_time, "end_time": end_time}
            result = create_event(event)
            st.success(result["message"])
    else:
        st.title("Show Events")
        events = show_all_events()
        events_data = events.get("events", [])
        if events_data:
            st.write("All events:")
            events_df = pd.DataFrame(events_data)
            st.write(
                events_df[['title', 'description', 'start_time', 'end_time']])
        else:
            st.write("No events found.")


if __name__ == "__main__":
    main()
