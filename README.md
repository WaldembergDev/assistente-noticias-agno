# Agno IA - Assistente de Notícias

Um sistema multiagente desenvolvido em Python utilizando a biblioteca [Agno](https://github.com/agno-ai/agno) para automatizar a pesquisa, redação e formatação de artigos e notícias. O sistema interage via linha de comando e utiliza a API da OpenAI (modelo `gpt-4o-mini`) para processamento de linguagem natural.

## 🚀 Funcionalidades

O projeto é composto por uma equipe de agentes com papéis específicos:

- **Jornalista:** Focado em realizar pesquisas na web em tempo real utilizando o DuckDuckGo. Extrai dados brutos, links e fontes para enviar adiante.
- **Editor:** Atua como redator e revisor. Ele recebe os dados levantados pelo Jornalista, formata o conteúdo em um artigo coeso e tem a capacidade de salvar o documento gerado localmente em seu computador.
- **Coordenador (Team):** Gerencia a interação entre o usuário e a equipe. Ele interpreta o que o usuário deseja e delega as pesquisas para o Jornalista ou a formatação e salvamento de arquivos para o Editor. O contexto e o histórico do chat são mantidos e salvos em um banco de dados local (`historico_chat.db`).

## 🛠️ Tecnologias e Dependências

- [Python](https://www.python.org/) 3.12+
- [Agno](https://github.com/agno-ai/agno) - Framework de criação de agentes
- [OpenAI](https://openai.com/) - Modelos de LLM (GPT-4o-mini)
- [DuckDuckGo Tools](https://pypi.org/project/ddgs/) (`ddgs`) - Para pesquisas web
- [uv](https://github.com/astral-sh/uv) - Gerenciador rápido de dependências (utilizado no projeto)

## ⚙️ Instalação e Configuração

1. Certifique-se de ter o gerenciador de dependências [uv](https://docs.astral.sh/uv/) instalado em sua máquina.
2. Na raiz do projeto, instale as dependências:
   ```bash
   uv sync
   ```
3. Crie um arquivo chamado `.env` na raiz do projeto. Ele armazenará suas credenciais. Adicione a sua chave da OpenAI:
   ```env
   OPENAI_API_KEY=sk-sua-chave-api-aqui
   ```

## ▶️ Como Usar

Para iniciar o assistente interativo, execute o arquivo principal pelo seu terminal:

```bash
uv run main.py
```
*(Ou, se preferir o método clássico, ative o ambiente virtual dentro de `.venv` e execute `python main.py`).*

Isso iniciará o chat interativo. Você pode dar comandos como:
- *"Busque as notícias mais recentes sobre os avanços da SpaceX e crie um artigo para minha newsletter."*
- *"Pesquise o resumo do jogo de ontem do Brasil e salve os dados num arquivo texto."*

Para encerrar o assistente, apenas digite `sair`, `exit` ou `quit`.
