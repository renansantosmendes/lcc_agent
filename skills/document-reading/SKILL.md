---
name: document-reading
description: Lê e resume arquivos PDF, DOCX e PPTX enviados pelo usuário, e responde perguntas sobre o conteúdo.
---
# Skill de Leitura de Documentos

## Quando Usar
- Sempre que o usuário citar um arquivo `.pdf`, `.docx` ou `.pptx` e pedir um resumo, dados, trechos ou uma resposta baseada no conteúdo.

## Protocolo de Execução
1. **Confirme o caminho:** o arquivo precisa estar no disco. Se o usuário não informar o caminho completo, peça antes de tentar ler.
2. **Formato:** aceite apenas PDF, DOCX e PPTX. Para `.doc` ou `.ppt` (formato antigo), explique que não é suportado e sugira converter para `.docx` ou `.pptx`.
3. **Leitura:**
   - Documento curto: chame `read_document` com o caminho completo e responda com base no texto.
   - Documento longo ou pergunta específica: delegue ao subagent `document_analyst`.
4. **Resposta:** responda apenas com o que está no documento. Se a informação não existir nele, diga isso explicitamente.

## Formato de Resposta
### 📄 [Nome do arquivo]
* **Resumo:** [2 a 4 frases]
* **Pontos principais:** lista curta
* **Trechos relevantes:** citados entre aspas, quando o usuário pedir precisão
