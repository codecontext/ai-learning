import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:1.7b"


def ask_llm(messages):
    prompt = ""

    for message in messages:
        prompt += f"{message['role']}: {message['content']}\n"

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

    answer = ""

    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            chunk = data["response"]
            print(chunk, end="", flush=True)
            answer += chunk

    print()

    return answer


def main():
    messages = []

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({
            "role": "user",
            "content": user_input
        })

        print("\nAI: ", end="")

        answer = ask_llm(messages)

        messages.append({
            "role": "assistant",
            "content": answer
        })


if __name__ == "__main__":
    main()
