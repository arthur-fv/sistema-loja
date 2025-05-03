from asyncpg import connect


async def fetch_in_range(id:int = 0, limit:int=30):
    rows, conn = None, None
    # uma lista com 1 record da coluna id, se existir um para a data o bloco é executado
    record_id = await conn.fetch(f"SELECT id FROM vendas WHERE data_venda = CURRENT_DATE LIMIT 1")
    if record_id:
        id = record_id[0]['id'] if id == 0 else id
        rows = await conn.fetch(f"SELECT * FROM vendas WHERE data_venda = CURRENT_DATE AND id >= {id} ORDER BY id LIMIT {limit}")
    await conn.close()
    return rows
