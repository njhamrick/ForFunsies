import pygame
import random
import math

pygame.init()

# =========================================================
# WINDOW SETTINGS
# =========================================================

WIDTH = 600

GAME_HEIGHT = 400
HUD_HEIGHT = 70
HEIGHT = GAME_HEIGHT + HUD_HEIGHT

SIZE = 20
GAME_SPEED = 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gremlin Worm: Dungeon Loot")

clock = pygame.time.Clock()


# =========================================================
# COLORS
# =========================================================

BLACK = (0, 0, 0)
WHITE = (240, 240, 240)

# Dungeon floor
FLOOR_1 = (21, 20, 24)
FLOOR_2 = (27, 26, 31)
FLOOR_LINE = (38, 37, 43)
FLOOR_CRACK = (46, 44, 50)

# Dungeon walls
STONE_1 = (86, 82, 78)
STONE_2 = (72, 69, 67)
STONE_3 = (98, 93, 87)
STONE_LIGHT = (130, 124, 115)
STONE_DARK = (40, 38, 39)
MORTAR = (25, 24, 27)

# Moss
MOSS = (55, 84, 46)
MOSS_LIGHT = (80, 112, 59)

# Gremlin
GREEN = (46, 205, 77)
GREEN_DARK = (20, 108, 44)
GREEN_LIGHT = (98, 245, 119)
GREMLIN_EYE = (255, 231, 90)
GREMLIN_OUTLINE = (10, 55, 24)

# Food
RED = (220, 44, 52)
RED_DARK = (125, 23, 29)

GOLD = (255, 211, 45)
ORANGE = (215, 121, 18)

PURPLE = (171, 66, 230)
PURPLE_DARK = (88, 30, 135)
PINK = (250, 118, 218)

CURSED_BLUE = (62, 177, 255)
CURSED_DARK = (18, 47, 91)
CURSED_GLOW = (101, 220, 255)

# Dungeon decorations
WOOD = (104, 62, 35)
METAL = (85, 82, 82)

FIRE_RED = (225, 56, 18)
FIRE_ORANGE = (255, 133, 16)
FIRE_YELLOW = (255, 226, 74)

BONE = (190, 181, 155)
BONE_DARK = (120, 111, 91)

CHAIN = (85, 86, 91)
COIN = (211, 164, 40)

# Door
DOOR_WOOD = (82, 49, 30)
DOOR_DARK = (45, 28, 20)
DOOR_GLOW = (100, 255, 140)

# HUD
HUD_BACKGROUND = (12, 12, 15)
HUD_BORDER = (75, 72, 77)
HUD_MUTED = (160, 160, 170)


# =========================================================
# DOOR
# =========================================================

DOOR_RECT = pygame.Rect(
    WIDTH - 40,
    GAME_HEIGHT // 2 - 30,
    40,
    60
)


# =========================================================
# LEVELS
# =========================================================

LEVELS = [

    # -----------------------------------------------------
    # LEVEL 1
    # -----------------------------------------------------

    {
        "name": "CRYPT ENTRANCE",
        "goal": 10,

        "walls": [
            pygame.Rect(100, 80, 140, 20),
            pygame.Rect(380, 80, 20, 120),
            pygame.Rect(180, 280, 160, 20),
            pygame.Rect(460, 260, 100, 20)
        ],

        "torches": [
            (125, 68),
            (390, 115),
            (245, 268),
            (510, 248)
        ],

        "skulls": [
            (55, 95),
            (430, 330)
        ],

        "bones": [
            (72, 245),
            (350, 65)
        ],

        "treasure": [
            (145, 340)
        ],

        "chains": [
            (340, 0, 60)
        ]
    },


    # -----------------------------------------------------
    # LEVEL 2
    # -----------------------------------------------------

    {
        "name": "BONE HALLS",
        "goal": 20,

        "walls": [
            pygame.Rect(60, 60, 160, 20),
            pygame.Rect(60, 60, 20, 120),

            pygame.Rect(260, 100, 20, 140),

            pygame.Rect(360, 60, 140, 20),

            pygame.Rect(420, 140, 20, 120),

            pygame.Rect(120, 300, 180, 20),

            pygame.Rect(340, 320, 160, 20)
        ],

        "torches": [
            (120, 48),
            (270, 150),
            (430, 180),
            (420, 308)
        ],

        "skulls": [
            (100, 220),
            (320, 75),
            (515, 110)
        ],

        "bones": [
            (210, 260),
            (350, 270),
            (510, 350)
        ],

        "treasure": [
            (170, 215),
            (470, 290)
        ],

        "chains": [
            (230, 0, 75),
            (530, 0, 55)
        ]
    },


    # -----------------------------------------------------
    # LEVEL 3
    # -----------------------------------------------------

    {
        "name": "CURSED VAULT",
        "goal": 30,

        "walls": [
            pygame.Rect(80, 60, 20, 180),
            pygame.Rect(80, 60, 140, 20),

            pygame.Rect(180, 120, 20, 120),

            pygame.Rect(260, 60, 160, 20),

            pygame.Rect(380, 120, 20, 160),

            pygame.Rect(460, 80, 20, 120),

            pygame.Rect(100, 300, 180, 20),

            pygame.Rect(320, 320, 180, 20)
        ],

        "torches": [
            (90, 110),
            (190, 165),
            (390, 180),
            (470, 125)
        ],

        "skulls": [
            (45, 350),
            (240, 260),
            (520, 70)
        ],

        "bones": [
            (145, 255),
            (340, 105),
            (510, 280)
        ],

        "treasure": [
            (230, 90),
            (445, 285),
            (525, 350)
        ],

        "chains": [
            (230, 0, 60),
            (540, 0, 85)
        ]
    }
]


# =========================================================
# CURRENT LEVEL
# =========================================================

current_level = 0

walls = []
torches = []
skulls = []
bone_piles = []
treasure_piles = []
chains = []


def load_level(level_number):

    global walls
    global torches
    global skulls
    global bone_piles
    global treasure_piles
    global chains

    level = LEVELS[level_number]

    walls = level["walls"]
    torches = level["torches"]
    skulls = level["skulls"]
    bone_piles = level["bones"]
    treasure_piles = level["treasure"]
    chains = level["chains"]


load_level(current_level)


