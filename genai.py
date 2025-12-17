from google import genai
import user_config

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=user_config.genAI_api_key)


def send_prompt(prompt):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    print(response.text.replace("#", "").replace("*", ""))
    return response.text.replace("#", "").replace("*", "")


# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="About Bangladesh"
# )
# print(response.text.replace("#", "").replace("*", ""))
