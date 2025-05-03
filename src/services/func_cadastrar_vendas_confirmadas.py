from asyncpg import connect


async def func_cadastrar_vendas_confirmadas(v: list):
    conn = None
    mensagem = 'cadastrada' # remover depois
    await conn.executemany(
            "INSERT INTO vendas (nome_vendedor, valor_venda, metodo_pagamento, status_venda) values($1, $2, $3, 'CONCLUIDA')",
            v
    )

    await conn.close()
    
    return mensagem