# =========================================================
# COBWEBS
# =========================================================

cobwebs = [
    (0, 0),
    (WIDTH - 40, 0),
    (0, GAME_HEIGHT - 40),
    (WIDTH - 40, GAME_HEIGHT - 40)
]


# =========================================================
# FLOOR DETAILS
#
# Generated once so they stay still.
# =========================================================

random.seed(8)

floor_pebbles = []

for _ in range(50):

    floor_pebbles.append(
        (
            random.randint(5, WIDTH - 5),
            random.randint(5, GAME_HEIGHT - 5),
            random.randint(1, 2)
        )
    )

random.seed()


# =========================================================
# FONTS
# =========================================================

font = pygame.font.SysFont(
    "consolas",
    22,
    bold=True
)

small_font = pygame.font.SysFont(
    "consolas",
    15,
    bold=True
)

tiny_font = pygame.font.SysFont(
    "consolas",
    12
)

big_font = pygame.font.SysFont(
    "consolas",
    46,
    bold=True
)

level_font = pygame.font.SysFont(
    "consolas",
    32,
    bold=True
)


# =========================================================
# RESET WORM
# =========================================================

def reset_worm():

    x = 300
    y = 200

    dx = 0
    dy = 0

    worm = [
        [300, 200],
        [280, 200],
        [260, 200],
        [240, 200],
        [220, 200]
    ]

    growth_remaining = 0

    return (
        x,
        y,
        dx,
        dy,
        worm,
        growth_remaining
    )


(
    x,
    y,
    dx,
    dy,
    worm,
    growth_remaining
) = reset_worm()


# =========================================================
# SCORE
# =========================================================

# Total score through all levels
score = 0

# Loot collected on current level
level_loot = 0


# =========================================================
# SAFE SPAWN LOCATION
# =========================================================

def safe_location(item_x, item_y):

    item_rect = pygame.Rect(
        item_x,
        item_y,
        SIZE,
        SIZE
    )

    # Don't spawn in walls
    for wall in walls:

        if item_rect.colliderect(wall):
            return False

    # Don't spawn in doorway
    if item_rect.colliderect(DOOR_RECT):
        return False

    # Don't spawn on worm
    if [item_x, item_y] in worm:
        return False

    return True


# =========================================================
# NORMAL FOOD
# =========================================================

def make_food():

    while True:

        food_x = random.randrange(
            0,
            WIDTH,
            SIZE
        )

        food_y = random.randrange(
            0,
            GAME_HEIGHT,
            SIZE
        )

        if safe_location(
            food_x,
            food_y
        ):

            return (
                food_x,
                food_y
            )


food_x, food_y = make_food()


# =========================================================
# RARE FOOD SETTINGS
# =========================================================

rare_active = False

rare_x = 0
rare_y = 0

rare_type = None
rare_points = 0

RARE_DURATION = 4000

rare_spawn_time = 0

next_rare_time = (
    pygame.time.get_ticks()
    + random.randint(
        6000,
        12000
    )
)


# =========================================================
# CHOOSE RARE FOOD
# =========================================================

def choose_rare_food():

    roll = random.randint(
        1,
        100
    )

    # 65% chance
    if roll <= 65:

        return (
            "gold",
            5
        )

    # 30% chance
    elif roll <= 95:

        return (
            "purple",
            10
        )

    # 5% chance
    else:

        return (
            "cursed",
            25
        )


# =========================================================
# MAKE RARE FOOD
# =========================================================

def make_rare_food():

    while True:

        rare_x = random.randrange(
            0,
            WIDTH,
            SIZE
        )

        rare_y = random.randrange(
            0,
            GAME_HEIGHT,
            SIZE
        )

        if (
            safe_location(
                rare_x,
                rare_y
            )

            and

            [rare_x, rare_y]
            !=
            [food_x, food_y]
        ):

            return (
                rare_x,
                rare_y
            )


# =========================================================
# DRAW FLOOR
# =========================================================

def draw_floor(surface):

    # ONLY draw over the dungeon area
    pygame.draw.rect(
        surface,
        FLOOR_1,
        (
            0,
            0,
            WIDTH,
            GAME_HEIGHT
        )
    )

    tile_size = 40

    for row, tile_y in enumerate(
        range(
            0,
            GAME_HEIGHT,
            tile_size
        )
    ):

        for column, tile_x in enumerate(
            range(
                0,
                WIDTH,
                tile_size
            )
        ):

            if (
                row + column
            ) % 2 == 0:

                color = FLOOR_1

            else:

                color = FLOOR_2

            pygame.draw.rect(
                surface,
                color,
                (
                    tile_x,
                    tile_y,
                    tile_size,
                    tile_size
                )
            )

    # Vertical tile lines
    for tile_x in range(
        0,
        WIDTH,
        tile_size
    ):

        pygame.draw.line(
            surface,
            FLOOR_LINE,
            (
                tile_x,
                0
            ),
            (
                tile_x,
                GAME_HEIGHT
            ),
            1
        )

    # Horizontal tile lines
    for tile_y in range(
        0,
        GAME_HEIGHT,
        tile_size
    ):

        pygame.draw.line(
            surface,
            FLOOR_LINE,
            (
                0,
                tile_y
            ),
            (
                WIDTH,
                tile_y
            ),
            1
        )

    # Pebbles
    for (
        pebble_x,
        pebble_y,
        radius
    ) in floor_pebbles:

        pygame.draw.circle(
            surface,
            FLOOR_CRACK,
            (
                pebble_x,
                pebble_y
            ),
            radius
        )

    # Larger cracks
    cracks = [
        (55, 145),
        (280, 55),
        (415, 235),
        (88, 325),
        (345, 350),
        (530, 135)
    ]

    for crack_x, crack_y in cracks:

        pygame.draw.line(
            surface,
            FLOOR_CRACK,
            (
                crack_x,
                crack_y
            ),
            (
                crack_x + 8,
                crack_y + 4
            ),
            2
        )

        pygame.draw.line(
            surface,
            FLOOR_CRACK,
            (
                crack_x + 8,
                crack_y + 4
            ),
            (
                crack_x + 4,
                crack_y + 10
            ),
            1
        )


# =========================================================
# DRAW DUNGEON WALL
# =========================================================

