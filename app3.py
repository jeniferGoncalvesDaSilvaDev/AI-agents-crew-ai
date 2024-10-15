import os
from crewai import Agent, Task, Crew, Process
from search_tools import SearchTools  # Importando a classe SearchTools
from langchain_openai import ChatOpenAI  # Importando a classe ChatOpenAI

# Definir a chave da API diretamente no código (não recomendado para produção)
serper_api_key = 'cb0d7b3ed11bfd1a68c4e90a9b89096477586dd2'

# Verificar se a chave da API foi carregada corretamente
if not serper_api_key:
    raise ValueError("A chave da API do Serper não foi encontrada. Verifique a chave corretamente.")

# Instanciar a ferramenta de busca usando a classe SearchTools
search_tool = SearchTools(api_key=serper_api_key)  # Passando a chave da API para a ferramenta de busca

# 1. Agente de Pesquisa (Researcher) - usando Serper para pesquisas
researcher = Agent(
    role="Researcher",
    goal="""Explique o que são agentes de IA, como eles funcionam, e identifique as principais bibliotecas, como LangChain, 
    que são usadas para criá-los.""",
    backstory="""Pesquise como bibliotecas como LangChain permitem a criação de agentes e identifique os componentes básicos, como ambientes,
    ferramentas e funções.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool.search_internet]  # Usando o método de busca da classe
)

# 2. Agente Escritor (Writer)
writer = Agent(
    role="Writer",
    goal="Desenvolva um tutorial completo explicando como criar agentes utilizando a LangChain.",
    backstory="""Estruture a explicação de forma didática, com uma introdução sobre agentes, os principais componentes da LangChain,
    e exemplos de implementação.""",
    verbose=True,
    allow_delegation=False
)

# 3. Agente Desenvolvedor (Developer)
developer = Agent(
    role="Developer",
    goal="Forneça exemplos práticos de código para a criação de agentes com LangChain.",
    backstory="""Implemente um agente simples usando LangChain que possa responder perguntas usando uma base de conhecimento ou uma API.""",
    verbose=True,
    allow_delegation=False
)

# 4. Agente Revisor (Reviewer)
reviewer = Agent(
    role="Reviewer",
    goal="Revisar o tutorial criado e garantir que ele esteja claro, preciso e fácil de entender.",
    backstory="""Verifique se o tutorial cobre todos os aspectos essenciais, se o código está correto, e se o leitor consegue
    seguir as instruções sem dificuldades.""",
    verbose=True,
    allow_delegation=False
)

# Instanciar o modelo GPT
