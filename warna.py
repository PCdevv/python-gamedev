import cv2
import numpy as np


def get_color_name(rgb):
    colors = {
        "255,0,0": "Merah",
        "0,255,0": "Hijau",
        "0,0,255": "Biru",
        "255,255,0": "Kuning",
        "0,255,255": "Cyan",
        "255,0,255": "Magenta",
        "255,255,255": "Putih",
        "0,0,0": "Hitam"
    }
    key = ",".join([str(x) for x in rgb])
    return colors.get(key, "Warna tidak dikenali")


def detect_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        color_name = get_color_name([r, g, b])
        print("Warna:", color_name)


cv2.namedWindow("Deteksi Warna")
cv2.setMouseCallback("Deteksi Warna", detect_color)

# Ganti dengan nama file gambar yang ingin Anda deteksi warnanya
img = cv2.imread("foto.jpg")

while True:
    cv2.imshow("Deteksi Warna", img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
