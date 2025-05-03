CREATE IF NOT EXISTS TABLE lojas (
    cnpj CHAR(14) PRIMARY KEY,
    nome VARCHAR(80) NOT NULL
);

CREATE IF NOT EXISTS TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    funcao VARCHAR(1) NOT NULL,
    salario REAL,
    id_gerente INTEGER REFERENCES funcionarios(id) 
);

CREATE IF NOT EXISTS TABLE trabalha_em (
    id_funcionario INTEGER REFERENCES funcionarios(id),
    cnpj CHAR(14) REFERENCES lojas(cnpj),
    PRIMARY KEY (id_funcionario, cnpj)
);

CREATE IF NOT EXISTS TABLE vendas (
    id SERIAL PRIMARY KEY,
    montante REAL NOT NULL,
    data_venda DATE NOT NULL DEFAULT CURRENT_DATE,
    horario TIME NOT NULL DEFAULT CURRENT_TIME,
    id_vendedor SERIAL REFERENCES funcionarios(id)
);

CREATE OR REPLACE MATERIALIZED VIEW faturamento_diario AS 
SELECT data_venda AS dia, SUM(montante) AS total 
from vendas 
group by dia 
WITH DATA;

CREATE OR REPLACE MATERIALIZED VIEW faturamento_mensal AS 
SELECT DATE_TRUNC('month', data_venda) AS mes, SUM(montante) AS total 
from vendas 
group by mes 
WITH DATA;

CREATE OR REPLACE MATERIALIZED VIEW faturamento_anual AS 
SELECT DATE_TRUNC('year', data_venda) AS ano, SUM(montante) AS total 
from vendas 
group by ano 
WITH DATA;