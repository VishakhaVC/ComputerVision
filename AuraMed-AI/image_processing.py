import io
import base64
from PIL import Image, ImageEnhance
import numpy as np

def preprocess_image(image: Image.Image, target_size=(256, 256)):
    """
    Apply any needed enhancement (brightness, contrast) and resize.
    """
    # Auto-adjust contrast as a rudimentary pre-processing
    enhancer = ImageEnhance.Contrast(image)
    img_contrast = enhancer.enhance(1.2)
    
    # Auto-adjust brightness to fix low-light issues conditionally
    img_gray = img_contrast.convert('L')
    stat = np.mean(np.array(img_gray))
    if stat < 100:  # Image is generally dark
        b_enhancer = ImageEnhance.Brightness(img_contrast)
        img_contrast = b_enhancer.enhance(1.5)
        
    img_resized = img_contrast.resize(target_size, Image.Resampling.LANCZOS)
    return img_resized


def encode_image_base64(image: Image.Image) -> str:
    """
    Encodes PIL Image into a base64 string.
    """
    buffered = io.BytesIO()
    # Save as JPEG for compression over the wire
    image.save(buffered, format="JPEG", quality=85)
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{img_str}"

def decode_image_base64(base64_string: str) -> Image.Image:
    """
    Decodes a base64 string into a PIL Image.
    """
    header, encoded = base64_string.split(",", 1)
    image_data = base64.b64decode(encoded)
    return Image.open(io.BytesIO(image_data))
