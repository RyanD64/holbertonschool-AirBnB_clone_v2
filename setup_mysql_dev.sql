-- prepare a mySql server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'locahlhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'locahlhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'locahlhost';