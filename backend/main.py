from fastapi import FastAPI
from models import Event
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="mysql", port='3306', password="root", user="root", database="db")
    print("DB connected")

except:
    print("DB connection failed")

app = FastAPI()


@app.post("/create_event/")
async def create_event(event: Event):
    cursor = connection.cursor()

    query = "INSERT INTO events (title, e_description, e_start_date, e_end_date) VALUES (%s, %s, %s, %s)"
    values = (event.title, event.e_description,
              event.e_start_date, event.e_end_date)
    cursor.execute(query, values)
    connection.commit()
    try:
        return {"message": "Event created successfully!!!"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        connection.close()
    # try:
    #     cursor = connection.cursor()
    #     sql = "INSERT INTO events (Title, EventDescription, StartDate, EndDate) VALUES (%s, %s, %s, %s)"
    #     cursor.execute(sql, (event.title, event.description,
    #                    event.start_time, event.end_time))
    #     connection.commit()
    #     return {"message": "Event created successfully."}
    # except Exception as e:
    #     return {"error": str(e)}


@app.get("/show_events/")
async def show_events():
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM events"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return {"error": str(e)}


@app.put("/update_event/")
async def update_event(id: int, event: Event):
    try:
        cursor = connection.cursor()
        sql = "UPDATE events SET title=%s, e_description=%s, e_start_date=%s, e_end_date=%s WHERE id=%s"
        cursor.execute(sql, (event.title, event.e_description,
                       event.e_start_date, event.e_end_date, id))
        connection.commit()
        return {"message": "Event updated successfully."}
    except Exception as e:
        return {"error": str(e)}


@app.delete("/delete_event/")
async def delete_event(id: int):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM events WHERE id=%s"
        cursor.execute(sql, (id,))
        connection.commit()
        return {"message": "Event deleted successfully."}
    except Exception as e:
        return {"error": str(e)}