def draw_dungeon_wall(
    surface,
    wall
):

    # Wall shadow
    pygame.draw.rect(
        surface,
        (8, 8, 10),
        (
            wall.x + 4,
            wall.y + 5,
            wall.width,
            wall.height
        )
    )

    brick_size = 20

    rows = max(
        1,
        wall.height // brick_size
    )

    columns = max(
        1,
        wall.width // brick_size
    )

    for row in range(rows):

        for column in range(columns):

            brick_x = (
                wall.x
                + column * brick_size
            )

            brick_y = (
                wall.y
                + row * brick_size
            )

            shade = (
                row
                + column
                + wall.x // 20
            ) % 3

            if shade == 0:

                stone = STONE_1

            elif shade == 1:

                stone = STONE_2

            else:

                stone = STONE_3

            brick = pygame.Rect(
                brick_x,
                brick_y,
                20,
                20
            )

            pygame.draw.rect(
                surface,
                stone,
                brick
            )

            pygame.draw.rect(
                surface,
                MORTAR,
                brick,
                2
            )

            # Highlight
            pygame.draw.line(
                surface,
                STONE_LIGHT,
                (
                    brick_x + 3,
                    brick_y + 3
                ),
                (
                    brick_x + 16,
                    brick_y + 3
                ),
                1
            )

            # Shadow
            pygame.draw.line(
                surface,
                STONE_DARK,
                (
                    brick_x + 2,
                    brick_y + 17
                ),
                (
                    brick_x + 17,
                    brick_y + 17
                ),
                2
            )

            # Cracks
            if (
                row
                + column
                + wall.y // 20
            ) % 5 == 0:

                pygame.draw.line(
                    surface,
                    STONE_DARK,
                    (
                        brick_x + 7,
                        brick_y + 5
                    ),
                    (
                        brick_x + 11,
                        brick_y + 10
                    ),
                    1
                )

                pygame.draw.line(
                    surface,
                    STONE_DARK,
                    (
                        brick_x + 11,
                        brick_y + 10
                    ),
                    (
                        brick_x + 8,
                        brick_y + 15
                    ),
                    1
                )

            # Moss
            if (
                row
                + column
                + wall.x // 20
            ) % 7 == 0:

                pygame.draw.line(
                    surface,
                    MOSS,
                    (
                        brick_x + 2,
                        brick_y + 4
                    ),
                    (
                        brick_x + 10,
                        brick_y + 4
                    ),
                    3
                )

                pygame.draw.circle(
                    surface,
                    MOSS_LIGHT,
                    (
                        brick_x + 5,
                        brick_y + 5
                    ),
                    2
                )


# =========================================================
# DRAW TORCH
# =========================================================

def draw_torch(
    surface,
    torch_x,
    torch_y,
    current_time
):

    flicker = int(
        math.sin(
            current_time / 75
            + torch_x
        ) * 2
    )

    # Glow
    glow = pygame.Surface(
        (70, 70),
        pygame.SRCALPHA
    )

    pygame.draw.circle(
        glow,
        (
            255,
            155,
            35,
            20
        ),
        (
            35,
            35
        ),
        30
    )

    surface.blit(
        glow,
        (
            torch_x - 35,
            torch_y - 35
        )
    )

    # Handle
    pygame.draw.rect(
        surface,
        WOOD,
        (
            torch_x - 2,
            torch_y + 5,
            5,
            17
        )
    )

    # Outer flame
    pygame.draw.polygon(
        surface,
        FIRE_RED,
        [
            (
                torch_x - 8,
                torch_y + 5
            ),

            (
                torch_x,
                torch_y - 14 - flicker
            ),

            (
                torch_x + 8,
                torch_y + 5
            )
        ]
    )

    # Middle flame
    pygame.draw.polygon(
        surface,
        FIRE_ORANGE,
        [
            (
                torch_x - 5,
                torch_y + 3
            ),

            (
                torch_x + 1,
                torch_y - 10 + flicker
            ),

            (
                torch_x + 5,
                torch_y + 3
            )
        ]
    )

    # Inner flame
    pygame.draw.polygon(
        surface,
        FIRE_YELLOW,
        [
            (
                torch_x - 2,
                torch_y + 2
            ),

            (
                torch_x,
                torch_y - 6 - flicker
            ),

            (
                torch_x + 3,
                torch_y + 2
            )
        ]
    )


# =========================================================
# DRAW COBWEB
# =========================================================

def draw_cobweb(
    surface,
    x,
    y
):

    color = (
        105,
        105,
        115
    )

    direction_x = (
        1
        if x < WIDTH // 2
        else -1
    )

    direction_y = (
        1
        if y < GAME_HEIGHT // 2
        else -1
    )

    center = (
        x,
        y
    )

    pygame.draw.line(
        surface,
        color,
        center,
        (
            x + 35 * direction_x,
            y
        ),
        1
    )

    pygame.draw.line(
        surface,
        color,
        center,
        (
            x,
            y + 35 * direction_y
        ),
        1
    )

    pygame.draw.line(
        surface,
        color,
        center,
        (
            x + 28 * direction_x,
            y + 28 * direction_y
        ),
        1
    )

    for radius in [
        10,
        20,
        30
    ]:

        points = [

            (
                x + radius * direction_x,
                y
            ),

            (
                x + int(radius * .7) * direction_x,
                y + int(radius * .7) * direction_y
            ),

            (
                x,
                y + radius * direction_y
            )
        ]

        pygame.draw.lines(
            surface,
            color,
            False,
            points,
            1
        )


# =========================================================
# DRAW SKULL
# =========================================================

def draw_skull(
    surface,
    x,
    y
):

    pygame.draw.circle(
        surface,
        BONE,
        (
            x,
            y
        ),
        8
    )

    pygame.draw.rect(
        surface,
        BONE,
        (
            x - 5,
            y + 4,
            10,
            7
        )
    )

    # Eye sockets
    pygame.draw.circle(
        surface,
        STONE_DARK,
        (
            x - 3,
            y - 1
        ),
        2
    )

    pygame.draw.circle(
        surface,
        STONE_DARK,
        (
            x + 3,
            y - 1
        ),
        2
    )

    # Nose
    pygame.draw.polygon(
        surface,
        STONE_DARK,
        [
            (
                x,
                y + 2
            ),

            (
                x - 2,
                y + 5
            ),

            (
                x + 2,
                y + 5
            )
        ]
    )

    # Teeth
    pygame.draw.line(
        surface,
        BONE_DARK,
        (
            x - 4,
            y + 7
        ),
        (
            x + 4,
            y + 7
        ),
        1
    )


