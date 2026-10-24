"""Tool that reads the text of PDF, DOCX and PPTX files via langchain-unstructured."""

from pathlib import Path

from langchain_core.tools import tool
from langchain_unstructured import UnstructuredLoader

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".pptx"}


@tool
def read_document(file_path: str) -> str:
    """Lê o texto de um arquivo PDF, DOCX ou PPTX e devolve o conteúdo.

    Args:
        file_path: caminho completo do arquivo no disco.
    """
    path = Path(file_path)

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        return f"Formato não suportado: '{path.suffix}'. Use PDF, DOCX ou PPTX."
    if not path.is_file():
        return f"Arquivo não encontrado: {file_path}"

    docs = UnstructuredLoader(file_path=str(path)).load()
    return "\n\n".join(doc.page_content for doc in docs)
