"""Terminal chat with the document agent. Type 'sair' to quit."""

from agent import create_agent


def main():
    agent = create_agent()
    print("Agente de documentos iniciado. Digite 'sair' para encerrar.")

    while True:
        question = input("\nVocê: ").strip()
        if question.lower() in {"sair", "exit", "quit"}:
            break
        if not question:
            continue

        result = agent.invoke({"messages": [{"role": "user", "content": question}]})
        print(f"\nAgente: {result['messages'][-1].content}")


if __name__ == "__main__":
    main()
