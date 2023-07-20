import cv2


def get_color_name(rgb):
    colors = {
        (0, 0, 0): "Hitam",
        (255, 255, 255): "Putih",
        (255, 0, 0): "Merah",
        # Add more color mappings here...
    }

    color_name = colors.get(rgb)
    return color_name if color_name else "Warna tidak dikenali"


def detect_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        color_rgb = (r, g, b)
        print("RGB Code:", color_rgb)


cv2.namedWindow("Deteksi Warna")
cv2.setMouseCallback("Deteksi Warna", detect_color)

# Replace "IGnoe.jpg" with the path to your image file
img = cv2.imread("IGnoe.jpg")

while True:
    cv2.imshow("Deteksi Warna", img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
