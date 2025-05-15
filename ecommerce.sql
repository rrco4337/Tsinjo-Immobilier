CREATE DATABASE Mobilier ;
USE Mobilier;



CREATE TABLE User (
    IdUser INT AUTO_INCREMENT PRIMARY KEY,
    Pseudo VARCHAR(50) NOT NULL UNIQUE,
    Motdepasse VARCHAR(255) NOT NULL  -- Stockez toujours les mots de passe hashés
);



insert into User(Pseudo,Motdepasse) values('stan','stan');
insert into User(Pseudo,Motdepasse) values('stanley','stan');
CREATE TABLE Vendre(
    IdVendre INT AUTO_INCREMENT PRIMARY KEY,
    IdUser INT NOT NULL,
    NomProduit VARCHAR(100) NOT NULL,
    Description TEXT,
    Prix DECIMAL(10, 2) NOT NULL,
    DateAjout TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (IdUser) REFERENCES User(IdUser)
)