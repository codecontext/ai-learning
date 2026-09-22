import requests
import json

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
        stream=True,
        timeout=120
    )

    response.raise_for_status()

    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            print(data["response"], end="", flush=True)

    print()


def main():
    prompt = input("You: ")

    try:
        print("\nAI: ", end="")
        ask_llm(prompt)
    except requests.exceptions.RequestException as e:
        print(f"\nError communicating with Ollama: {e}")


if __name__ == "__main__":
    main()
