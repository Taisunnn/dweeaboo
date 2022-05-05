
USE anime_db;

CREATE TABLE animes (

anime_id INT AUTO_INCREMENT,
title VARCHAR(255),
score FLOAT,
synopsis VARCHAR(500),
episodes INT,
rated VARCHAR(255),
PRIMARY KEY(anime_id)

);