# =========================================================
# DRAW BONES
# =========================================================

def draw_bones(
    surface,
    x,
    y
):

    pygame.draw.line(
        surface,
        BONE,
        (
            x - 8,
            y - 5
        ),
        (
            x + 9,
            y + 6
        ),
        4
    )

    pygame.draw.line(
        surface,
        BONE,
        (
            x + 8,
            y - 6
        ),
        (
            x - 8,
            y + 7
        ),
        4
    )

    for bx, by in [

        (
            x - 9,
            y - 6
        ),

        (
            x + 10,
            y + 7
        ),

        (
            x + 9,
            y - 7
        ),

        (
            x - 9,
            y + 8
        )
    ]:

        pygame.draw.circle(
            surface,
            BONE,
            (
                bx,
                by
            ),
            3
        )


# =========================================================
# DRAW TREASURE
# =========================================================

def draw_treasure(
    surface,
    x,
    y
):

    # Shadow
    pygame.draw.ellipse(
        surface,
        (
            8,
            8,
            8
        ),
        (
            x - 14,
            y + 5,
            30,
            8
        )
    )

    coins = [
        (-8, 3),
        (-3, 0),
        (3, 3),
        (8, 0),
        (0, -4)
    ]

    for (
        offset_x,
        offset_y
    ) in coins:

        pygame.draw.circle(
            surface,
            COIN,
            (
                x + offset_x,
                y + offset_y
            ),
            4
        )

        pygame.draw.circle(
            surface,
            GOLD,
            (
                x + offset_x - 1,
                y + offset_y - 1
            ),
            1
        )

    # Gem
    pygame.draw.polygon(
        surface,
        PURPLE,
        [
            (
                x + 11,
                y - 6
            ),

            (
                x + 15,
                y - 2
            ),

            (
                x + 11,
                y + 3
            ),

            (
                x + 7,
                y - 2
            )
        ]
    )


# =========================================================
# DRAW CHAIN
# =========================================================

def draw_chain(
    surface,
    x,
    y,
    length
):

    for offset in range(
        0,
        length,
        8
    ):

        pygame.draw.ellipse(
            surface,
            CHAIN,
            (
                x - 3,
                y + offset,
                7,
                10
            ),
            2
        )


# =========================================================
# DRAW DOOR
# =========================================================

def draw_door(
    surface,
    door_open,
    current_time
):

    x = DOOR_RECT.x
    y = DOOR_RECT.y

    # Stone doorway frame
    pygame.draw.rect(
        surface,
        STONE_DARK,
        (
            x - 6,
            y - 7,
            46,
            74
        )
    )

    pygame.draw.rect(
        surface,
        STONE_1,
        (
            x - 3,
            y - 4,
            43,
            68
        ),
        3
    )


    # -----------------------------------------------------
    # OPEN DOOR
    # -----------------------------------------------------

    if door_open:

        pulse = int(
            abs(
                math.sin(
                    current_time / 150
                )
            ) * 4
        )

        glow = pygame.Surface(
            (
                80,
                100
            ),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            glow,
            (
                80,
                255,
                130,
                18
            ),
            (
                10 - pulse,
                10 - pulse,
                50 + pulse * 2,
                80 + pulse * 2
            ),
            border_radius=12
        )

        surface.blit(
            glow,
            (
                x - 20,
                y - 20
            )
        )

        pygame.draw.rect(
            surface,
            (
                5,
                15,
                10
            ),
            DOOR_RECT
        )

        pygame.draw.rect(
            surface,
            DOOR_GLOW,
            DOOR_RECT,
            3
        )

        open_text = tiny_font.render(
            "OPEN",
            True,
            DOOR_GLOW
        )

        surface.blit(
            open_text,
            open_text.get_rect(
                center=(
                    x + 20,
                    y + 30
                )
            )
        )


    # -----------------------------------------------------
    # LOCKED DOOR
    # -----------------------------------------------------

    else:

        pygame.draw.rect(
            surface,
            DOOR_DARK,
            DOOR_RECT
        )

        # Wooden planks
        for plank_y in range(
            y,
            y + 60,
            15
        ):

            pygame.draw.rect(
                surface,
                DOOR_WOOD,
                (
                    x,
                    plank_y,
                    40,
                    13
                )
            )

        pygame.draw.rect(
            surface,
            (
                35,
                20,
                15
            ),
            DOOR_RECT,
            3
        )

        # Chains
        pygame.draw.line(
            surface,
            CHAIN,
            (
                x + 3,
                y + 10
            ),
            (
                x + 37,
                y + 50
            ),
            3
        )

        pygame.draw.line(
            surface,
            CHAIN,
            (
                x + 37,
                y + 10
            ),
            (
                x + 3,
                y + 50
            ),
            3
        )

        # Lock
        pygame.draw.rect(
            surface,
            GOLD,
            (
                x + 14,
                y + 25,
                12,
                12
            )
        )

        pygame.draw.circle(
            surface,
            BLACK,
            (
                x + 20,
                y + 30
            ),
            2
        )


# =========================================================
# DRAW NORMAL APPLE
# =========================================================

def draw_normal_food(
    surface,
    food_x,
    food_y
):

    center_x = food_x + 10
    center_y = food_y + 10

    # Shadow
    pygame.draw.ellipse(
        surface,
        (
            7,
            7,
            7
        ),
        (
            food_x + 2,
            food_y + 15,
            17,
            5
        )
    )

    # Dark apple outline
    pygame.draw.circle(
        surface,
        RED_DARK,
        (
            center_x,
            center_y + 1
        ),
        10
    )

    # Apple
    pygame.draw.circle(
        surface,
        RED,
        (
            center_x,
            center_y
        ),
        8
    )

    # Shine
    pygame.draw.circle(
        surface,
        (
            255,
            135,
            140
        ),
        (
            center_x - 3,
            center_y - 3
        ),
        2
    )

    # Stem
    pygame.draw.line(
        surface,
        WOOD,
        (
            center_x,
            food_y + 3
        ),
        (
            center_x + 1,
            food_y
        ),
        2
    )

    # Leaf
    pygame.draw.ellipse(
        surface,
        MOSS_LIGHT,
        (
            center_x + 1,
            food_y,
            7,
            4
        )
    )


