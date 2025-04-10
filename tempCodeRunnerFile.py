import cv2
import numpy as np
import matplotlib.pyplot as plt
def affine_transform(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    rows, cols, _ = image.shape

    src_points = np.float32([[50, 50], [200, 50], [50, 200]])
    dst_points = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(src_points, dst_points)

    transformed_image = cv2.warpAffine(image, M, (cols, rows))

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(transformed_image)
    plt.title('Affine Transformed Image')
    plt.axis('off')

    plt.show()


image_path = '"C:\\Users\\hp\\OneDrive\\Desktop\\New folder\\IMG20241230102201.jpg"'
affine_transform(image_path)