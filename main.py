from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from agno.tools.file import FileTools
from agno.team import Team
from pathlib import Path
from dotenv import load_dotenv


# imporando as variáveis de ambiente
load_dotenv()

# criando o agente
jornalista = Agent(
    name="Jornalista",
    role="Pesquisador de dados em tempo real",
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um jornalista",
    instructions=[
        "Pesquise as informações mais recentes na web.",
        "Forneça os dados brutos, links e fontes oficiais para o Editor-Chefe.",
        "Busque apenas pesquisas gerais na web. NUNCA use a função de pesquisa de notícias, mesmo que o usuário use a palavra 'notícias'.",
    ],
    tools=[DuckDuckGoTools()],
    markdown=True,
)

editor = Agent(
    name="Editor",
    role="Redator e Revisor",
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um redator e revisor",
    tools=[FileTools(base_dir=Path.cwd())],
    instructions=[
        "Você é o Editor-Chefe de um newsletter.",
        "Sempre delegue a busca por notícias ao jornalista.",
        "Quando receber os dados do Jornalista, escreva um artigo formatado.",
        "Sempre que o usuário pedir, use a ferramenta de arquivos para salvar o texto final.",
    ],
    markdown=True,
)

team = Team(
    name="Time",
    members=[jornalista, editor],
    db=SqliteDb(db_file="historico_chat.db"),
    add_history_to_context=True,
    instructions=[
        "Você é o coordenador da equipe.",
        "Sempre que o usuário pedir para buscar novidades, dados ou pesquisar na web, delegue imediatamente para o Jornalista.",
        "Sempre que o usuário pedir para escrever um texto final, formatar um documento ou salvar um arquivo no disco, delegue imediatamente para o Editor.",
    ],
)


print('Olá! Sou o seu assistente de notícias. Digite "sair" para encerrar.')

while True:
    pergunta = input("\nVocê: ")

    # verificando se o utilizador quer sair
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Até logo!")
        break

    # stream faz o texto aparecer aos poucos
    team.print_response(pergunta, stream=True)
