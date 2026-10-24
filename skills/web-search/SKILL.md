---
name: web-search
description: Busca informações atuais, dados específicos e referências na web com a ferramenta web_search (Tavily), e cita as fontes.
---
# Skill de Busca na Web

## Quando Usar
- Quando a pergunta depende de informação que pode ter mudado: datas, legislação, preços, versões, notícias ou estatísticas recentes.
- Quando o usuário pedir fontes, referências ou links.
- Quando você não tem certeza de um fato específico (nomes, números, datas, citações exatas).

## Quando Não Usar
- Conteúdo consolidado de uma disciplina (conceitos, teorias, fórmulas clássicas). Responda com o seu conhecimento.
- Perguntas sobre você ou sobre o que você faz.

## Protocolo de Execução
1. **Reformule a pergunta em palavras-chave:** use de 3 a 6 termos. Ex.: "Lei de Diretrizes e Bases artigo 26 ensino médio".
2. **Chame `web_search`** com a query. Use `max_results` padrão (5), a menos que o usuário peça mais ou menos fontes.
3. **Avalie os resultados:**
   - Prefira fontes oficiais, universidades, órgãos públicos e publicações revisadas.
   - Descarte resultados que não tratam do tema pedido.
   - Se o campo `answer` vier preenchido, use-o como ponto de partida, mas confirme com o `content` das fontes.
4. **Se a busca falhar** (campo `error`, lista vazia ou resultados fora do tema), diga isso ao usuário e responda com o que sabe, deixando claro o que não foi verificado.
5. **Use `raw_content` com cuidado:** é o texto completo da página, cortado no limite. Use só quando o `content` não bastar.

## Formato de Resposta
- Resposta direta primeiro, em português do Brasil.
- Lista de fontes ao final, com título e URL:
  ```
  Fontes:
  - [Título](https://exemplo.gov.br/...)
  ```
- Informação que não apareceu nas fontes deve ser marcada como conhecimento geral, sem atribuir a uma fonte.
