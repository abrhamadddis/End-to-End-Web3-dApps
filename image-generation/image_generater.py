import os
import openai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY

client = openai.Client(api_key=API_KEY)

response = client.images.generate(
 model="dall-e-3",
 prompt="",
 quality="standard",
 n=1,
)

image_url = response.data[0].url

print(image_url)