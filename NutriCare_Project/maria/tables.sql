CREATE DATABASE IF NOT EXISTS nutricare;
USE nutricare;

CREATE TABLE IF NOT EXISTS Nutricionista(
  id INT AUTO_INCREMENT PRIMARY KEY,
  cfn VARCHAR(3) NOT NULL UNIQUE,
  nome VARCHAR(255),
  email VARCHAR(255) NOT NULL UNIQUE,
  senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Paciente(
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE, 
  senha VARCHAR(255) NOT NULL,
  cpf VARCHAR(11) NOT NULL UNIQUE,
  genero CHAR NOT NULL,
  ficha INT
  FOREIGN KEY (ficha) REFERENCES PlanoAlimentar(id),
);

CREATE TABLE IF NOT EXISTS Avaliacao(
  id INT AUTO_INCREMENT PRIMARY KEY,
  peso FLOAT, -- em kg 
  altura INT, -- em cm
  imc FLOAT,
  gordura FLOAT, -- porcentagem
  dataConsulta DATE NOT NULL -- data 
);

CREATE TABLE IF NOT EXISTS Alimentos(
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(55) NOT NULL,
  carboidratosFLOAT,
  proteina FLOAT,
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
  idPlano INT,
  idRef INT,
  FOREIGN KEY (idPlano) REFERENCES PlanoAlimentar(id),
  FOREIGN KEY (idRef) REFERENCES Refeicao(id)
);

---------------------------- Populando tabelas ------------------------------

-- Inserindo nutricionistas 
INSERT INTO Nutricionista (cfn, nome, email, senha)
VALUES (327, 'Monica Camara Gurgel', 'monicacg@yahoo.com.br', 'monica25791'),
  (483, 'Arnobio Correia de Araujo', 'arnobiocaraujo@hotmail.com', '78nakaema45'),
  (496, 'Ana Beatriz Silva', 'anabsilva@email.com', 'sbana'),
  (382, 'Carlos Barbosa dos Santos', 'carlosbbsantos@email.com', '_clos');

-- Inserindo pacientes
INSERT INTO Paciente (cpf, nome, genero, email, senha)
VALUES 
  ('32748988209', 'Gabriel Ferreira Dantas', 'm', 'gabiferreira@hotmail.com', 'moca.1459'),
  ('48351236803', 'Amanda Valentin dos Santos', 'f', 'santosamanda@gmail.com', '78nakaema45'),
  ('32546988201', 'João Carlos Dantas Silva', 'm', 'jcsilva@hotmail.com', 'flamengo2009'),
  ('48781536806', 'Carla Macedo Amorin', 'f', 'carlaamorin@hotmail.com', '548645715');

-- Inserindo avaliacao
INSERT INTO Refeicao (peso, altura, imc, gordura, dataConsulta)
VALUES 
  (70.5 , 175, 23.02 , 20.3, '2023-08-10'),
  (68.0 , 165, 24.98 , 21.0, '2024-02-16'),
  (105.0 , 180, 32.41 , 24.0, '2024-02-08'),
  (65.0 , 160, 25.39 , 18.5, '2023-07-25');

-- Inserindo Alimentos
INSERT INTO Alimentos (nome, carboidrato, proteina, calorias)
VALUES  
  ('Arroz integral', 25.0, 2.5, 120),
  ('Frango grelhado', 0.0, 30.0, 165), 
  ('Banana', 23.0, 1.0, 90);  

-- Inserindo refeicao 
INSERT INTO Refeicao (caloriasTotais, dia)
VALUES 
  (54.5, 'seg'),
  (450.0, 'qua');

-- Inserindo Plano Alimentar 
INSERT INTO PlanoAlimentar (idPaciente, idNutri)
VALUES
  (1, 1), 
  (2, 2);

-- Inserindo Refeicao_Alimento 
INSERT INTO Ref_Alim (idAlim, idRef)
VALUES
  (1, 1),
  (2, 1),
  (3, 2);

-- Inserindo Plano_Refeicao 
INSERT INTO Plano_Ref (idPlano, idRef)
VALUES
  (1, 1),
  (1, 2),
  (2, 2);
  