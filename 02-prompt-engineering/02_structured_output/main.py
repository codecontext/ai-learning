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
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()["response"]

def main():
    prompt = """
             Explain DMA and return the answer as JSON.

             Use exactly these fields:
             {
                 "concept": "...",
                 "purpose": "...",
                 "example": "..."
             }

             Do not include any other text outside the JSON.
             """

    answer = ask_llm(prompt)

    print("Raw AI response:")
    print(answer)

    print("\nParsed data:")

    data = json.loads(answer)

    print("Concept:", data["concept"])
    print("Purpose:", data["purpose"])
    print("Example:", data["example"])


if __name__ == "__main__":
    main()
