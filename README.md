# Personal-calendar - Make events you Don't forget!

* The Personal calendar is a event saving.
* The purpose of the application is to give the user the option to save events and display them.
* The app includes two containers:
1. Backend: written with python using pydentic and Fast API. the port that the backend runs with is: 8080.

![image](https://user-images.githubusercontent.com/58915223/217578761-b2e2e545-03c3-40aa-9290-0af182d7f0ec.png)

2. Frontend: written with Python using Streamlit (a UI library). the port that the frontend runs with is: 8501.
![image](https://user-images.githubusercontent.com/58915223/218325610-dd54befc-ce85-40d7-8fc3-3584bde29cef.png)

3. DataBase - I use MySQL for the Database, the DB in runnig on port 3306

4. Visual Diagram:

![image](https://user-images.githubusercontent.com/58915223/218325547-b0471aa7-ef93-4944-94e2-451e10ca0eb4.png)

5. The app runnig by Docker-compose:
version: '3'
services:
  backend:
    container_name: backend
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports: 
      - "8080:8080"
    depends_on:
      - mysql

  frontend:
    container_name: frontend
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports: 
      - "8501:8501"
    depends_on:
      - backend

  mysql:
    container_name: mysql
    build:
      context: ./mysql/
      dockerfile: Dockerfile
    restart: always
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: db
