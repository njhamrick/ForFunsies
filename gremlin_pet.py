import tkinter as tk
import random
import math
import os

from PIL import Image, ImageTk, ImageEnhance


# =========================================================
# WINDOW
# =========================================================

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
DESK_Y = 445

root = tk.Tk()
root.title("Russian Blue Desktop Pet")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    bg="#d8d2c6",
    highlightthickness=0
)

canvas.pack()


# =========================================================
# BACKGROUND
# =========================================================

# Wall
canvas.create_rectangle(
    0,
    0,
    WINDOW_WIDTH,
    DESK_Y,
    fill="#d8d2c6",
    outline=""
)

# Back edge of desk
canvas.create_rectangle(
    0,
    DESK_Y - 8,
    WINDOW_WIDTH,
    DESK_Y,
    fill="#5c4030",
    outline=""
)

# Desk
canvas.create_rectangle(
    0,
    DESK_Y,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    fill="#8b6548",
    outline=""
)


# =========================================================
# MONSTERA COLORS
# =========================================================

stem_color = "#426a43"

leaf_fill = "#4f8054"
leaf_dark = "#315a38"
leaf_vein = "#77bf7f"

# Same color as wall.
# This makes the cutouts look like holes in the leaves.
cut_color = "#d8d2c6"


# =========================================================
# MONSTERA STEMS
# =========================================================

# Left-most stem
canvas.create_line(
    98, DESK_Y - 62,
    81, DESK_Y - 108,
    59, DESK_Y - 145,
    fill=stem_color,
    width=4,
    smooth=True
)

# Small front / lower-left stem
canvas.create_line(
    101, DESK_Y - 62,
    94, DESK_Y - 96,
    91, DESK_Y - 116,
    fill=stem_color,
    width=4,
    smooth=True
)

# Tall center stem
canvas.create_line(
    103, DESK_Y - 62,
    103, DESK_Y - 140,
    106, DESK_Y - 205,
    fill=stem_color,
    width=5,
    smooth=True
)

# Right-middle stem
canvas.create_line(
    106, DESK_Y - 62,
    119, DESK_Y - 94,
    130, DESK_Y - 119,
    144, DESK_Y - 136,
    fill=stem_color,
    width=5,
    smooth=True
)

# Far-right stem
canvas.create_line(
    109, DESK_Y - 62,
    132, DESK_Y - 105,
    157, DESK_Y - 138,
    181, DESK_Y - 155,
    fill=stem_color,
    width=4,
    smooth=True
)

# =========================================================
# LEAF 1 - CENTER MONSTERA LEAF
# =========================================================

canvas.create_polygon(
    106, DESK_Y - 245,

    92, DESK_Y - 230,
    84, DESK_Y - 205,
    90, DESK_Y - 180,

    106, DESK_Y - 160,

    121, DESK_Y - 180,
    128, DESK_Y - 205,
    120, DESK_Y - 230,

    fill=leaf_fill,
    outline=leaf_dark,
    width=2,
    smooth=True
)

canvas.create_line(
    106,
    DESK_Y - 240,
    106,
    DESK_Y - 165,
    fill=leaf_vein,
    width=2
)

