import cv2
import numpy as np

def create_binary_image():
    binary_image = np.zeros((300, 300), dtype=np.uint8)

    # 添加多个矩形对象
    binary_image[50:100, 50:100] = 255
    binary_image[50:100, 150:200] = 255
    binary_image[150:200, 50:100] = 255
    binary_image[150:200, 150:200] = 255

    return binary_image

def is_valid_move(binary_image, visited, row, col):
    return (row >= 0) and (row < len(binary_image)) and (col >= 0) and (col < len(binary_image[0])) and \
           (binary_image[row][col] == 255) and (not visited[row][col])

def dfs_iterative(binary_image, visited, row, col):
    stack = [(row, col)]
    min_row, max_row, min_col, max_col = row, row, col, col

    while stack:
        current_row, current_col = stack.pop()

        if not is_valid_move(binary_image, visited, current_row, current_col):
            continue

        visited[current_row][current_col] = True

        min_row, max_row = min(min_row, current_row), max(max_row, current_row)
        min_col, max_col = min(min_col, current_col), max(max_col, current_col)

        row_moves = [-1, 0, 1, 0]
        col_moves = [0, 1, 0, -1]

        for k in range(4):
            new_row = current_row + row_moves[k]
            new_col = current_col + col_moves[k]
            stack.append((new_row, new_col))

    return min_row, max_row, min_col, max_col

def region_labeling(binary_image):
    visited = np.zeros_like(binary_image, dtype=bool)
    object_count = 0
    labeled_image = binary_image.copy()
    labeled_image = cv2.cvtColor(labeled_image, cv2.COLOR_GRAY2BGR)

    for i in range(len(binary_image)):
        for j in range(len(binary_image[0])):
            if binary_image[i][j] == 255 and not visited[i][j]:
                min_row, max_row, min_col, max_col = dfs_iterative(binary_image, visited, i, j)
                object_count += 1
                cv2.rectangle(labeled_image, (min_col, min_row), (max_col, max_row), (0, 255, 0), 2)

    return object_count, labeled_image

def main():
    binary_image = create_binary_image()

    cv2.imshow("Binary Image", binary_image)
    cv2.waitKey(0)

    object_count, labeled_image = region_labeling(binary_image)

    print("Number of objects detected:", object_count)

    cv2.imshow("Labeled Image", labeled_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
