import cv2

from nozzlevision.config import *


def preprocess(frame):

    # ----------------------------
    # Crop ROI
    # ----------------------------
    roi = frame[
        ROI_Y:ROI_Y + ROI_HEIGHT,
        ROI_X:ROI_X + ROI_WIDTH
    ]

    # ----------------------------
    # Grayscale
    # ----------------------------
    gray = cv2.cvtColor(
        roi,
        cv2.COLOR_BGR2GRAY
    )

    # ----------------------------
    # Gaussian Blur
    # ----------------------------
    blur = cv2.GaussianBlur(
        gray,
        BLUR_KERNEL,
        BLUR_SIGMA
    )

    # ----------------------------
    # Binary Threshold
    # ----------------------------
    _, binary = cv2.threshold(
        blur,
        THRESHOLD,
        THRESHOLD_MAX,
        cv2.THRESH_BINARY
    )

    # ----------------------------
    # Adaptive Threshold
    # ----------------------------
    adaptive = cv2.adaptiveThreshold(
        blur,
        ADAPTIVE_MAX,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        ADAPTIVE_BLOCK_SIZE,
        ADAPTIVE_C
    )

    # ----------------------------
    # Otsu Threshold
    # ----------------------------
    _, otsu = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # ----------------------------
    # Canny Edge Detection
    # ----------------------------
    edges = cv2.Canny(
        blur,
        CANNY_LOW,
        CANNY_HIGH
    )

    # ----------------------------
    # Find Contours
    # ----------------------------
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # ----------------------------
    # Measurement defaults
    # ----------------------------
    area = 0
    width = 0
    height = 0
    perimeter = 0
    x = 0
    y = 0

    contour_debug = roi.copy()

    # ----------------------------
    # Largest contour
    # ----------------------------
    if contours:

        largest = max(contours, key=cv2.contourArea)

        area = cv2.contourArea(largest)

        x, y, width, height = cv2.boundingRect(largest)

        perimeter = cv2.arcLength(largest, True)

        cv2.drawContours(
            contour_debug,
            [largest],
            -1,
            (0, 0, 255),
            2
        )

        cv2.rectangle(
            contour_debug,
            (x, y),
            (x + width, y + height),
            (255, 0, 0),
            2
        )

    # ----------------------------
    # Print measurements
    # ----------------------------
    print(f"Contours : {len(contours)}")
    print(f"Area     : {area:.2f}")
    print(f"Width    : {width}")
    print(f"Height   : {height}")
    print(f"Perimeter: {perimeter:.2f}")

    # ----------------------------
    # Return pipeline
    # ----------------------------
    return {
        "roi": roi,
        "gray": gray,
        "blur": blur,
        "binary": binary,
        "adaptive": adaptive,
        "otsu": otsu,
        "edges": edges,
        "contours": contour_debug,

        "measurements": {
            "count": len(contours),
            "area": area,
            "width": width,
            "height": height,
            "perimeter": perimeter,
        }
    }