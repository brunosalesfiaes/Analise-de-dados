USE Arrecadacao;

CREATE TABLE IF NOT EXISTS Clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL UNIQUE,
    valor_contribuido DECIMAL(10, 2) NOT NULL,
    forma_pagamento VARCHAR(50) NOT NULL
);

