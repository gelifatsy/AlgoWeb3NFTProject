import os
from PIL import Image, ImageDraw, ImageFont

def create_certificate_with_info(existing_certificate_path, full_name, logo_filename, date, output_folder):
    certificate_image = Image.open(existing_certificate_path)
    draw = ImageDraw.Draw(certificate_image)

    # Set a maximum size for the text and logo
    max_text_size = 30
    max_logo_size = (certificate_image.width // 3, certificate_image.height // 6)

    # Calculate the available space for the text and logo
    available_text_space = certificate_image.height - max_logo_size[1]
    available_logo_space = certificate_image.width

    # Adjust the font size based on available space
    font_size = min(max_text_size, available_text_space // 4)
    font = ImageFont.load_default().font_variant(size=font_size)

    # Load the logo and resize it based on available space
    logo_path = os.path.join(os.getcwd(), logo_filename)
    logo_image = Image.open(logo_path)
    logo_image.thumbnail(max_logo_size)

    # Add space or padding from the top before the logo starts
    space_before_logo_top = 100
    # Calculate the center position for the logo
    logo_position = ((certificate_image.width - logo_image.width) // 2, space_before_logo_top)

    # Paste the logo at the center
    certificate_image.paste(logo_image, logo_position)

    # Add space before the text
    space_before_text = 80
    # Calculate the bounding box for the text
    text_bbox = draw.textbbox((0, 0), full_name, font=font)

    # Extract width and height from the bounding box
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate the position for the text
    text_position = ((certificate_image.width - text_width) // 2, logo_position[1] + logo_image.height + space_before_text)

    # Draw text at the center
    draw.text(text_position, full_name, (0, 0, 0), font=font)

    # Draw "Certificate of Achievement" at the center
    achievement_title = "This Certificate is"
    achievement_title_position = ((certificate_image.width - draw.textbbox((0, 0), achievement_title, font=font)[2]) // 2, text_position[1] + text_height + 20)
    draw.text(achievement_title_position, achievement_title, (0, 0, 0), font=font)

    # Draw additional achievement-related text
    achievement_text = f"Presented to {full_name} \n\nfor successfully completing our data\n\n science training with distinction."
    achievement_position = ((certificate_image.width - draw.textbbox((0, 0), achievement_text, font=font)[2]) // 2, achievement_title_position[1] + text_height + 20)
    draw.multiline_text(achievement_position, achievement_text, (0, 0, 0), font=font, spacing=5)

    # Draw space before the date
    space_before_date_bottom = 350

    # Draw date text at the bottom-right corner
    date_position = (certificate_image.width - text_width - space_before_date_bottom, certificate_image.height - space_before_date_bottom)
    date_content = f"Date: {date}"
    draw.text(date_position, date_content, (0, 0, 0), font=font)

    final_certificate_path = os.path.join(output_folder, 'final_certificate.png')
    certificate_image.save(final_certificate_path)

    return final_certificate_path


existing_certificate_path = 'generated_certificates/certificate_background.png'
output_folder = 'generated_certificates'
full_name = 'Elias Assamnew Gebretsadik'
logo_filename = 'logo.png'
date = '2024-01-10'

edited_certificate_path = create_certificate_with_info(existing_certificate_path, full_name, logo_filename, date, output_folder)
print(f"Edited certificate saved at: {edited_certificate_path}")
