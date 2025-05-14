CREATE DATABASE sistema;

CREATE TABLE IF NOT EXISTS loja (
    cnpj CHAR(14) PRIMARY KEY,
    nome VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    cnpj_loja CHAR(14) NOT NULL REFERENCES loja(cnpj),
    senha VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS funcionario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    funcao VARCHAR(1) NOT NULL,
    salario REAL,
    id_gerente INTEGER REFERENCES funcionario(id) 
);

CREATE TABLE IF NOT EXISTS trabalha_em (
    id_funcionario INTEGER REFERENCES funcionario(id),
    cnpj CHAR(14) REFERENCES loja(cnpj),
    inicio DATE DEFAULT CURRENT_DATE,
    fim DATE,
    PRIMARY KEY (id_funcionario, cnpj)
);

CREATE TABLE IF NOT EXISTS venda (
    id SERIAL PRIMARY KEY,
    montante REAL NOT NULL,
    data_venda DATE NOT NULL DEFAULT CURRENT_DATE,
    horario TIME NOT NULL DEFAULT CURRENT_TIME,
    id_vendedor SERIAL REFERENCES funcionario(id)
);

CREATE MATERIALIZED VIEW faturamento_diario AS 
SELECT data_venda AS dia, SUM(montante) AS total 
from venda 
group by dia 
WITH DATA;

CREATE MATERIALIZED VIEW faturamento_mensal AS 
SELECT DATE_TRUNC('month', data_venda) AS mes, SUM(montante) AS total 
from venda 
group by mes 
WITH DATA;

CREATE MATERIALIZED VIEW faturamento_anual AS 
SELECT DATE_TRUNC('year', data_venda) AS ano, SUM(montante) AS total 
from venda 
group by ano 
WITH DATA;

ALTER TABLE funcionario ADD CONSTRAINT chk_funcao CHECK (funcao in ('G', 'C', 'V', 'E', 'S'));