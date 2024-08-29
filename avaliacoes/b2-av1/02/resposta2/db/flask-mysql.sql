create database avaliacao1;
use avaliacao1;

CREATE TABLE IF NOT EXISTS users(
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS pecas(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(50) NOT NULL
);

select * from users;