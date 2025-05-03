from asyncpg import connect


async def func_get_vendedores():
    conn = None
    rows = None

    rows = await conn.fetch("SELECT nome_funcionario FROM funcionarios WHERE funcao = 'VENDEDOR'")

    await conn.close()
    rows = []
    
    nomes = [nome['nome_funcionario'] for nome in rows]
    nomes.reverse()
    return nomes
