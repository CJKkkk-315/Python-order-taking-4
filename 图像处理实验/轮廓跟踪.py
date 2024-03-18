import cv2
import numpy as np

def find_contours(binary_image):
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours, color=(62, 62, 62), thickness=2):
    image_with_contours = np.copy(image)
    for contour in contours:
        cv2.drawContours(image_with_contours, [contour], 0, color, thickness)
    return image_with_contours

def main():
    # 创建一个简单的二值图像
    binary_image = np.zeros((300, 300), dtype=np.uint8)
    binary_image[50:200, 100:200] = 255

    # 寻找轮廓
    contours = find_contours(binary_image)

    # 在原始图像上绘制轮廓
    image_with_contours = draw_contours(binary_image, contours)

    # 显示原始图像和带有轮廓的图像
    cv2.imshow("Binary Image", binary_image)
    cv2.imshow("Image with Contours", image_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
