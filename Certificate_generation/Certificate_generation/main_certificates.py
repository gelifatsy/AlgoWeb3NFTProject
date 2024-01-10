import os

from certificate_generation import generate_certificate_background
from certificate_editing import create_certificate_with_info

# Example usage (assuming your logo filename is 'logo.png' in the same directory)
output_folder = 'generated_certificates'
os.makedirs(output_folder, exist_ok=True)

# Step 1: Generate Certificate Background
background_path = generate_certificate_background(output_folder)

# Step 2: Generate Variations or Edits (Using Image Processing Libraries)
edited_certificate_path = create_certificate_with_info(
    background_path, 'Elias Assamne Gebretsadik', 'logo.png', 'January 1, 2024', output_folder
)

print(f"Certificate generated and saved at: {edited_certificate_path}")
