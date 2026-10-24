# lcc_agent

Agente de documentos (PDF, DOCX e PPTX) construído com `deepagents` e LangChain.

## Estrutura

```
lcc_agent/
├── agent.py                 # create_agent(): modelo, tools, subagents e skills
├── run.py                   # chat no terminal
├── tools/
│   ├── document_reader.py   # read_document: lê PDF, DOCX e PPTX (UnstructuredLoader)
│   └── web_search.py        # web_search: busca na web com Tavily (copiada do web_search_agent)
├── subagents/
│   ├── __init__.py          # build_subagents(): lista de subagents
│   └── document_analyst.py  # subagent que analisa documentos longos
├── skills/
│   ├── document-reading/
│   │   └── SKILL.md         # quando e como ler documentos
│   └── web-search/
│       └── SKILL.md         # quando buscar na web e como citar fontes
├── AGENTS.md                # instruções para quem altera o projeto
├── requirements.txt
└── .env.example
```

- **Tools:** funções que o agente chama diretamente. Ficam em `tools/`.
- **Subagents:** agentes especializados que o agente principal delega com a ferramenta `task`. Cada um tem nome, descrição, prompt, tools e modelo. Ficam em `subagents/`.
- **Skills:** arquivos `SKILL.md` com instruções de quando agir e como responder. Cada pasta em `skills/` é uma skill.

## Como rodar

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # preencha OPENAI_API_KEY
python run.py
```

## Adicionar coisas

- **Nova tool:** crie a função com `@tool` em `tools/` e adicione em `tools=[...]` no `agent.py`.
- **Novo subagent:** crie um módulo em `subagents/` que retorne o dicionário `SubAgent` e inclua na lista de `build_subagents`.
- **Nova skill:** crie `skills/<nome>/SKILL.md` com o front-matter `name` e `description`.
