import asyncpg
from .database.instance import *


class Client():

    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool
    
    @classmethod
    async def create_pool(cls, min_sixe: int, max_sixe: int):
        pool = await asyncpg.create_pool(
            host    =HOSTNAME, 
            port    =PORT, 
            user    =USERNAME, 
            database=DATABASE, 
            password=PASSWORD, 
            min_size=min_sixe, 
            max_size=max_sixe
        )
        return cls(pool)
    
    async def close(self):
        await self.pool.close()

    async def cadastrar_loja(self, cnpj: str, nome: str):
        async with self.pool.acquire() as conn:
            await conn.execute('INSERT INTO loja(cnpj, nome) VALUES($1, $2)', 
                         cnpj, 
                         nome
            )

    async def cadastrar_funcionario(self, 
                                    nome: str, 
                                    salario: float, 
                                    funcao='', 
                                    id_gerente=None):
        async with self.pool.acquire() as conn:
            await conn.execute('INSERT INTO funcionario(nome, funcao, salario, id_gerente) VALUES($1, $2, $3, $4)',
                         nome, 
                         funcao, 
                         salario, 
                         id_gerente
            )
            
    async def cadastrar_loja_trabalho_funcionario(self, 
                                                  id_funcionario: int, 
                                                  cnpj: str, 
                                                  inicio=None):
        async with self.pool.acquire() as conn:
            await conn.execute('INSERT INTO tabalha_em(id_funcionario, cnpj, inicio, fim) VALUES($1, $2, $3, NULL)',
                         id_funcionario,
                         cnpj,
                         inicio
            )

    async def cadastrar_usuario(self, 
                                nome: str, 
                                cnpj: str, 
                                senha: str):
        async with self.pool.acquire() as conn:
            await conn.execute('INSERT INTO usuario(nome, cnpj, senha) VALUES($1, $2, $3)',
                         nome,
                         cnpj,
                         senha
            )
    
    async def cadastrar_venda(self, 
                              montante: float, 
                              id_vendedor: int):
        async with self.pool.acquire() as conn:
            await conn.execute('INSERT INTO venda(montante, id_vendedor) VALUES($1, $2)',
                         montante,
                         id_vendedor
            )

            
    async def login(self, 
                    nome: str, 
                    senha: str) -> bool:
        async with self.pool.acquire() as conn:
            resultado = await conn.fetchval('SELECT 1 FROM usuarios WHERE nome = $1 AND senha = $2', 
                             nome, 
                             senha
                    )
        return resultado != None

    async def fetch_vendas_concluidas_hoje(self) -> list[asyncpg.Record]:
        async with self.pool.acquire() as conn:
            resultado = await conn.fetch('SELECT * venda WHERE data_venda = CURRENT_DATE')
        return resultado
    
    async def fetch_nome_vendedores_ativos(self, cnpj: str):
        async with self.pool.acquire() as conn:
            records = await conn.fetch('SELECT f.nome FROM trabalha_em AS t ' \
                                       'INNER JOIN funcionarios AS f' \
                                       'ON t.id_funcionario = f.id ' \
                                       'WHERE t.cnpj = $1', 
                                      cnpj
                            )
        return records
