import os
import openai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY

client = openai.Client(api_key=API_KEY)

response = client.images.edit(
  model="dall-e-2",
  image=open("/image_generater.py", "rb"),
  prompt="make the incense behind the book",
  n=1,
  size="1024x1024"
)
image_url = response.data[0].url