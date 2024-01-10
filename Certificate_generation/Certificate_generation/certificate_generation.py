import os
import requests
from openai import OpenAI



VARIABLE_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=VARIABLE_KEY)

def generate_certificate_background(output_folder):
    # Step 1: Generate Beautiful Certificate Background (Using OpenAI API)
    
    response = client.images.generate(
        model="dall-e-3",
        prompt="""
                Create a minimalist and sophisticated certificate background, ideal for highlighting achievements without overshadowing the main content. The design should feature very light and unobtrusive bold Red patterns, ensuring they are not too eye-catching. Include thin, elegant borders that frame the certificate tastefully. The color palette should be restricted to soft, neutral tones, providing a clean and professional look. Overall, the background must support and enhance the legibility and prominence of the certificate's text, blending seamlessly with the overall layout, without drawing attention away from the central message of the certificate, put no wrting oon the background, use bold red color for the boarders
        """,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    background_path = os.path.join(output_folder, 'certificate_background.png')

    # Use requests to download the image
    with open(background_path, 'wb') as f:
        f.write(requests.get(image_url).content)

    return background_path