# =========================================================
# DRAW GOLD FRUIT
# =========================================================

def draw_gold_fruit(
    surface,
    fruit_x,
    fruit_y,
    current_time
):

    cx = fruit_x + 10
    cy = fruit_y + 10

    pulse = int(
        abs(
            math.sin(
                current_time / 180
            )
        ) * 2
    )

    pygame.draw.circle(
        surface,
        ORANGE,
        (
            cx,
            cy
        ),
        11
    )

    pygame.draw.circle(
        surface,
        GOLD,
        (
            cx,
            cy
        ),
        8
    )

    pygame.draw.circle(
        surface,
        WHITE,
        (
            cx - 3,
            cy - 3
        ),
        2
    )

    distance = (
        13 + pulse
    )

    # Sparkle
    pygame.draw.line(
        surface,
        GOLD,
        (
            cx,
            cy - distance
        ),
        (
            cx,
            cy - distance + 4
        ),
        1
    )

    pygame.draw.line(
        surface,
        GOLD,
        (
            cx - distance,
            cy
        ),
        (
            cx - distance + 4,
            cy
        ),
        1
    )


# =========================================================
# DRAW PURPLE FRUIT
# =========================================================

def draw_purple_fruit(
    surface,
    fruit_x,
    fruit_y,
    current_time
):

    cx = fruit_x + 10
    cy = fruit_y + 10

    pulse = int(
        abs(
            math.sin(
                current_time / 150
            )
        ) * 2
    )

    pygame.draw.circle(
        surface,
        PURPLE_DARK,
        (
            cx,
            cy
        ),
        11 + pulse,
        1
    )

    pygame.draw.circle(
        surface,
        PURPLE,
        (
            cx,
            cy
        ),
        8
    )

    pygame.draw.circle(
        surface,
        PINK,
        (
            cx,
            cy
        ),
        4
    )

    pygame.draw.circle(
        surface,
        WHITE,
        (
            cx - 3,
            cy - 3
        ),
        1
    )


# =========================================================
# DRAW CURSED FRUIT
# =========================================================

def draw_cursed_fruit(
    surface,
    fruit_x,
    fruit_y,
    current_time
):

    cx = fruit_x + 10
    cy = fruit_y + 10

    pulse = int(
        2
        + abs(
            math.sin(
                current_time / 120
            )
        ) * 4
    )

    # Glow
    pygame.draw.circle(
        surface,
        CURSED_GLOW,
        (
            cx,
            cy
        ),
        11 + pulse,
        1
    )

    # Dark outline
    pygame.draw.circle(
        surface,
        CURSED_DARK,
        (
            cx,
            cy
        ),
        10
    )

    # Fruit
    pygame.draw.circle(
        surface,
        CURSED_BLUE,
        (
            cx,
            cy
        ),
        8
    )

    # X
    pygame.draw.line(
        surface,
        WHITE,
        (
            cx - 4,
            cy - 4
        ),
        (
            cx + 4,
            cy + 4
        ),
        2
    )

    pygame.draw.line(
        surface,
        WHITE,
        (
            cx + 4,
            cy - 4
        ),
        (
            cx - 4,
            cy + 4
        ),
        2
    )


# =========================================================
# DRAW GREMLIN WORM
# =========================================================

def draw_worm(
    surface,
    worm,
    dx,
    dy
):

    worm_length = len(worm)


    # -----------------------------------------------------
    # BODY
    # -----------------------------------------------------

    for index in range(
        worm_length - 1,
        0,
        -1
    ):

        segment = worm[index]

        cx = (
            segment[0]
            + SIZE // 2
        )

        cy = (
            segment[1]
            + SIZE // 2
        )

        # Tail gets darker
        if (
            index / worm_length
        ) > .65:

            body_color = GREEN_DARK

        else:

            body_color = GREEN

        # Shadow
        pygame.draw.circle(
            surface,
            (
                7,
                7,
                8
            ),
            (
                cx + 2,
                cy + 3
            ),
            10
        )

        # Outline
        pygame.draw.circle(
            surface,
            GREMLIN_OUTLINE,
            (
                cx,
                cy
            ),
            10
        )

        # Segment
        pygame.draw.circle(
            surface,
            body_color,
            (
                cx,
                cy
            ),
            8
        )

        # Highlight
        pygame.draw.circle(
            surface,
            GREEN_LIGHT,
            (
                cx - 3,
                cy - 3
            ),
            2
        )


    # -----------------------------------------------------
    # HEAD
    # -----------------------------------------------------

    head_x = worm[0][0]
    head_y = worm[0][1]

    cx = head_x + 10
    cy = head_y + 10


    # Head shadow
    pygame.draw.circle(
        surface,
        (
            5,
            5,
            6
        ),
        (
            cx + 2,
            cy + 3
        ),
        12
    )


    # Ears
    pygame.draw.polygon(
        surface,
        GREEN_DARK,
        [
            (
                cx - 7,
                cy - 4
            ),

            (
                cx - 15,
                cy - 9
            ),

            (
                cx - 8,
                cy + 2
            )
        ]
    )

    pygame.draw.polygon(
        surface,
        GREEN_DARK,
        [
            (
                cx + 7,
                cy - 4
            ),

            (
                cx + 15,
                cy - 9
            ),

            (
                cx + 8,
                cy + 2
            )
        ]
    )


    # Head outline
    pygame.draw.circle(
        surface,
        GREMLIN_OUTLINE,
        (
            cx,
            cy
        ),
        11
    )

    # Head
    pygame.draw.circle(
        surface,
        GREEN,
        (
            cx,
            cy
        ),
        9
    )


    # Angry eyebrows
    pygame.draw.line(
        surface,
        GREEN_DARK,
        (
            cx - 7,
            cy - 6
        ),
        (
            cx - 1,
            cy - 4
        ),
        2
    )

    pygame.draw.line(
        surface,
        GREEN_DARK,
        (
            cx + 7,
            cy - 6
        ),
        (
            cx + 1,
            cy - 4
        ),
        2
    )


    # -----------------------------------------------------
    # EYE DIRECTION
    # -----------------------------------------------------

    eye_move_x = 0
    eye_move_y = 0

    if dx > 0:
        eye_move_x = 2

    elif dx < 0:
        eye_move_x = -2

    elif dy > 0:
        eye_move_y = 2

    elif dy < 0:
        eye_move_y = -2


    left_eye = (
        cx - 4,
        cy - 2
    )

    right_eye = (
        cx + 4,
        cy - 2
    )


    pygame.draw.circle(
        surface,
        GREMLIN_EYE,
        left_eye,
        3
    )

    pygame.draw.circle(
        surface,
        GREMLIN_EYE,
        right_eye,
        3
    )


    pygame.draw.circle(
        surface,
        BLACK,
        (
            left_eye[0] + eye_move_x,
            left_eye[1] + eye_move_y
        ),
        1
    )

    pygame.draw.circle(
        surface,
        BLACK,
        (
            right_eye[0] + eye_move_x,
            right_eye[1] + eye_move_y
        ),
        1
    )


    # Tiny fangs
    pygame.draw.polygon(
        surface,
        WHITE,
        [
            (
                cx - 4,
                cy + 4
            ),

            (
                cx - 2,
                cy + 4
            ),

            (
                cx - 3,
                cy + 7
            )
        ]
    )

    pygame.draw.polygon(
        surface,
        WHITE,
        [
            (
                cx + 2,
                cy + 4
            ),

            (
                cx + 4,
                cy + 4
            ),

            (
                cx + 3,
                cy + 7
            )
        ]
    )


