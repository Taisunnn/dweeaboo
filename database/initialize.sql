
USE anime_db;

CREATE TABLE animes (

anime_id INT AUTO_INCREMENT,
title VARCHAR(255),
score FLOAT,
PRIMARY KEY(anime_id)

);


" initialize database script -> use it to create database first; defined in docker-compose file"
volume:
    - "./database/initialize.sql:/docker-entrypoint-initdb.d/1.sql"