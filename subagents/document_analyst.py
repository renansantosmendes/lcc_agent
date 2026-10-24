"""Subagent that reads documents and answers questions about their content."""

from tools.document_reader import read_document

DOCUMENT_ANALYST_PROMPT = (
    "Você é um analista de documentos. Leia o arquivo indicado com a ferramenta "
    "read_document, depois responda à pergunta usando apenas o conteúdo lido. "
    "Se a informação não estiver no documento, diga isso explicitamente. "
    "Responda em português do Brasil e devolva um resumo objetivo, com os trechos "
    "relevantes citados entre aspas."
)


def document_analyst_spec(model):
    """Return the SubAgent spec for the document analyst.

    Parameters
    ----------
    model : BaseChatModel
        Model used by the subagent.
    """
    return {
        "name": "document_analyst",
        "description": (
            "Lê e analisa um PDF, DOCX ou PPTX específico: resume, extrai dados "
            "ou responde perguntas sobre o conteúdo. Use para documentos longos."
        ),
        "system_prompt": DOCUMENT_ANALYST_PROMPT,
        "tools": [read_document],
        "model": model,
    }
