from google import genai
from openai import chat
import user_config

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=user_config.genAI_api_key)


def send_prompt(prompt):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    print(response.text.replace("#", "").replace("*", ""))
    return response.text.replace("#", "").replace("*", "")


def send_prompt2(prompt):
    client = genai.Client(api_key=user_config.genAI_api_key2)
    chat = client.chats.create(model="gemini-2.5-flash")

    response = chat.send_message("I have 2 dogs in my house.")
    print(response.text)
    print("--------------")
    response = chat.send_message("How many paws are in my house?")
    print(response.text)
    print("--------------")
    for message in chat.get_history():
        print(f"role - {message.role}", end=": ")
    #     print(message.parts[0].text)
    # print(response.text.replace("#", "").replace("*", ""))
    # return response.text.replace("#", "").replace("*", "")


if __name__ == "__main__":
    # send_prompt("Explain quantum computing in simple terms.")
    print("Using API Key 1:")
