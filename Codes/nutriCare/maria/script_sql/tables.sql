CREATE DATABASE IF NOT EXISTS nutricare;
USE nutricare;

CREATE TABLE IF NOT EXISTS Nutricionista(
    id INT AUTO_INCREMENT PRIMARY KEY,
    cfn VARCHAR(3) NOT NULL UNIQUE,
    nome VARCHAR(255),
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Avaliacao(
    id INT AUTO_INCREMENT PRIMARY KEY,
    peso FLOAT, -- em kg 
    altura INT, -- em cm
    imc FLOAT,
    gordura FLOAT, -- porcentagem
    dataConsulta DATE NOT NULL -- data 
);

CREATE TABLE IF NOT EXISTS Paciente(
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(11) NOT NULL UNIQUE, 
    nome VARCHAR(255) NOT NULL,
    genero CHAR NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE, 
    senha VARCHAR(255) NOT NULL, 
    ficha INT,
    FOREIGN KEY (ficha) REFERENCES Avaliacao(id)  
);

CREATE TABLE IF NOT EXISTS Alimento(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(55) NOT NULL,
    tipo VARCHAR(15) NOT NULL,
    calorias FLOAT
);

CREATE TABLE IF NOT EXISTS Refeicao(
    id INT AUTO_INCREMENT PRIMARY KEY,
    caloriasTotais FLOAT,
    dia VARCHAR(10) -- dia da semana (seg - dom)
);

CREATE TABLE IF NOT EXISTS PlanoAlimentar(
    id INT AUTO_INCREMENT PRIMARY KEY,
    idPaciente INT,
    idNutri INT,
    FOREIGN KEY (idPaciente) REFERENCES Paciente(id),
    FOREIGN KEY (idNutri) REFERENCES Nutricionista(id)
);

CREATE TABLE IF NOT EXISTS Ref_Alim(
    idAlim INT,
    idRef INT,
    FOREIGN KEY (idAlim) REFERENCES Alimento(id),
    FOREIGN KEY (idRef) REFERENCES Refeicao(id)
);

CREATE TABLE IF NOT EXISTS Plano_Ref(
    idPlano INT ,
    idRef INT,
    FOREIGN KEY (idPlano) REFERENCES PlanoAlimentar(id),
    FOREIGN KEY (idRef) REFERENCES Refeicao(id)
);