from asyncpg import connect


async def func_login_usuario(usuario, senha):
    conn = None
    linhas = []
    linhas = await conn.fetch(f"SELECT 1 FROM usuarios WHERE nome = '{usuario}' and senha = '{senha}'")
    await conn.close()
    return bool(linhas)  # caso o não exista uma linha, o linhas de fetchall é []
