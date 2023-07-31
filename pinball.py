import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 1280
screen_height = 720

# Warna RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Membuat layar
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Bouncing Ball")

# Posisi awal pemain
player_width = 10000
player_height = 20
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height

# Posisi awal bola
ball_radius = 70
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = 50
ball_speed_x = 21
ball_speed_y = 21

# Skor awal
score = 0

# Fungsi untuk menggambar pemain


def draw_player(x, y):
    pygame.draw.rect(screen, red, (x, y, player_width, player_height))

# Fungsi untuk menggambar bola


def draw_ball(x, y):
    pygame.draw.circle(screen, white, (x, y), ball_radius)


# Font untuk skor
font = pygame.font.Font(None, 36)

# Loop utama permainan
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Pergerakan pemain menggunakan keyboard (left and right arrow)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 7
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += 7

    # Gerakan bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bola memantul saat bertabrakan dengan tepi layar
    if ball_x < ball_radius or ball_x > screen_width - ball_radius:
        ball_speed_x = -ball_speed_x

    if ball_y < ball_radius or (player_x < ball_x < player_x + player_width and player_y < ball_y < player_y + player_height):
        ball_speed_y = -ball_speed_y

        # Posisi bola di atas papan merah saat ditangkap
        if player_x < ball_x < player_x + player_width and player_y < ball_y < player_y + player_height:
            ball_y = player_y - ball_radius

            # Tambahkan skor setiap kali bola ditangkap
            score += 1

    # Jika bola jatuh ke bawah layar, game over
    if ball_y > screen_height + ball_radius:
        game_over = True

    # Hapus layar dan gambar elemen-elemen
    screen.fill(black)
    draw_player(player_x, player_y)
    draw_ball(ball_x, ball_y)

    # Tampilkan skor di layar
    score_text = font.render("Skor: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    # Perbarui tampilan
    pygame.display.update()
    clock.tick(60)

# Keluar dari permainan Pygame
pygame.quit()
