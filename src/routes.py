from pg_login import pg_login
from pg_painel_controle import pg_painel_controle
from pg_cadastro_vendas import pg_cadastro_vendas
from pg_revisao_vendas import pg_revisao_vendas

ROUTES = {
        '/login'          : pg_login,
        '/painel_controle': pg_painel_controle,
        '/cadastro_vendas': pg_cadastro_vendas,
        '/revisao_vendas' : pg_revisao_vendas
    }