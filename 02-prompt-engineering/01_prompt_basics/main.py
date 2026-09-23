import requests

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
    prompts = [
        "Explain DMA.",

        "Explain DMA to a beginner.",

        """You are an embedded systems engineer.
           Explain DMA to a beginner.
           Use a simple example.
           Keep the answer under 100 words."""
    ]

    for i, prompt in enumerate(prompts, 1):
        print(f"\n{'=' * 60}")
        print(f"PROMPT {i}")
        print("=" * 60)
        print(prompt)

        print("\nAI:")
        print(ask_llm(prompt))


if __name__ == "__main__":
    main()
