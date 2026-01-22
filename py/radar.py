import pygame
import math
import random

# --- Konfigurasi ---
WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 250
SPEED = 2  # Kecepatan putaran (derajat per frame)
BG_COLOR = (0, 0, 0)
RADAR_COLOR = (0, 255, 0)  # Hijau Neon
FADE_SPEED = 10  # Semakin kecil angka, semakin lama jejak tertinggal (0-255)

# Inisialisasi Pygame  
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Radar Simulation")
clock = pygame.time.Clock()

# Permukaan untuk efek jejak (fading)
fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.set_alpha(FADE_SPEED)
fade_surface.fill(BG_COLOR)

# Generate beberapa "target" acak
targets = []
for _ in range(5):
    tx = random.randint(CENTER[0] - RADIUS + 20, CENTER[0] + RADIUS - 20)
    ty = random.randint(CENTER[1] - RADIUS + 20, CENTER[1] + RADIUS - 20)
    # Pastikan target ada di dalam lingkaran
    dist = math.hypot(tx - CENTER[0], ty - CENTER[1])
    if dist < RADIUS:
        targets.append((tx, ty))

angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Gambar efek fade (menutup frame sebelumnya sedikit demi sedikit)
    screen.blit(fade_surface, (0, 0))

    # 2. Gambar Elemen Statis (Lingkaran Radar)
    pygame.draw.circle(screen, RADAR_COLOR, CENTER, RADIUS, 2)
    pygame.draw.circle(screen, RADAR_COLOR, CENTER, RADIUS // 2, 1) # Lingkaran dalam
    pygame.draw.circle(screen, RADAR_COLOR, CENTER, 5, 0) # Titik tengah

    # 3. Hitung posisi garis pemindai (Sweep Line)
    # Menggunakan matematika trigonometri: 
    # x = r * cos(theta), y = r * sin(theta)
    radians = math.radians(angle)
    end_x = CENTER[0] + RADIUS * math.cos(radians)
    end_y = CENTER[1] + RADIUS * math.sin(radians)

    # 4. Gambar garis pemindai
    pygame.draw.line(screen, RADAR_COLOR, CENTER, (end_x, end_y), 3)

    # 5. Logika Deteksi Target (Blip)
    # Jika garis pemindai dekat dengan target, gambar targetnya lebih terang
    for tx, ty in targets:
        # Hitung sudut target terhadap pusat
        target_angle = math.degrees(math.atan2(ty - CENTER[1], tx - CENTER[0]))
        
        # Normalisasi sudut agar sesuai dengan putaran (0-360)
        if target_angle < 0: target_angle += 360
        current_angle_norm = angle % 360

        # Jika sudut sapuan dekat dengan target (+- 5 derajat)
        diff = abs(current_angle_norm - target_angle)
        if diff < 5:
            # Gambar "Blip" (Target terdeteksi)
            pygame.draw.circle(screen, (255, 255, 255), (tx, ty), 5) # Putih terang
            pygame.draw.circle(screen, RADAR_COLOR, (tx, ty), 8, 1)

    # Update sudut
    angle += SPEED

    # Render
    pygame.display.flip()
    clock.tick(60)

pygame.quit()