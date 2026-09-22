import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:1.7b"


def ask_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": True
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()
    return data["response"]

def main():
    prompt = input("You: ")

    try:
        answer = ask_llm(prompt)
        print("\nAI:", answer)
    except requests.exceptions.RequestException as e:
        print(f"\nError communicating with Ollama: {e}")


if __name__ == "__main__":
    main()
