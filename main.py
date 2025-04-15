from PIL import Image, ImageDraw, ImageFont
import os

def generate_image(prompt, output_path='output.png'):
    img = Image.new('RGB', (600, 400), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Gunakan font default sistem
    font = ImageFont.load_default()
    d.text((10, 150), prompt, fill=(0, 0, 0), font=font)

    img.save(output_path)
    print(f"Gambar berhasil dibuat: {output_path}")

if __name__ == "__main__":
    user_input = input("Masukkan prompt teks untuk digambar: ")
    generate_image(user_input)
