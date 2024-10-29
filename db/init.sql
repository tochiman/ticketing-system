SET CHARACTER_SET_CLIENT = utf8;
SET CHARACTER_SET_CONNECTION = utf8;

CREATE DATABASE IF NOT EXISTS TicketingSystemDB;
USE TicketingSystemDB;

CREATE TABLE  IF NOT EXISTS user (
    id                      VARCHAR(36) PRIMARY KEY NOT NULL,
    username                TEXT NOT NULL,
    password                TEXT, 
    email                   VARCHAR(255) unique NOT NULL,
    image                   TEXT
);

CREATE TABLE  IF NOT EXISTS token (
    id                      VARCHAR(36) NOT NULL,
    token                   VARCHAR(400) UNIQUE NOT NULL,
    FOREIGN KEY uuid(id) REFERENCES user(id) on delete cascade on update cascade
);