# =========================================================
# DRAW HUD
# =========================================================

def draw_hud(
    surface,
    score,
    level_loot,
    level_goal,
    current_level,
    worm_length,
    door_open,
    rare_active,
    rare_type
):

    # HUD background
    pygame.draw.rect(
        surface,
        HUD_BACKGROUND,
        (
            0,
            GAME_HEIGHT,
            WIDTH,
            HUD_HEIGHT
        )
    )

    # Stone divider
    pygame.draw.line(
        surface,
        HUD_BORDER,
        (
            0,
            GAME_HEIGHT
        ),
        (
            WIDTH,
            GAME_HEIGHT
        ),
        3
    )


    # -----------------------------------------------------
    # LOOT
    # -----------------------------------------------------

    loot_text = font.render(
        f"LOOT: {score}",
        True,
        GOLD
    )

    surface.blit(
        loot_text,
        (
            15,
            GAME_HEIGHT + 8
        )
    )


    # -----------------------------------------------------
    # LEVEL
    # -----------------------------------------------------

    level_text = tiny_font.render(
        f"LEVEL {current_level + 1}: "
        f"{LEVELS[current_level]['name']}",
        True,
        WHITE
    )

    surface.blit(
        level_text,
        (
            15,
            GAME_HEIGHT + 42
        )
    )


    # -----------------------------------------------------
    # GREMLIN LENGTH
    # -----------------------------------------------------

    length_text = small_font.render(
        f"LENGTH: {worm_length}",
        True,
        GREEN_LIGHT
    )

    surface.blit(
        length_text,
        (
            215,
            GAME_HEIGHT + 12
        )
    )


    controls_text = tiny_font.render(
        "ARROW KEYS: MOVE",
        True,
        HUD_MUTED
    )

    surface.blit(
        controls_text,
        (
            215,
            GAME_HEIGHT + 43
        )
    )


    # -----------------------------------------------------
    # DOOR STATUS
    # -----------------------------------------------------

    if door_open:

        door_text = small_font.render(
            "DOOR OPEN!",
            True,
            DOOR_GLOW
        )

    else:

        door_text = small_font.render(
            f"DOOR: {level_loot}/{level_goal}",
            True,
            GOLD
        )

    door_rect = door_text.get_rect(
        topright=(
            WIDTH - 12,
            GAME_HEIGHT + 10
        )
    )

    surface.blit(
        door_text,
        door_rect
    )


    # -----------------------------------------------------
    # RARE FOOD STATUS
    # -----------------------------------------------------

    if rare_active:

        if rare_type == "gold":

            message = "GOLD FRUIT +5"
            color = GOLD

        elif rare_type == "purple":

            message = "PURPLE FRUIT +10"
            color = PURPLE

        else:

            message = "CURSED +25 / +5 LENGTH"
            color = CURSED_BLUE

    else:

        message = "STEAL LOOT // DON'T BONK"
        color = HUD_MUTED


    rare_text = tiny_font.render(
        message,
        True,
        color
    )

    rare_rect = rare_text.get_rect(
        bottomright=(
            WIDTH - 12,
            HEIGHT - 10
        )
    )

    surface.blit(
        rare_text,
        rare_rect
    )


# =========================================================
# GAME VARIABLES
# =========================================================

running = True

game_over = False

victory = False

death_reason = ""

level_banner_end = (
    pygame.time.get_ticks()
    + 2500
)


# =========================================================
# GAME LOOP
# =========================================================

