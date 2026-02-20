# contrast-enhancement-for-rice-plant-images
Implementation of histogram equalization for contrast enhancement of rice plant images using Python and OpenCV.

##HE and CLAHE
This project compares Histogram Equalization (HE) and Contrast Limited Adaptive Histogram Equalization (CLAHE) for enhancing rice plant images. Histogram Equalization improves image contrast globally by redistributing intensity values across the entire image, but it can lead to over-enhancement, loss of detail, and amplification of noise in areas with uneven lighting. CLAHE addresses these limitations by applying contrast enhancement locally on small regions (tiles) and introducing a clip limit to prevent excessive contrast. As a result, CLAHE produces more natural-looking images, preserves important texture details of leaves, and performs better under varying illumination conditions commonly found in agricultural environments.

Images were collected from three different smartphones with different camera specifications to represent real-world variability in image quality. CLAHE is applied to reduce these differences and enhance important visual details consistently across devices.


