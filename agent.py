"""Creates the deep agent with ChatOpenAI, the document tools, subagents and skills.

Shared by the terminal chat (run.py) and any other entry point.

Required environment variables:
    OPENAI_API_KEY   key of the OpenAI model
    TAVILY_API_KEY   key of the Tavily search API (web_search tool)
"""

import os
from pathlib import Path

from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from subagents import build_subagents
from tools.document_reader import read_document
from tools.web_search import web_search

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

SYSTEM_PROMPT = (
    "Você é um assistente de criação de conteúdo didático. Você produz material "
    "para disciplinas do ensino médio, ensino básico, graduação e pós-graduação: "
    "planos de aula, resumos, explicações, exemplos, exercícios com gabarito, "
    "roteiros de slides e avaliações. "
    "Responda sempre em português do Brasil. "
    "Antes de criar qualquer material, identifique o nível (ensino médio, ensino "
    "básico, graduação ou pós-graduação), a disciplina e o tema. Se algum deles "
    "estiver faltando e mudar o resultado, pergunte antes de produzir. "
    "Adapte a linguagem, a profundidade e o vocabulário ao nível: no ensino médio "
    "e no básico, use linguagem simples, exemplos do cotidiano e pouca notação; "
    "na graduação, use a terminologia técnica da área e cite autores e teorias "
    "relevantes; na pós-graduação, aprofunde a discussão, trate de limitações, "
    "debates em aberto e literatura recente. "
    "Estruture o conteúdo com objetivos de aprendizagem, desenvolvimento do tema, "
    "exemplos resolvidos, atividades e, quando pedido, gabarito. "
    "Use a ferramenta web_search somente quando precisar de informação atual, "
    "dados específicos, referências ou verificação de fatos que você não tem "
    "certeza. Não use a busca para conteúdo consolidado da disciplina. "
    "Quando usar a busca, cite as URLs de origem ao final do material. "
    "Para ler um arquivo enviado pelo usuário, use read_document com o caminho "
    "completo. Para documentos longos ou análises mais profundas, delegue ao "
    "subagent document_analyst. "
    "Se a pergunta for sobre você ou sobre o que você faz, responda diretamente, "
    "sem procurar em arquivos."
)


def create_agent():
    """Create the agent with the document and web tools, the subagents and the skills folder.

    Returns
    -------
    object
        A compiled deep agent; call ``invoke({"messages": [...]})`` on it.
    """
    model = ChatOpenAI(model=os.getenv("MODEL_NAME", "gpt-4o-mini"), temperature=0)

    agent = create_deep_agent(
        model=model,
        tools=[read_document, web_search],
        subagents=build_subagents(model),
        backend=FilesystemBackend(root_dir=str(BASE_DIR), virtual_mode=True),
        skills=[str(BASE_DIR / "skills")],
        system_prompt=SYSTEM_PROMPT,
    )
    return agent
