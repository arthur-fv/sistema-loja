from asyncpg import connect


async def func_get_vendas_concluidas(range=100):
    conn = None
    rows = None
   
    id = 0 # faça para gerar tabelas de visualização ao invés de uma única tabela com todos os registros...
    rows = await conn.fetch("SELECT * FROM vendas WHERE status_venda = 'CONCLUIDA' and data_venda = '2025-02-01'")
    
    return rows
