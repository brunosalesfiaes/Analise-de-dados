USE Arrecadacao;
SET NAMES utf8mb4;

LOAD DATA INFILE 'C:/Users/BRUNO/OneDrive/Documentos/Desktop/BigData/Analise de dados/dados/base_clientes_import.csv'
INTO TABLE Clientes
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nome, telefone, valor_contribuido, forma_pagamento);

SELECT * FROM Clientes LIMIT 10;