canvas.create_line(
    89,
    DESK_Y - 214,
    100,
    DESK_Y - 207,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_line(
    123,
    DESK_Y - 214,
    112,
    DESK_Y - 207,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_line(
    89,
    DESK_Y - 192,
    100,
    DESK_Y - 188,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_line(
    123,
    DESK_Y - 192,
    112,
    DESK_Y - 188,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_oval(
    98,
    DESK_Y - 224,
    104,
    DESK_Y - 213,
    fill=cut_color,
    outline=""
)

canvas.create_oval(
    108,
    DESK_Y - 224,
    114,
    DESK_Y - 213,
    fill=cut_color,
    outline=""
)


# =========================================================
# LEAF 2 - UPPER LEFT MONSTERA LEAF
# =========================================================

canvas.create_polygon(
    60, DESK_Y - 165,

    45, DESK_Y - 155,
    38, DESK_Y - 138,
    43, DESK_Y - 120,

    58, DESK_Y - 108,

    72, DESK_Y - 120,
    78, DESK_Y - 139,
    73, DESK_Y - 155,

    fill=leaf_fill,
    outline=leaf_dark,
    width=2,
    smooth=True
)

canvas.create_line(
    59,
    DESK_Y - 160,
    58,
    DESK_Y - 111,
    fill=leaf_vein,
    width=2
)

canvas.create_line(
    42,
    DESK_Y - 142,
    53,
    DESK_Y - 136,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_line(
    75,
    DESK_Y - 143,
    65,
    DESK_Y - 136,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_oval(
    56,
    DESK_Y - 151,
    62,
    DESK_Y - 141,
    fill=cut_color,
    outline=""
)


# =========================================================
# LEAF 3 - SMALL FRONT MONSTERA LEAF
# =========================================================

canvas.create_polygon(
    92, DESK_Y - 125,

    80, DESK_Y - 115,
    75, DESK_Y - 98,
    79, DESK_Y - 82,

    91, DESK_Y - 70,

    103, DESK_Y - 82,
    108, DESK_Y - 98,
    103, DESK_Y - 114,

    fill=leaf_fill,
    outline=leaf_dark,
    width=2,
    smooth=True
)

canvas.create_line(
    92,
    DESK_Y - 121,
    91,
    DESK_Y - 73,
    fill=leaf_vein,
    width=2
)

canvas.create_line(
    78,
    DESK_Y - 101,
    87,
    DESK_Y - 96,
    fill=cut_color,
    width=4,
    smooth=True
)

canvas.create_line(
    105,
    DESK_Y - 101,
    96,
    DESK_Y - 96,
    fill=cut_color,
    width=4,
    smooth=True
)

canvas.create_oval(
    89,
    DESK_Y - 112,
    95,
    DESK_Y - 103,
    fill=cut_color,
    outline=""
)


# =========================================================
# LEAF 4 - RIGHT MIDDLE MONSTERA LEAF
# SLIGHT RIGHT TILT
# =========================================================

canvas.create_polygon(
    153, DESK_Y - 164,

    139, DESK_Y - 157,
    130, DESK_Y - 142,
    132, DESK_Y - 124,

    144, DESK_Y - 108,

    159, DESK_Y - 116,
    169, DESK_Y - 132,
    168, DESK_Y - 150,

    fill=leaf_fill,
    outline=leaf_dark,
    width=2,
    smooth=True
)

canvas.create_line(
    152,
    DESK_Y - 160,
    145,
    DESK_Y - 112,
    fill=leaf_vein,
    width=2
)

canvas.create_line(
    135,
    DESK_Y - 148,
    145,
    DESK_Y - 142,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_line(
    166,
    DESK_Y - 145,
    156,
    DESK_Y - 139,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_line(
    131,
    DESK_Y - 132,
    142,
    DESK_Y - 127,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_line(
    164,
    DESK_Y - 129,
    154,
    DESK_Y - 124,
    fill=cut_color,
    width=5,
    smooth=True
)

canvas.create_oval(
    148,
    DESK_Y - 153,
    154,
    DESK_Y - 144,
    fill=cut_color,
    outline=""
)


# =========================================================
# LEAF 5 - FAR RIGHT MONSTERA LEAF
# STRONGLY TILTED RIGHT
#
# IMPORTANT:
# Every piece gets the tag "leaf5".
# That lets us wiggle the entire leaf later.
# =========================================================

canvas.create_polygon(
    215, DESK_Y - 178,

    199, DESK_Y - 181,
    184, DESK_Y - 173,
    176, DESK_Y - 158,

    181, DESK_Y - 145,

    198, DESK_Y - 147,
    213, DESK_Y - 157,
    220, DESK_Y - 169,

    fill=leaf_fill,
    outline=leaf_dark,
    width=2,
    smooth=True,
    tags="leaf5"
)

canvas.create_line(
    212,
    DESK_Y - 176,
    182,
    DESK_Y - 148,
    fill=leaf_vein,
    width=2,
    tags="leaf5"
)

canvas.create_line(
    193,
    DESK_Y - 176,
    201,
    DESK_Y - 168,
    fill=cut_color,
    width=5,
    smooth=True,
    tags="leaf5"
)

canvas.create_line(
    217,
    DESK_Y - 168,
    207,
    DESK_Y - 163,
    fill=cut_color,
    width=5,
    smooth=True,
    tags="leaf_5"
)

canvas.create_line(
    181,
    DESK_Y - 164,
    192,
    DESK_Y - 158,
    fill=cut_color,
    width=5,
    smooth=True,
    tags="leaf5"
)

canvas.create_line(
    209,
    DESK_Y - 156,
    199,
    DESK_Y - 153,
    fill=cut_color,
    width=5,
    smooth=True,
    tags="leaf5"
)

canvas.create_oval(
    198,
    DESK_Y - 174,
    204,
    DESK_Y - 165,
    fill=cut_color,
    outline="",
    tags="leaf5"
)

canvas.create_oval(
    207,
    DESK_Y - 169,
    213,
    DESK_Y - 160,
    fill=cut_color,
    outline="",
    tags="leaf5"
)


# =========================================================
# MONSTERA POT - CORRECT LAYERING
# =========================================================

# ---------------------------------------------------------
# POT SHADOW
# ---------------------------------------------------------

canvas.create_oval(
    62,
    DESK_Y - 3,
    145,
    DESK_Y + 12,
    fill="#6f4d39",
    outline=""
)


# ---------------------------------------------------------
# POT BODY
# ---------------------------------------------------------

canvas.create_polygon(
    73, DESK_Y - 61,
    134, DESK_Y - 61,

    127, DESK_Y,
    81, DESK_Y,

    fill="#a66c49",
    outline="#72462f",
    width=2,
    smooth=True
)


# ---------------------------------------------------------
# POT HIGHLIGHT
# ---------------------------------------------------------

canvas.create_line(
    88,
    DESK_Y - 48,
    85,
    DESK_Y - 18,
    fill="#c98a62",
    width=3
)


# ---------------------------------------------------------
# BACK HALF OF POT RIM
# ---------------------------------------------------------

canvas.create_arc(
    66,
    DESK_Y - 76,
    141,
    DESK_Y - 54,

    start=0,
    extent=180,

    style=tk.PIESLICE,

    fill="#b97952",
    outline="#72462f",
    width=2
)


# ---------------------------------------------------------
# SOIL
# ---------------------------------------------------------

canvas.create_oval(
    73,
    DESK_Y - 70,
    136,
    DESK_Y - 57,
    fill="#443326",
    outline=""
)


# =========================================================
# STEMS
# These are now drawn ON TOP of the soil.
# =========================================================

# Left stem
canvas.create_line(
    98, DESK_Y - 62,
    81, DESK_Y - 108,
    59, DESK_Y - 145,
    fill=stem_color,
    width=4,
    smooth=True
)

# Small front stem
canvas.create_line(
    101, DESK_Y - 62,
    94, DESK_Y - 96,
    91, DESK_Y - 116,
    fill=stem_color,
    width=4,
    smooth=True
)

# Tall center stem
canvas.create_line(
    103, DESK_Y - 62,
    103, DESK_Y - 140,
    106, DESK_Y - 205,
    fill=stem_color,
    width=5,
    smooth=True
)

# Right-middle stem
canvas.create_line(
    106, DESK_Y - 62,
    119, DESK_Y - 94,
    130, DESK_Y - 119,
    144, DESK_Y - 136,
    fill=stem_color,
    width=5,
    smooth=True
)

# Far-right stem
canvas.create_line(
    109, DESK_Y - 62,
    132, DESK_Y - 105,
    157, DESK_Y - 138,
    181, DESK_Y - 155,
    fill=stem_color,
    width=4,
    smooth=True,
    tags="leaf_5_stem"
)


# ---------------------------------------------------------
# FRONT HALF OF POT RIM
#
# This gets drawn LAST so it hides the bottoms
# of the stems and makes them look planted.
# ---------------------------------------------------------

canvas.create_arc(
    66,
    DESK_Y - 76,
    141,
    DESK_Y - 54,

    start=180,
    extent=180,

    style=tk.ARC,

    outline="#72462f",
    width=7
)

# =========================================================
# WORKSTATION
# =========================================================

# Monitor riser
canvas.create_rectangle(
    365,
    390,
    735,
    410,
    fill="#76543d",
    outline="#51392d",
    width=3
)

canvas.create_rectangle(
    385,
    410,
    410,
    DESK_Y,
    fill="#684936",
    outline="#51392d",
    width=2
)

canvas.create_rectangle(
    690,
    410,
    715,
    DESK_Y,
    fill="#684936",
    outline="#51392d",
    width=2
)

# Monitor frame
canvas.create_rectangle(
    420,
    105,
    680,
    300,
    fill="#33383d",
    outline="#25282b",
    width=5
)

# Screen
canvas.create_rectangle(
    435,
    120,
    665,
    285,
    fill="#20262b",
    outline=""
)

# Fake code
canvas.create_line(
    460, 155,
    555, 155,
    fill="#7d91a0",
    width=5
)

canvas.create_line(
    480, 185,
    620, 185,
    fill="#78956f",
    width=5
)

canvas.create_line(
    460, 215,
    590, 215,
    fill="#8b778f",
    width=5
)

canvas.create_line(
    480, 245,
    630, 245,
    fill="#718796",
    width=5
)

# Monitor neck
canvas.create_rectangle(
    535,
    300,
    565,
    365,
    fill="#363b3f",
    outline=""
)

# Rectangular monitor base
canvas.create_rectangle(
    495,
    365,
    605,
    388,
    fill="#363b3f",
    outline="#292d30",
    width=2
)


# =========================================================
# MOUSE
# =========================================================

# Mouse shadow
canvas.create_oval(
    750,
    DESK_Y - 26,
    800,
    DESK_Y + 1,
    fill="#4d3d44",
    outline=""
)

# Mouse
canvas.create_oval(
    752,
    DESK_Y - 34,
    792,
    DESK_Y - 2,
    fill="#555b60",
    outline="#303437",
    width=2
)

canvas.create_line(
    772,
    DESK_Y - 33,
    772,
    DESK_Y - 14,
    fill="#33383b",
    width=2
)

canvas.create_oval(
    769,
    DESK_Y - 27,
    775,
    DESK_Y - 20,
    fill="#858d92",
    outline=""
)


# =========================================================
# SPRITE FILES
# =========================================================

BASE_FOLDER = os.path.dirname(
    os.path.abspath(__file__)
)

sprite_files = {
    "standing": "cat_standing.png",
    "walk_1": "cat_walk_1.png",
    "walk_2": "cat_walk_2.png",
    "sitting": "cat_sitting.png",
    "loaf": "cat_loaf.png",
    "sleeping": "cat_sleeping.png",
    "happy": "cat_happy.png",
    "sideeye": "cat_sideeye.png",
    "paw": "cat_paw.png",
    "grooming": "cat_grooming.png"
}


# =========================================================
# SPRITE SIZES
# =========================================================

sprite_sizes = {
    "standing": (250, 245),
    "walk_1": (270, 245),
    "walk_2": (270, 245),
    "sitting": (225, 255),
    "loaf": (265, 185),
    "sleeping": (265, 185),
    "happy": (225, 255),
    "sideeye": (225, 255),
    "paw": (285, 235),

    # Your adjusted grooming size
    "grooming": (280, 280)
}


# =========================================================
# POSE HEIGHT OFFSETS
# =========================================================

pose_y_offsets = {
    "standing": 0,
    "walking": 0,
    "sitting": 0,
    "happy": 0,
    "sideeye": 0,
    "paw": 0,
    "grooming": 0,

    # Magic anti-levitation number
    "loaf": 42,
    "sleeping": 42
}


# =========================================================
# LOAD SPRITES
# =========================================================

sprites_right = {}
sprites_left = {}


def load_sprite(
    filename,
    max_width,
    max_height
):

    path = os.path.join(
        BASE_FOLDER,
        filename
    )

    if not os.path.exists(path):

        raise FileNotFoundError(
            f"\nMissing sprite:\n{path}\n"
        )

    image = Image.open(
        path
    ).convert("RGBA")

    # Grooming sprite was darker than the others,
    # so brighten ONLY that image by 25%.
    if filename == "cat_grooming.png":

        brightness = ImageEnhance.Brightness(
            image
        )

        image = brightness.enhance(
            1.25
        )

    bbox = image.getbbox()

    if bbox:

        image = image.crop(
            bbox
        )

    image.thumbnail(
        (
            max_width,
            max_height
        ),
        Image.Resampling.LANCZOS
    )

    finished = Image.new(
        "RGBA",
        (
            max_width,
            max_height
        ),
        (
            0,
            0,
            0,
            0
        )
    )

    x = (
        max_width
        - image.width
    ) // 2

    y = (
        max_height
        - image.height
    )

    finished.paste(
        image,
        (
            x,
            y
        ),
        image
    )

    return finished


for sprite_name, filename in sprite_files.items():

    width, height = sprite_sizes[
        sprite_name
    ]

    right_image = load_sprite(
        filename,
        width,
        height
    )

    left_image = right_image.transpose(
        Image.Transpose.FLIP_LEFT_RIGHT
    )

    sprites_right[
        sprite_name
    ] = ImageTk.PhotoImage(
        right_image
    )

    sprites_left[
        sprite_name
    ] = ImageTk.PhotoImage(
        left_image
    )


# =========================================================
# CAT VARIABLES
# =========================================================

cat_x = 350
cat_ground_y = DESK_Y + 5

cat_direction = 1
cat_pose = "standing"

walk_frame = 1

action_in_progress = False

click_count = 0

scheduled_action_id = None
pose_timer_id = None

speech_items = []


# =========================================================
# CAT SHADOW
# =========================================================

cat_shadow = canvas.create_oval(
    cat_x - 70,
    DESK_Y - 5,
    cat_x + 70,
    DESK_Y + 14,
    fill="#684a38",
    outline=""
)


# =========================================================
# CAT IMAGE
# =========================================================

cat_image_item = canvas.create_image(
    cat_x,
    cat_ground_y,
    anchor="s"
)


# =========================================================
# CURRENT SPRITE
# =========================================================

def get_current_sprite():

    if cat_pose == "walking":

        if walk_frame == 1:
            sprite_name = "walk_1"

        else:
            sprite_name = "walk_2"

    else:

        sprite_name = cat_pose

    if cat_direction == 1:

        return sprites_right[
            sprite_name
        ]

    return sprites_left[
        sprite_name
    ]


# =========================================================
# DRAW CAT
# =========================================================

def draw_cat():

    sprite = get_current_sprite()

    y_offset = pose_y_offsets.get(
        cat_pose,
        0
    )

    canvas.itemconfig(
        cat_image_item,
        image=sprite
    )

    canvas.coords(
        cat_image_item,
        cat_x,
        cat_ground_y + y_offset
    )

    if cat_pose in [
        "loaf",
        "sleeping"
    ]:

        shadow_width = 90

    elif cat_pose in [
        "sitting",
        "happy",
        "sideeye",
        "grooming"
    ]:

        shadow_width = 65

    else:

        shadow_width = 74

    canvas.coords(
        cat_shadow,
        cat_x - shadow_width,
        DESK_Y - 5,
        cat_x + shadow_width,
        DESK_Y + 14
    )

    canvas.tag_raise(
        cat_image_item
    )


# =========================================================
# WATER BOTTLE
# =========================================================

bottle_x = 950
bottle_y = DESK_Y

bottle_angle = 0
bottle_knocked = False

bottle_parts = []

water_spill = None


def rotate_point(
    x,
    y,
    angle
):

    radians = math.radians(
        angle
    )

    new_x = (
        x * math.cos(radians)
        - y * math.sin(radians)
    )

    new_y = (
        x * math.sin(radians)
        + y * math.cos(radians)
    )

    return new_x, new_y


def draw_bottle():

    global bottle_parts

    for item in bottle_parts:

        canvas.delete(
            item
        )

    bottle_parts = []

    width = 30
    height = 78

    body_points = [
        (-width / 2, 0),
        (width / 2, 0),

        (width / 2, -55),

        (10, -66),

        (10, -height),
        (-10, -height),

        (-10, -66),

        (-width / 2, -55)
    ]

    rotated = []

    for x, y in body_points:

        rx, ry = rotate_point(
            x,
            y,
            bottle_angle
        )

        rotated.extend([
            bottle_x + rx,
            bottle_y + ry
        ])

    body = canvas.create_polygon(
        rotated,
        fill="#75b1d0",
        outline="#416d84",
        width=2
    )

    cap_points = [
        (-10, -height),
        (10, -height),
        (10, -height - 9),
        (-10, -height - 9)
    ]

    cap_rotated = []

    for x, y in cap_points:

        rx, ry = rotate_point(
            x,
            y,
            bottle_angle
        )

        cap_rotated.extend([
            bottle_x + rx,
            bottle_y + ry
        ])

    cap = canvas.create_polygon(
        cap_rotated,
        fill="#436f86",
        outline=""
    )

    shine_start = rotate_point(
        -6,
        -58,
        bottle_angle
    )

    shine_end = rotate_point(
        -6,
        -25,
        bottle_angle
    )

    shine = canvas.create_line(
        bottle_x + shine_start[0],
        bottle_y + shine_start[1],
        bottle_x + shine_end[0],
        bottle_y + shine_end[1],
        fill="#c1e4f4",
        width=3
    )

    bottle_parts.extend([
        body,
        cap,
        shine
    ])

    for item in bottle_parts:

        canvas.tag_raise(
            item
        )


# =========================================================
# SPEECH
# =========================================================

random_comments = [
    "Meow",
    "Meow",
    "I'm bored"
]


def remove_speech():

    global speech_items

    for item in speech_items:

        canvas.delete(
            item
        )

    speech_items = []


def show_speech(
    message,
    duration=2300
):

    global speech_items

    remove_speech()

    bubble_x = max(
        125,
        min(
            WINDOW_WIDTH - 125,
            cat_x
        )
    )

    bubble_y = DESK_Y - 270

    shadow = canvas.create_oval(
        bubble_x - 105,
        bubble_y - 29,
        bubble_x + 105,
        bubble_y + 35,
        fill="#aaa49b",
        outline=""
    )

    bubble = canvas.create_oval(
        bubble_x - 105,
        bubble_y - 34,
        bubble_x + 105,
        bubble_y + 30,
        fill="#faf9f5",
        outline="#555b60",
        width=2
    )

    tail = canvas.create_polygon(
        bubble_x - 12,
        bubble_y + 27,

        bubble_x + 7,
        bubble_y + 27,

        bubble_x - 2,
        bubble_y + 44,

        fill="#faf9f5",
        outline="#555b60"
    )

    text = canvas.create_text(
        bubble_x,
        bubble_y - 2,
        text=message,
        font=(
            "Segoe UI",
            13,
            "bold"
        ),
        fill="#33383b"
    )

    speech_items = [
        shadow,
        bubble,
        tail,
        text
    ]

    root.after(
        duration,
        remove_speech
    )


# =========================================================
# TIMER HELPERS
# =========================================================

def cancel_pose_timer():

    global pose_timer_id

    if pose_timer_id is not None:

        try:

            root.after_cancel(
                pose_timer_id
            )

        except tk.TclError:

            pass

        pose_timer_id = None


# =========================================================
# WALKING
# =========================================================

def walk_to(
    target_x,
    speed=6,
    delay=60,
    on_done=None
):

    global action_in_progress
    global cat_pose
    global cat_direction
    global cat_x
    global walk_frame

    cancel_pose_timer()

    action_in_progress = True
    cat_pose = "walking"

    if target_x > cat_x:

        cat_direction = 1

    else:

        cat_direction = -1

    def step():

        global cat_x
        global walk_frame
        global action_in_progress
        global cat_pose

        distance = (
            target_x - cat_x
        )

        if abs(distance) <= speed:

            cat_x = target_x

            cat_pose = "standing"

            walk_frame = 1

            action_in_progress = False

            draw_cat()

            if on_done is not None:

                on_done()

            else:

                schedule_next_action()

            return

        if distance > 0:

            cat_x += speed

        else:

            cat_x -= speed

        if walk_frame == 1:

            walk_frame = 2

        else:

            walk_frame = 1

        draw_cat()

        root.after(
            delay,
            step
        )

    step()


def random_walk():

    target = cat_x + random.randint(
        -260,
        260
    )

    target = max(
        170,
        min(
            WINDOW_WIDTH - 130,
            target
        )
    )

    walk_to(
        target
    )


# =========================================================
# NORMAL POSES
# =========================================================

def hold_pose(
    pose,
    minimum,
    maximum
):

    global cat_pose
    global action_in_progress
    global pose_timer_id

    cancel_pose_timer()

    action_in_progress = True

    cat_pose = pose

    draw_cat()

    pose_timer_id = root.after(
        random.randint(
            minimum,
            maximum
        ),
        finish_pose
    )


def finish_pose():

    global cat_pose
    global action_in_progress
    global pose_timer_id

    pose_timer_id = None

    cat_pose = "standing"

    action_in_progress = False

    draw_cat()

    schedule_next_action()


def sit():

    hold_pose(
        "sitting",
        3000,
        6500
    )


def loaf():

    show_speech(
        "*Yawn*"
    )

    hold_pose(
        "loaf",
        4500,
        8500
    )


def sleep():

    show_speech(
        "*Yawn*"
    )

    hold_pose(
        "sleeping",
        7000,
        13000
    )


# =========================================================
# GROOMING
# =========================================================

def groom():

    global cat_pose
    global action_in_progress

    action_in_progress = True

    cat_pose = "sitting"

    draw_cat()

    root.after(
        800,
        start_grooming
    )


def start_grooming():

    global cat_pose

    cat_pose = "grooming"

    draw_cat()

    root.after(
        random.randint(
            2500,
            4500
        ),
        finish_grooming
    )


def finish_grooming():

    global cat_pose

    cat_pose = "sitting"

    draw_cat()

    root.after(
        1000,
        leave_grooming
    )


def leave_grooming():

    global cat_pose
    global action_in_progress

    cat_pose = "standing"

    action_in_progress = False

    draw_cat()

    schedule_next_action(
        random.randint(
            1800,
            3500
        )
    )


# =========================================================
# SLOW BLINK
# =========================================================

def slow_blink():

    global cat_pose
    global action_in_progress

    action_in_progress = True

    cat_pose = "happy"

    draw_cat()

    root.after(
        1100,
        finish_slow_blink
    )


def finish_slow_blink():

    global cat_pose

    cat_pose = "sitting"

    draw_cat()

    root.after(
        1700,
        finish_pose
    )

# =========================================================
# PLANT INTERACTION
# =========================================================

def investigate_plant():

    walk_to(
        255,
        speed=5,
        delay=60,
        on_done=inspect_plant
    )


def inspect_plant():

    global cat_pose
    global cat_direction
    global action_in_progress

    action_in_progress = True

    # Face toward plant
    cat_direction = -1

    # Sit and stare at it first
    cat_pose = "sitting"

    draw_cat()

    root.after(
        1200,
        prepare_to_smack_plant
    )


def prepare_to_smack_plant():

    global cat_pose

    # Paw comes out
    cat_pose = "paw"

    draw_cat()

    root.after(
        500,
        smack_plant
    )


def smack_plant():

    wiggle_leaf5()

    root.after(
        900,
        after_plant_smack
    )


# =========================================================
# LEAF 5 + STEM WIGGLE
# =========================================================

def wiggle_leaf5():

    # Horizontal movement pattern.
    # Positive = right
    # Negative = left
    wiggle_positions = [
        0,
        7,
        -8,
        6,
        -5,
        3,
        -2,
        0
    ]

    current_position = 0

    def wiggle_step(index=0):

        nonlocal current_position

        if index >= len(wiggle_positions):
            return

        target_position = wiggle_positions[index]

        movement = (
            target_position
            - current_position
        )

        # Move the entire leaf
        canvas.move(
            "leaf5",
            movement,
            0
        )

        # Move the stem too,
        # but only about half as much
        # so it looks like bending
        canvas.move(
            "leaf5_stem",
            movement * 0.45,
            0
        )

        current_position = target_position

        root.after(
            90,
            lambda: wiggle_step(
                index + 1
            )
        )

    wiggle_step()


# =========================================================
# AFTER FIRST SMACK
# =========================================================

def after_plant_smack():

    global cat_pose

    # Sit there looking suspicious
    cat_pose = "sideeye"

    draw_cat()

    # 40% chance she decides to smack it again
    if random.random() < 0.40:

        root.after(
            900,
            second_plant_smack
        )

    else:

        root.after(
            1400,
            finish_plant_crime
        )


# =========================================================
# SECOND SMACK
# =========================================================

def second_plant_smack():

    global cat_pose

    cat_pose = "paw"

    draw_cat()

    root.after(
        400,
        second_leaf_hit
    )


def second_leaf_hit():

    wiggle_leaf5()

    root.after(
        900,
        plant_crime_sideeye
    )


def plant_crime_sideeye():

    global cat_pose

    cat_pose = "sideeye"

    draw_cat()

    root.after(
        1200,
        finish_plant_crime
    )


# =========================================================
# FINISH PLANT INTERACTION
# =========================================================

def finish_plant_crime():

    global cat_pose
    global action_in_progress

    cat_pose = "standing"

    action_in_progress = False

    draw_cat()

    schedule_next_action(
        random.randint(
            1800,
            3500
        )
    )

# =========================================================
# MONITOR BLOCKING
# =========================================================

def block_monitor():

    walk_to(
        550,
        speed=5,
        delay=60,
        on_done=sit_in_front_of_monitor
    )


def sit_in_front_of_monitor():

    global cat_pose
    global action_in_progress

    action_in_progress = True

    cat_pose = "sitting"

    draw_cat()

    if random.random() < 0.40:

        root.after(
            900,
            lambda: show_speech(
                "Meow"
            )
        )

    root.after(
        random.randint(
            4500,
            8000
        ),
        finish_monitor_block
    )


def finish_monitor_block():

    global cat_pose
    global action_in_progress

    cat_pose = "standing"

    action_in_progress = False

    draw_cat()

    schedule_next_action()


# =========================================================
# ZOOMIES
# =========================================================

def zoomies():

    global action_in_progress
    global cat_pose
    global cat_direction
    global cat_x
    global walk_frame

    action_in_progress = True

    cat_pose = "walking"

    if cat_x < WINDOW_WIDTH / 2:

        cat_direction = 1

    else:

        cat_direction = -1

    total_steps = random.randint(
        55,
        75
    )

    def zoom_step(
        step_number=0
    ):

        global cat_x
        global cat_direction
        global walk_frame
        global cat_pose
        global action_in_progress

        if step_number >= total_steps:

            cat_pose = "standing"

            action_in_progress = False

            draw_cat()

            schedule_next_action(
                random.randint(
                    1500,
                    3000
                )
            )

            return

        cat_x += (
            cat_direction
            * 15
        )

        if cat_x > WINDOW_WIDTH - 130:

            cat_x = WINDOW_WIDTH - 130

            cat_direction = -1

        elif cat_x < 170:

            cat_x = 170

            cat_direction = 1

        if walk_frame == 1:

            walk_frame = 2

        else:

            walk_frame = 1

        draw_cat()

        root.after(
            30,
            lambda: zoom_step(
                step_number + 1
            )
        )

    zoom_step()


# =========================================================
# WATER BOTTLE CRIME
# =========================================================

def go_to_bottle():

    if bottle_knocked:

        schedule_next_action()

        return

    walk_to(
        bottle_x - 135,
        speed=5,
        delay=55,
        on_done=inspect_bottle
    )


def inspect_bottle():

    global cat_pose
    global cat_direction
    global action_in_progress

    action_in_progress = True

    cat_direction = 1

    cat_pose = "sideeye"

    draw_cat()

    root.after(
        1500,
        first_bottle_tap
    )


def first_bottle_tap():

    global cat_pose

    cat_pose = "paw"

    draw_cat()

    root.after(
        500,
        bottle_hesitation
    )


def bottle_hesitation():

    global cat_pose

    cat_pose = "sideeye"

    draw_cat()

    root.after(
        800,
        second_bottle_tap
    )


def second_bottle_tap():

    global cat_pose

    cat_pose = "paw"

    draw_cat()

    root.after(
        450,
        knock_bottle
    )


def knock_bottle():

    global bottle_angle
    global bottle_knocked

    bottle_knocked = True

    def tip():

        global bottle_angle

        if bottle_angle >= 90:

            bottle_angle = 90

            draw_bottle()

            make_water_spill()

            root.after(
                350,
                after_bottle_crime
            )

            return

        bottle_angle += 8

        draw_bottle()

        root.after(
            45,
            tip
        )

    tip()


# =========================================================
# WATER DROPLETS / SPILL
# =========================================================

def make_water_spill():

    global water_spill

    if water_spill is not None:

        for item in water_spill:

            canvas.delete(
                item
            )

    water_spill = []

    puddle = canvas.create_polygon(
        bottle_x - 5, DESK_Y + 6,
        bottle_x + 18, DESK_Y + 2,
        bottle_x + 45, DESK_Y + 5,
        bottle_x + 70, DESK_Y + 10,
        bottle_x + 55, DESK_Y + 15,
        bottle_x + 25, DESK_Y + 14,
        bottle_x + 2, DESK_Y + 11,

        fill="#78b9d4",
        outline="#5ea2bf",
        width=1
    )

    drop1 = canvas.create_oval(
        bottle_x + 72,
        DESK_Y + 8,
        bottle_x + 79,
        DESK_Y + 14,
        fill="#78b9d4",
        outline=""
    )

    drop2 = canvas.create_oval(
        bottle_x + 84,
        DESK_Y + 11,
        bottle_x + 89,
        DESK_Y + 15,
        fill="#78b9d4",
        outline=""
    )

    water_spill.extend([
        puddle,
        drop1,
        drop2
    ])

    # Bottle stays visible above water.
    for item in bottle_parts:

        canvas.tag_raise(
            item
        )


def after_bottle_crime():

    global cat_pose
    global action_in_progress

    cat_pose = "sideeye"

    action_in_progress = False

    draw_cat()

    show_speech(
        "Drink some water",
        3000
    )

    root.after(
        8500,
        reset_bottle
    )

    schedule_next_action(
        4200
    )


def reset_bottle():

    global bottle_angle
    global bottle_knocked
    global water_spill

    bottle_angle = 0

    bottle_knocked = False

    if water_spill is not None:

        for item in water_spill:

            canvas.delete(
                item
            )

        water_spill = None

    draw_bottle()


# =========================================================
# RANDOM BEHAVIOR
# =========================================================

def choose_action():

    if action_in_progress:

        return

    actions = [
        "walk",
        "walk",
        "walk",
        "walk",

        "sit",
        "sit",

        "loaf",

        "sleep",

        "groom",
        "groom",

        "speak",
        "speak",

        "blink",
        "blink",

        "plant",
        "plant",

        "monitor",

        "zoomies"
    ]

    if not bottle_knocked:

        actions.extend([
            "bottle",
            "bottle"
        ])

    action = random.choice(
        actions
    )

    if action == "walk":

        random_walk()

    elif action == "sit":

        sit()

    elif action == "loaf":

        loaf()

    elif action == "sleep":

        sleep()

    elif action == "groom":

        groom()

    elif action == "blink":

        slow_blink()

    elif action == "plant":

        investigate_plant()

    elif action == "monitor":

        block_monitor()

    elif action == "zoomies":

        zoomies()

    elif action == "bottle":

        go_to_bottle()

    elif action == "speak":

        message = random.choice(
            random_comments
        )

        show_speech(
            message
        )

        if (
            message == "I'm bored"
            and random.random() < 0.50
        ):

            root.after(
                2500,
                zoomies
            )

        else:

            schedule_next_action(
                random.randint(
                    2800,
                    4800
                )
            )


# =========================================================
# SCHEDULER
# =========================================================

def schedule_next_action(
    delay=None
):

    global scheduled_action_id

    if scheduled_action_id is not None:

        try:

            root.after_cancel(
                scheduled_action_id
            )

        except tk.TclError:

            pass

    if delay is None:

        delay = random.randint(
            2000,
            5000
        )

    scheduled_action_id = root.after(
        delay,
        choose_action
    )


# =========================================================
# HAPPY PETTING POSE
# =========================================================

def happy_pet_pose():

    global cat_pose

    old_pose = cat_pose

    if old_pose != "walking":

        cat_pose = "happy"

        draw_cat()

        def restore():

            global cat_pose

            if cat_pose == "happy":

                if old_pose in [
                    "standing",
                    "sitting",
                    "loaf"
                ]:

                    cat_pose = old_pose

                else:

                    cat_pose = "standing"

                draw_cat()

        root.after(
            1300,
            restore
        )


# =========================================================
# CLICK / PET CAT
# =========================================================

def cat_clicked(event):

    global click_count
    global cat_pose
    global action_in_progress

    if (
        cat_x - 135
        < event.x
        < cat_x + 135

        and

        DESK_Y - 280
        < event.y
        < DESK_Y + 30
    ):

        # Wake sleeping cat
        if cat_pose == "sleeping":

            cancel_pose_timer()

            cat_pose = "sitting"

            action_in_progress = False

            draw_cat()

            show_speech(
                "Meow"
            )

            schedule_next_action(
                3000
            )

            return

        click_count += 1

        happy_pet_pose()

        if click_count == 1:

            show_speech(
                "*Purr*"
            )

        elif click_count == 2:

            show_speech(
                random.choice([
                    "*Purr*",
                    "Mmm, more pets"
                ])
            )

        elif click_count == 3:

            show_speech(
                "Mmm, more pets"
            )

        elif click_count <= 5:

            show_speech(
                random.choice([
                    "*Purr*",
                    "Mmm, more pets"
                ])
            )

        else:

            click_count = 0

            show_speech(
                "Meow"
            )

            if not action_in_progress:

                if cat_x < WINDOW_WIDTH / 2:

                    target = (
                        cat_x + 220
                    )

                else:

                    target = (
                        cat_x - 220
                    )

                target = max(
                    170,
                    min(
                        WINDOW_WIDTH - 130,
                        target
                    )
                )

                root.after(
                    700,
                    lambda: walk_to(
                        target,
                        speed=8,
                        delay=40
                    )
                )


# =========================================================
# START
# =========================================================

canvas.bind(
    "<Button-1>",
    cat_clicked
)

draw_bottle()

draw_cat()

schedule_next_action(
    1500
)

root.mainloop()