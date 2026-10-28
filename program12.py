from PIL import Image, ImageFilter
import os

def apply_grayscale(input_path: str, output_path: str):
    """
    Converts an image to grayscale by calculating the luminance of raw RGB channels.
    Input:
        input_path (str): Path to the source image (JPEG/PNG).
        output_path (str): Path to save the processed image.
    Output:
        None (Saves the output image to disk)
    """
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        pixels = img.load()
        
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                pixels[x, y] = (gray, gray, gray)
                
        img.save(output_path)
        print(f"Grayscale image saved to: {output_path}")

def apply_thresholding(input_path: str, output_path: str, threshold: int = 128):
    """
    Applies a binary threshold to generate a stark black and white image.
    Input:
        input_path (str): Path to the source image.
        output_path (str): Path to save the processed image.
        threshold (int): Brightness cutoff (0-255). Values above become white, below become black.
    Output:
        None (Saves the output image to disk)
    """
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        pixels = img.load()
        
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                
                bw_val = 255 if gray >= threshold else 0
                pixels[x, y] = (bw_val, bw_val, bw_val)
                
        img.save(output_path)
        print(f"Threshold (B&W) image saved to: {output_path}")

def apply_spatial_blur(input_path: str, output_path: str, radius: int = 3):
    """
    Applies a simple spatial blur filter to the image.
    Input:
        input_path (str): Path to the source image.
        output_path (str): Path to save the processed image.
        radius (int): The intensity/spread of the blur.
    Output:
        None (Saves the output image to disk)
    """
    with Image.open(input_path) as img:
        blurred_img = img.filter(ImageFilter.BoxBlur(radius))
        blurred_img.save(output_path)
        print(f"Blurred image saved to: {output_path}")

def generate_test_image(test_path: str):
    """Helper function to generate a basic test image if none exists."""
    img = Image.new('RGB', (200, 200), color = (73, 109, 137))
    pixels = img.load()
    for x in range(50, 150):
        for y in range(50, 150):
            pixels[x, y] = (255, 100, x)
    img.save(test_path)
    print(f"Generated test image at: {test_path}")

if __name__ == "__main__":
    print("--- Digital Image Filter and Color Converter Utility ---\n")
    
    source_img = "sample_input.jpg"
    if not os.path.exists(source_img):
        generate_test_image(source_img)

    apply_grayscale(source_img, "output_grayscale.jpg")
    apply_thresholding(source_img, "output_threshold.jpg", threshold=100)
    apply_spatial_blur(source_img, "output_blurred.jpg", radius=4)