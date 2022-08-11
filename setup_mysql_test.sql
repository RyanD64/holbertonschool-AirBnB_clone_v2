-- prepare a mySql server for the tests of the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'locahlhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'locahlhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'locahlhost';