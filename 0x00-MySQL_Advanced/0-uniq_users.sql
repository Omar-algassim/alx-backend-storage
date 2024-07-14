--create table uniq_users
--create user table with id email and name

CREATE TABLE if NOT EXISTS users(
    id INT NOTNULL INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
)
