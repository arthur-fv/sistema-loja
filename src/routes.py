from view_login import view_login
from view_painel_controle import view_painel_controle
from view_cadastro_vendas import view_cadastro_vendas
from view_revisao_vendas import view_revisao_vendas

ROUTES = {
        '/login'          : view_login,
        '/painel_controle': view_painel_controle,
        '/cadastro_vendas': view_cadastro_vendas,
        '/revisao_vendas' : view_revisao_vendas
    }