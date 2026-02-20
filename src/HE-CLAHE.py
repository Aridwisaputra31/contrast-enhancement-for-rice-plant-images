import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image, ax, title, color):
    ax.set_title(title)
    ax.set_xlabel('Pixel Intensities')
    ax.set_ylabel('Frequency')
    ax.hist(image.ravel(), 256, [0, 256], color=color)
    ax.set_xlim([0, 256])
    ax.set_ylim([0, 200000])


img_path = "D:/File Photo/Ari/SAMSUNG 1/HST 50/baris 1 hst 50/Rename/samsung_HST50_C1_(1)_07.52.jpg"
img_read = cv2.imread(img_path)
img_read_rgb = cv2.cvtColor(img_read, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)

lab_img = cv2.cvtColor(img_read, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab_img)

# 1. Histogram Equalization (HE)
l_equalized = cv2.equalizeHist(l)
lab_equalized = cv2.merge((l_equalized, a, b))
img_HE = cv2.cvtColor(lab_equalized, cv2.COLOR_LAB2RGB)
img_HE_gray = cv2.cvtColor(img_HE, cv2.COLOR_RGB2GRAY)

# 2. Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
cl_l = clahe.apply(l)
merged_img = cv2.merge((cl_l, a, b))
img_clahe = cv2.cvtColor(merged_img, cv2.COLOR_LAB2RGB)
img_clahe_gray = cv2.cvtColor(img_clahe, cv2.COLOR_RGB2GRAY)


plt.figure()
plt.title('Citra RGB')
plt.imshow(img_read_rgb)
plt.axis('off')
fig, axes = plt.subplots(3, 2, figsize=(12, 12))

# Image 
axes[0, 0].imshow(img_gray, cmap='gray')
axes[0, 0].set_title('Citra Grayscale')
axes[0, 0].axis('off')
plot_histogram(img_gray, axes[0, 1], 'Histogram Citra Asli', 'blue')

# Image with HE
axes[1, 0].imshow(img_HE_gray, cmap='gray')
axes[1, 0].set_title('HE (Histogram Equalization)')
axes[1, 0].axis('off')
plot_histogram(img_HE_gray, axes[1, 1], 'Histogram HE', 'green')

# Image with CLAHE
axes[2, 0].imshow(img_clahe_gray, cmap='gray')
axes[2, 0].set_title('CLAHE (Contrast Limited AHE)')
axes[2, 0].axis('off')
plot_histogram(img_clahe_gray, axes[2, 1], 'Histogram CLAHE', 'red')

plt.tight_layout()
plt.show()