while running:

    current_time = (
        pygame.time.get_ticks()
    )

    level = LEVELS[
        current_level
    ]

    level_goal = level[
        "goal"
    ]

    door_open = (
        level_loot
        >=
        level_goal
    )


    # =====================================================
    # EVENTS
    # =====================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        if event.type == pygame.KEYDOWN:


            # -------------------------------------------------
            # GAME OVER / VICTORY CONTROLS
            # -------------------------------------------------

            if game_over or victory:

                if event.key == pygame.K_r:

                    current_level = 0

                    load_level(
                        current_level
                    )

                    (
                        x,
                        y,
                        dx,
                        dy,
                        worm,
                        growth_remaining
                    ) = reset_worm()

                    score = 0
                    level_loot = 0

                    food_x, food_y = (
                        make_food()
                    )

                    rare_active = False
                    rare_type = None

                    game_over = False
                    victory = False

                    death_reason = ""

                    level_banner_end = (
                        current_time
                        + 2500
                    )

                    next_rare_time = (
                        current_time
                        + random.randint(
                            6000,
                            12000
                        )
                    )


                elif event.key == pygame.K_q:

                    running = False


            # -------------------------------------------------
            # MOVEMENT
            # -------------------------------------------------

            else:

                if (
                    event.key == pygame.K_UP
                    and dy == 0
                ):

                    dx = 0
                    dy = -SIZE


                elif (
                    event.key == pygame.K_DOWN
                    and dy == 0
                ):

                    dx = 0
                    dy = SIZE


                elif (
                    event.key == pygame.K_LEFT
                    and dx == 0
                ):

                    dx = -SIZE
                    dy = 0


                elif (
                    event.key == pygame.K_RIGHT
                    and dx == 0
                ):

                    dx = SIZE
                    dy = 0


    # =====================================================
    # RARE FOOD TIMER
    # =====================================================

    if (
        not game_over
        and
        not victory
    ):

        # Spawn rare fruit
        if (
            not rare_active
            and
            current_time
            >=
            next_rare_time
        ):

            rare_x, rare_y = (
                make_rare_food()
            )

            (
                rare_type,
                rare_points
            ) = choose_rare_food()

            rare_active = True

            rare_spawn_time = (
                current_time
            )


        # Remove rare fruit after time expires
        if rare_active:

            if (
                current_time
                - rare_spawn_time
                >=
                RARE_DURATION
            ):

                rare_active = False
                rare_type = None

                next_rare_time = (
                    current_time
                    + random.randint(
                        6000,
                        12000
                    )
                )


    # =====================================================
    # MOVE WORM
    # =====================================================

    if (
        not game_over
        and
        not victory
    ):

        if (
            dx != 0
            or
            dy != 0
        ):

            x += dx
            y += dy


            # -------------------------------------------------
            # SCREEN WRAPPING
            #
            # IMPORTANT:
            # Only wrap inside GAME_HEIGHT.
            # The gremlin cannot enter the HUD.
            # -------------------------------------------------

            if x >= WIDTH:

                x = 0

            elif x < 0:

                x = WIDTH - SIZE


            if y >= GAME_HEIGHT:

                y = 0

            elif y < 0:

                y = GAME_HEIGHT - SIZE


            # Add new head
            worm.insert(
                0,
                [
                    x,
                    y
                ]
            )


            # -------------------------------------------------
            # NORMAL FOOD
            # -------------------------------------------------

            if (
                x == food_x
                and
                y == food_y
            ):

                score += 1

                level_loot += 1

                growth_remaining += 1

                food_x, food_y = (
                    make_food()
                )


            # -------------------------------------------------
            # RARE FOOD
            # -------------------------------------------------

            if (
                rare_active
                and
                x == rare_x
                and
                y == rare_y
            ):

                score += rare_points

                level_loot += rare_points


                if rare_type == "gold":

                    growth_remaining += 1


                elif rare_type == "purple":

                    growth_remaining += 1


                elif rare_type == "cursed":

                    growth_remaining += 5


                rare_active = False

                rare_type = None

                next_rare_time = (
                    current_time
                    + random.randint(
                        6000,
                        12000
                    )
                )


            # -------------------------------------------------
            # GROWTH
            # -------------------------------------------------

            if growth_remaining > 0:

                growth_remaining -= 1

            else:

                worm.pop()


            # Head rectangle
            head_rect = pygame.Rect(
                x,
                y,
                SIZE,
                SIZE
            )

            transitioned = False


            # -------------------------------------------------
            # ENTER OPEN DOOR
            # -------------------------------------------------

            if (
                door_open
                and
                head_rect.colliderect(
                    DOOR_RECT
                )
            ):


                # ---------------------------------------------
                # FINAL LEVEL COMPLETE
                # ---------------------------------------------

                if (
                    current_level
                    ==
                    len(LEVELS) - 1
                ):

                    victory = True

                    dx = 0
                    dy = 0


                # ---------------------------------------------
                # NEXT LEVEL
                # ---------------------------------------------

                else:

                    current_level += 1

                    load_level(
                        current_level
                    )

                    (
                        x,
                        y,
                        dx,
                        dy,
                        worm,
                        growth_remaining
                    ) = reset_worm()

                    level_loot = 0

                    food_x, food_y = (
                        make_food()
                    )

                    rare_active = False

                    rare_type = None

                    next_rare_time = (
                        current_time
                        + random.randint(
                            6000,
                            12000
                        )
                    )

                    level_banner_end = (
                        current_time
                        + 2500
                    )

                    transitioned = True


            # -------------------------------------------------
            # COLLISIONS
            # -------------------------------------------------

            if (
                not transitioned
                and
                not victory
            ):


                # Wall collision
                for wall in walls:

                    if head_rect.colliderect(
                        wall
                    ):

                        game_over = True

                        death_reason = (
                            "BONKED INTO A DUNGEON WALL"
                        )


                # Self collision
                if worm[0] in worm[1:]:

                    game_over = True

                    death_reason = (
                        "THE GREMLIN ATE ITS OWN TAIL"
                    )


    # =====================================================
    # DRAW DUNGEON
    # =====================================================

    draw_floor(
        screen
    )


    # =====================================================
    # DECORATIONS
    # =====================================================

    for web_x, web_y in cobwebs:

        draw_cobweb(
            screen,
            web_x,
            web_y
        )


    for (
        chain_x,
        chain_y,
        chain_length
    ) in chains:

        draw_chain(
            screen,
            chain_x,
            chain_y,
            chain_length
        )


    for skull_x, skull_y in skulls:

        draw_skull(
            screen,
            skull_x,
            skull_y
        )


    for bones_x, bones_y in bone_piles:

        draw_bones(
            screen,
            bones_x,
            bones_y
        )


    for treasure_x, treasure_y in treasure_piles:

        draw_treasure(
            screen,
            treasure_x,
            treasure_y
        )


    # =====================================================
    # WALLS
    # =====================================================

    for wall in walls:

        draw_dungeon_wall(
            screen,
            wall
        )


    # =====================================================
    # TORCHES
    # =====================================================

    for (
        torch_x,
        torch_y
    ) in torches:

        draw_torch(
            screen,
            torch_x,
            torch_y,
            current_time
        )


    # =====================================================
    # DOOR
    # =====================================================

    draw_door(
        screen,
        door_open,
        current_time
    )


    # =====================================================
    # FOOD
    # =====================================================

    draw_normal_food(
        screen,
        food_x,
        food_y
    )


    if rare_active:

        if rare_type == "gold":

            draw_gold_fruit(
                screen,
                rare_x,
                rare_y,
                current_time
            )


        elif rare_type == "purple":

            draw_purple_fruit(
                screen,
                rare_x,
                rare_y,
                current_time
            )


        elif rare_type == "cursed":

            draw_cursed_fruit(
                screen,
                rare_x,
                rare_y,
                current_time
            )


    # =====================================================
    # GREMLIN
    # =====================================================

    draw_worm(
        screen,
        worm,
        dx,
        dy
    )


    # =====================================================
    # BOTTOM HUD
    #
    # Nothing in here covers the dungeon anymore.
    # =====================================================

    draw_hud(
        screen,
        score,
        level_loot,
        level_goal,
        current_level,
        len(worm),
        door_open,
        rare_active,
        rare_type
    )


    # =====================================================
    # LEVEL INTRO BANNER
    # =====================================================

    if (
        current_time
        <
        level_banner_end
        and
        not game_over
        and
        not victory
    ):

        banner = pygame.Surface(
            (
                400,
                80
            ),
            pygame.SRCALPHA
        )

        banner.fill(
            (
                0,
                0,
                0,
                185
            )
        )

        banner_x = (
            WIDTH // 2
            - 200
        )

        banner_y = 150

        screen.blit(
            banner,
            (
                banner_x,
                banner_y
            )
        )


        level_number_text = tiny_font.render(
            f"DUNGEON LEVEL {current_level + 1}",
            True,
            GOLD
        )

        level_name_text = level_font.render(
            LEVELS[current_level]["name"],
            True,
            WHITE
        )


        screen.blit(
            level_number_text,
            level_number_text.get_rect(
                center=(
                    WIDTH // 2,
                    168
                )
            )
        )

        screen.blit(
            level_name_text,
            level_name_text.get_rect(
                center=(
                    WIDTH // 2,
                    198
                )
            )
        )


    # =====================================================
    # GAME OVER SCREEN
    # =====================================================

    if game_over:

        overlay = pygame.Surface(
            (
                WIDTH,
                HEIGHT
            ),
            pygame.SRCALPHA
        )

        overlay.fill(
            (
                0,
                0,
                0,
                205
            )
        )

        screen.blit(
            overlay,
            (
                0,
                0
            )
        )


        panel = pygame.Rect(
            105,
            100,
            390,
            235
        )

        pygame.draw.rect(
            screen,
            (
                23,
                20,
                24
            ),
            panel,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            STONE_1,
            panel,
            3,
            border_radius=10
        )


        death_text = big_font.render(
            "YOU DIED",
            True,
            RED
        )

        reason_text = tiny_font.render(
            death_reason,
            True,
            (
                180,
                180,
                185
            )
        )

        final_score = font.render(
            f"LOOT STOLEN: {score}",
            True,
            GOLD
        )

        final_length = tiny_font.render(
            f"FINAL GREMLIN LENGTH: {len(worm)}",
            True,
            GREEN_LIGHT
        )

        restart_text = small_font.render(
            "[ R ] RETURN TO DUNGEON",
            True,
            WHITE
        )

        quit_text = small_font.render(
            "[ Q ] FLEE IN SHAME",
            True,
            (
                150,
                150,
                155
            )
        )


        screen.blit(
            death_text,
            death_text.get_rect(
                center=(
                    WIDTH // 2,
                    140
                )
            )
        )

        screen.blit(
            reason_text,
            reason_text.get_rect(
                center=(
                    WIDTH // 2,
                    185
                )
            )
        )

        screen.blit(
            final_score,
            final_score.get_rect(
                center=(
                    WIDTH // 2,
                    220
                )
            )
        )

        screen.blit(
            final_length,
            final_length.get_rect(
                center=(
                    WIDTH // 2,
                    250
                )
            )
        )

        screen.blit(
            restart_text,
            restart_text.get_rect(
                center=(
                    WIDTH // 2,
                    290
                )
            )
        )

        screen.blit(
            quit_text,
            quit_text.get_rect(
                center=(
                    WIDTH // 2,
                    315
                )
            )
        )


    # =====================================================
    # VICTORY SCREEN
    # =====================================================

    if victory:

        overlay = pygame.Surface(
            (
                WIDTH,
                HEIGHT
            ),
            pygame.SRCALPHA
        )

        overlay.fill(
            (
                0,
                0,
                0,
                215
            )
        )

        screen.blit(
            overlay,
            (
                0,
                0
            )
        )


        victory_text = level_font.render(
            "DUNGEON CLEARED",
            True,
            GOLD
        )

        gremlin_text = small_font.render(
            "THE GREMLIN ESCAPED WITH THE LOOT",
            True,
            GREEN_LIGHT
        )

        loot_text = font.render(
            f"TOTAL LOOT: {score}",
            True,
            WHITE
        )

        length_text = small_font.render(
            f"FINAL LENGTH: {len(worm)}",
            True,
            GREEN_LIGHT
        )

        restart_text = small_font.render(
            "[ R ] RAID AGAIN",
            True,
            WHITE
        )

        quit_text = small_font.render(
            "[ Q ] RETIRE RICH",
            True,
            (
                170,
                170,
                175
            )
        )


        screen.blit(
            victory_text,
            victory_text.get_rect(
                center=(
                    WIDTH // 2,
                    135
                )
            )
        )

        screen.blit(
            gremlin_text,
            gremlin_text.get_rect(
                center=(
                    WIDTH // 2,
                    185
                )
            )
        )

        screen.blit(
            loot_text,
            loot_text.get_rect(
                center=(
                    WIDTH // 2,
                    225
                )
            )
        )

        screen.blit(
            length_text,
            length_text.get_rect(
                center=(
                    WIDTH // 2,
                    255
                )
            )
        )

        screen.blit(
            restart_text,
            restart_text.get_rect(
                center=(
                    WIDTH // 2,
                    300
                )
            )
        )

        screen.blit(
            quit_text,
            quit_text.get_rect(
                center=(
                    WIDTH // 2,
                    330
                )
            )
        )


    # =====================================================
    # UPDATE SCREEN
    # =====================================================

    pygame.display.flip()

    clock.tick(
        GAME_SPEED
    )


pygame.quit()