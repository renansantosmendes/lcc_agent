# AGENTS.md

Instruções para quem (pessoa ou agente de código) altera este projeto.

## Visão geral

`lcc_agent` é um agente de criação de conteúdo didático, construído com `deepagents` e LangChain. Ele usa tools (`tools/`), subagents (`subagents/`) e skills (`skills/`), montados em `agent.py`.

## Boas práticas de Python

- Siga PEP 8 e use type hints em funções públicas.
- Docstrings no padrão NumPy, como em `agent.py`.
- Mantenha funções pequenas, com uma responsabilidade. Prefira funções puras quando possível.
- Não coloque segredos no código. Chaves ficam em `.env` (nunca versionado) e o modelo de referência está em `.env.example`.
- Carregue variáveis de ambiente em um único ponto (`agent.py`), não em cada módulo.
- Não use `print` para depuração em código comitado. Use `logging`.
- Trate exceções de I/O e de APIs externas. Não deixe uma falha de rede derrubar a conversa.
- Fixe versões de dependências em `requirements.txt`, como o restante do projeto.
- Antes de comitar, rode `python -m py_compile` nos arquivos alterados e limpe `__pycache__`.

## Boas práticas de agentes

- **Tools:** o docstring é a descrição que o modelo lê. Escreva-o com clareza: quando usar, o que recebe e o que devolve.
- **Erros em tools:** devolva uma mensagem de erro legível (`str` ou `dict` com `error`) em vez de lançar exceção. O modelo consegue reagir a uma mensagem, mas não a um traceback.
- **Validação:** valide entradas antes de agir. Ex.: `read_document` recusa extensões não suportadas e arquivos inexistentes.
- **Tamanho de saída:** limite o texto devolvido pelas tools (ex.: `MAX_RAW_CHARS` em `web_search`). Saídas grandes gastam contexto e pioram a resposta.
- **Menor privilégio:** cada subagent recebe só as tools de que precisa.
- **Subagents:** use para tarefas longas ou que exigem contexto próprio, como análise de documentos. Não crie subagents para tarefas simples.
- **Skills:** uma skill descreve um procedimento (quando agir, como responder). Não coloque lógica de código em `SKILL.md`. Código fica em `tools/`.
- **Prompts:** ficam como constantes nomeadas (`SYSTEM_PROMPT`, `DOCUMENT_ANALYST_PROMPT`), não espalhados pelo código.
- **Fontes e incerteza:** o agente deve citar fontes quando usar busca e deixar claro o que não foi verificado. Não inventar referências, números ou citações.
- **Ações irreversíveis:** qualquer tool que escreva, apague ou envie algo fora do projeto deve pedir confirmação do usuário antes.

## Como testar mudanças

- Teste tools isoladamente, sem o modelo, com entradas válidas e inválidas.
- Para mudanças no prompt ou nas skills, rode `python run.py` e confira pelo menos um caso por nível de ensino (médio, básico, graduação e pós-graduação).
- Não rode testes que gastam a API (OpenAI ou Tavily) sem avisar quem está alterando o projeto.

## Estrutura

Veja o [README.md](README.md) para a estrutura de pastas e como adicionar tools, subagents e skills.
