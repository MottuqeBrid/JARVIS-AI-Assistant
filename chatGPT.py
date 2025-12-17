from openai import OpenAI
import user_config

client = OpenAI(api_key=user_config.chatgpt_api_key)

response = client.responses.create(
    model="gpt-5.2", input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
