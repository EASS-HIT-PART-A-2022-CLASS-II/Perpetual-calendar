FROM mysql:latest

# Copy the database.sql file to the container
COPY ./database_events.sql /docker-entrypoint-initdb.d/

# Set the working directory to /sql
# WORKDIR /app

# # Set the environment variables for the MySQL root user
# ENV MYSQL_ROOT_PASSWORD=root
# ENV MYSQL_DATABASE=db

# EXPOSE 3306
# # Run the database.sql file to set up the tables
# CMD ["mysql", "-u", "root", "-proot", "db", "<", "database_events.sql"]
