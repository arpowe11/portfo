from PIL import Image

# Open the image
image_path = '/Users/apowell/Developer/portfo/static/assets/images/profil.jpeg'  # Replace with your image path
img = Image.open(image_path)

# Convert the image to black and white
bw_img = img.convert('L')

# Save the black and white image
bw_image_path = 'black_and_white_image.jpg'
bw_img.save(bw_image_path)

print(f"Image converted to black and white and saved as {bw_image_path}")
