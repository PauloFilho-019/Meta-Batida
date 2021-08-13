import os
from twilio.rest import Client
import pandas as pd
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

token = os.getenv('auth_token')
sid = os.getenv('account_sid')

client = Client(sid, token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    # print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            # aqui vai o seu telefone 
            to="+5519993128895",
            # aqui vai o telefone que o twilio gerou pra ti
            from_="+16195033549",
            body=f"Parábens {vendedor}, no mês de {mes} você bateu a meta de 55.000")
        print(message.sid)
