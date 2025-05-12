import asyncpg
from database.instance import *

from asyncio import sleep

class Client():

    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool
    
    @classmethod
    async def create_pool(cls):
        pool = await asyncpg.create_pool(
            host    =HOSTNAME, 
            port    =PORT, 
            user    =USERNAME, 
            database=DATABASE,
            password=PASSWORD, 
            min_size=1, 
            max_size=10
        )
        return cls(pool)
    
    async def close(self):
        await self.pool.close()

    async def cadastrar_loja(self, cnpj, nome):
        async with self.pool.acquire() as conn:
            conn.execute('INSERT INTO loja(cnpj, nome) VALUES($1, $2)', 
                         cnpj, 
                         nome
            )

    async def cadastrar_funcionario(self, nome, salario, funcao='', id_gerente=''):
        async with self.pool.acquire() as conn:
            conn.execute('INSERT INTO funcionario(nome, funcao, salario, id_genrente) VALUES($1, $2, $3, $4)',
                         nome, 
                         funcao, 
                         salario, 
                         id_gerente
            )
            
    async def cadastrar_loja_trabalho_funcionario(self, id_funcionario, cnpj, inicio=None):
        async with self.pool.acquire() as conn:
            conn.execute('INSERT INTO tabalha_em(id_funcionario, cnpj, inicio, fim) VALUES($1, $2, $3, NULL)',
                         id_funcionario,
                         cnpj,
                         inicio
            )

    async def cadastrar_usuario(self, nome, cnpj, senha):
        async with self.pool.acquire() as conn:
            await conn.execute('INSERT INTO usuario(nome, cnpj, senha) VALUES($1, $2, $3)',
                         nome,
                         cnpj,
                         senha
            )
    
    async def cadastrar_venda(self, montante, id_vendedor):
        async with self.pool.acquire() as conn:
            conn.execute('INSERT INTO venda(montante, id_vendedor) VALUES($1, $2)',
                         montante,
                         id_vendedor
            )
            
    async def login(self, nome, senha):
        async with self.pool.acquire() as conn:
            await conn.fetch('SELECT 1 FROM usuarios WHERE nome = $1 AND senha = $2', 
                             nome, 
                             senha
                    )

    def fetch_vendas_concluidas():
        pass
    
    async def fetch_vendedores_ativos(self, cnpj: str):
        async with self.pool.acquire() as conn:
            linhas = await conn.fetch('SELECT * FROM trabalha_em WHERE cnpj = $1 AND fim IS NULL', 
                                      cnpj
                            )
