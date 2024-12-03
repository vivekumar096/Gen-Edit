# Step 1: Install the required libraries
# Run the following command in your terminal
# pip install openai requests pillow

# Step 2: Import the necessary libraries
import openai
import requests
from PIL import Image

# Step 3: Set your OpenAI API key
openai.api_key = 'your_api_key_here'  # Replace with your actual OpenAI API key

# Step 4: Function to generate an image using the DALL-E API
def generate_image(text):
    # Create an image using the text prompt
    response = openai.Image.create(
        prompt=text,     # Text describing the image
        n=1,             # Number of images to generate
        size="256x256"   # Image size
    )
    # Return the URL of the generated image
    return response['data'][0]['url']

# Step 5: Generate an image with a text prompt
text_prompt = "batman art in red and blue color"  # Example prompt
image_url = generate_image(text_prompt)

# Step 6: Fetch the generated image
response = requests.get(image_url)

# Step 7: Open and display the image
img = Image.open(response.raw)
img.show()

# Optional: Save the image to a file
img.save("generated_image.png")
