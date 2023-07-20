import cv2


def get_rgb_code(image_path, x, y):
    # Read the image
    image = cv2.imread(image_path)

    # Get the RGB values of the pixel at coordinates (x, y)
    (blue, green, red) = image[y, x]

    # Return the RGB code as a tuple (R, G, B)
    return (red, green, blue)


# Example usage
image_path = 'foto.jpg'
x_coordinate = 100
y_coordinate = 200

rgb_code = get_rgb_code(image_path, x_coordinate, y_coordinate)
print(f"RGB code at ({x_coordinate}, {y_coordinate}): {rgb_code}")
