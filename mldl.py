import cv2
import numpy as np
import matplotlib.pyplot as plt

def data_augmentation(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    (h, w) = image.shape[:2]
    
    # Translation
    trans_matrix = np.float32([[1, 0, 60], [0, 1, 60]])
    translated = cv2.warpAffine(image, trans_matrix, (w, h))
    
    # Rotation
    center = (w // 2, h // 2)
    rot_matrix = cv2.getRotationMatrix2D(center, 30, 1.2)
    rotated = cv2.warpAffine(image, rot_matrix, (w, h))
    
    # Scaling
    scaled = cv2.resize(image, (int(w * 1.2), int(h * 1.2)))
    
    # Shearing
    shear_matrix = np.float32([[1, 0.4, 0], [0.4, 1, 0]])
    sheared = cv2.warpAffine(image, shear_matrix, (w, h))
    
    # Horizontal Flip
    flipped_h = cv2.flip(image, 1)
    
    # Vertical Flip
    flipped_v = cv2.flip(image, 0)
    
    # Cropping
    crop_x, crop_y = 40, 40
    crop_w, crop_h = min(250, w) - crop_x, min(250, h) - crop_y
    cropped = image[crop_y:crop_y + crop_h, crop_x:crop_x + crop_w]
    
    # Skewing
    skew_matrix = np.float32([[1, 0.3, 0], [0.3, 1, 0]])
    skewed = cv2.warpAffine(image, skew_matrix, (w, h))
    
    # Display images
    plt.figure(figsize=(12, 12))
    
    images = [(image, 'Original Image'), (translated, 'Translated'), (rotated, 'Rotated'),
              (scaled, 'Scaled'), (sheared, 'Sheared'), (flipped_h, 'Horizontally Flipped'),
              (flipped_v, 'Vertically Flipped'), (cropped, 'Cropped')]
    
    for i, (img, title) in enumerate(images, 1):
        plt.subplot(2, 4, i)
        plt.imshow(img)
        plt.title(title)
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Example usage
image_path = 'path_to_your_image.jpg'  # Replace with your actual image path
data_augmentation(image_path)