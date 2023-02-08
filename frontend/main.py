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

# Create a function to create an event
def create_event(event):
    r = requests.post("http://backend:8080/events/", json=event)
    return r.json()

# Create a function to show all events
def show_all_events():
    r = requests.get("http://backend:8080/show-events/")
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
            event = {"title": title, "description": description, "start_time": start_time, "end_time": end_time}
            result = create_event(event)
            st.success(result["message"])
    else:
        st.title("Show Events")
        events = show_all_events()
        st.write("All events:")
        st.write(events)

if __name__ == "__main__":
    main()