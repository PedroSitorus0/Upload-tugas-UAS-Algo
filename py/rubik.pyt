from ursina import *
from panda3d.core import loadPrcFileData

# --- KONFIGURASI DRIVER ---
# Penting agar tidak blank screen di Linux/Fedora
loadPrcFileData('', 'framebuffer-multisample 0')
loadPrcFileData('', 'multisamples 0')

app = Ursina()

# --- SETUP TAMPILAN ---
window.title = 'Rubik 3D Fixed'
window.color = color.dark_gray
# Posisi kamera mundur sedikit
camera.position = (0, 0, -20)
camera.rotation = (0, 0, 0)

# --- INSTRUKSI ---
Text(
    text='[PANAH]: Putar Kamera\n[KLIK KIRI]: Putar Sisi Rubik\n[SHIFT + KLIK]: Putar Balik\n[SPASI]: Reset Kamera',
    position=(-0.85, 0.45),
    color=color.yellow
)

# --- DEFINISI WARNA ---
colors = {
    'white': color.white, 'yellow': color.yellow,
    'blue': color.blue, 'green': color.green,
    'red': color.red, 'orange': color.orange,
    'black': color.black
}

ROTATION_PIVOT = Entity()
cubies = []

# --- FUNGSI MEMBUAT KUBUS ---
def create_cubie(x, y, z):
    # scale=0.92 memberi celah hitam antar kubus
    cubie = Entity(model='cube', color=colors['black'], position=(x, y, z), scale=0.92, unlit=True)
    cubie.collider = 'box' 

    # --- PERBAIKAN STIKER (Menggunakan Plane) ---
    # Kita menggunakan model='plane' yang secara default menghadap ke ATAS (+Y)
    # Jadi kita harus memutarnya agar menghadap ke arah yang benar.
    
    # Sisi Kanan (Merah) -> Putar Z -90 derajat
    if x == 1:  Entity(parent=cubie, model='plane', rotation_z=-90, x=0.501, color=colors['red'], unlit=True)
    # Sisi Kiri (Oranye) -> Putar Z 90 derajat
    if x == -1: Entity(parent=cubie, model='plane', rotation_z=90, x=-0.501, color=colors['orange'], unlit=True)
    
    # Sisi Atas (Kuning) -> Tidak perlu diputar (sudah menghadap Y)
    if y == 1:  Entity(parent=cubie, model='plane', rotation=(0,0,0), y=0.501, color=colors['yellow'], unlit=True)
    # Sisi Bawah (Putih) -> Putar X 180 derajat
    if y == -1: Entity(parent=cubie, model='plane', rotation_x=180, y=-0.501, color=colors['white'], unlit=True)
    
    # Sisi Depan (Hijau) -> Putar X 90 derajat
    if z == 1:  Entity(parent=cubie, model='plane', rotation_x=90, z=0.501, color=colors['green'], unlit=True)
    # Sisi Belakang (Biru) -> Putar X -90 derajat
    if z == -1: Entity(parent=cubie, model='plane', rotation_x=-90, z=-0.501, color=colors['blue'], unlit=True)

    cubies.append(cubie)

# Buat Grid 3x3x3
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            create_cubie(x, y, z)

# --- LOGIKA ROTASI ---
rotation_lock = False

def rotate_side(normal, direction=1):
    global rotation_lock
    if rotation_lock: return
    rotation_lock = True

    # Deteksi sumbu rotasi
    axis = 'x'
    if abs(normal.y) > 0.9: axis = 'y'
    elif abs(normal.z) > 0.9: axis = 'z'

    # Filter kubus yang akan diputar
    target_cubies = []
    for c in cubies:
        if axis == 'x' and round(c.x) == round(normal.x): target_cubies.append(c)
        elif axis == 'y' and round(c.y) == round(normal.y): target_cubies.append(c)
        elif axis == 'z' and round(c.z) == round(normal.z): target_cubies.append(c)
    
    # Parent ke pivot
    for c in target_cubies:
        c.world_parent = ROTATION_PIVOT
    
    # Animasi
    angle = 90 * direction
    duration = 0.4
    if axis == 'x': ROTATION_PIVOT.animate_rotation_x(angle, duration=duration)
    elif axis == 'y': ROTATION_PIVOT.animate_rotation_y(angle, duration=duration)
    elif axis == 'z': ROTATION_PIVOT.animate_rotation_z(angle, duration=duration)
    
    # Reset
    def reset_pivot():
        global rotation_lock
        for c in target_cubies:
            c.world_parent = scene 
        ROTATION_PIVOT.rotation = (0,0,0)
        rotation_lock = False

    invoke(reset_pivot, delay=duration + 0.1)

# --- INPUT KEYBOARD & MOUSE ---
def update():
    # Kamera Keyboard
    speed = 150 * time.dt
    if held_keys['right arrow']: camera.rotation_y -= speed
    if held_keys['left arrow']:  camera.rotation_y += speed
    if held_keys['up arrow']:    camera.rotation_x += speed
    if held_keys['down arrow']:  camera.rotation_x -= speed

def input(key):
    if key == 'space': # Reset
        camera.position = (0, 0, -20)
        camera.rotation = (0, 0, 0)

    # Klik Mouse
    if key == 'left mouse down' and mouse.hovered_entity:
        hit = mouse.hovered_entity
        if hit in cubies:
            direction = -1 if held_keys['shift'] else 1
            rotate_side(mouse.normal, direction)

app.run()