import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)
response = client.images.create_variation(
  image=open("certificate.png", "rb"),
  n=2,
  size="1024x1024"
)

image_url = response.data[0].url

print(image_url)