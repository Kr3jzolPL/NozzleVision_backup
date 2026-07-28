# ==========================================
# NozzleVision Configuration
# ==========================================

# Camera
CAMERA_URL = "http://192.168.1.117:8080/?action=snapshot"

# ==========================================
# ROI
# ==========================================

ROI_X = 448
ROI_Y = 208
ROI_WIDTH = 338
ROI_HEIGHT = 194

# ==========================================
# Image Processing
# ==========================================

# Gaussian blur
BLUR_KERNEL = (5, 5)
BLUR_SIGMA = 0

# Binary threshold
THRESHOLD = 120
THRESHOLD_MAX = 255

# Adaptive threshold
ADAPTIVE_MAX = 255
ADAPTIVE_BLOCK_SIZE = 11
ADAPTIVE_C = 2

# Canny edge detection
CANNY_LOW = 30
CANNY_HIGH = 100