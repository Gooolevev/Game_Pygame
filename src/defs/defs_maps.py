from src.defs.models import BaseObjectDef, BaseTileDef

TREE_DEF = BaseObjectDef(
    id="tree_oak",
    name="Oak Tree",
    max_hp=100,
    work_type="chopping",
    loot={"wood": 5},
    is_fire=True,
    passable=False,
    image_path="tree_oak.png",
)

ROCK_DEF = BaseObjectDef(
    id="rock_granite",
    name="Granite Rock",
    max_hp=250,
    work_type="mining",
    loot={"stone": 5},
    is_fire=False,
    passable=False,
    image_path="rock_granite.png",
)

WALL_WOOD_DEF = BaseObjectDef(
    id="wall_wood",
    name="Wall Wood",
    max_hp=250,
    work_type="chopping",
    loot={"wood": 3},
    is_fire=True,
    passable=False,
    image_path="well_wood.png",
)

WALL_STONE_DEF = BaseObjectDef(
    id="wall_stone",
    name="Wall Stone",
    max_hp=500,
    work_type="mining",
    loot={"stone": 3},
    is_fire=False,
    passable=False,
    image_path="well_stone.png",
)

GRASS_DEF = BaseTileDef(
    id="grass",
    name="Grass",
    walk_speed=1.0,
    can_plant=False,
    can_build=False,
    image_path="grass.png",
)

WATER_DEF = BaseTileDef(
    id="water",
    name="Water",
    walk_speed=0.3,
    can_plant=False,
    can_build=False,
    image_path="water.png",
)

SAND_DEF = BaseTileDef(
    id="sand",
    name="Sand",
    walk_speed=0.8,
    can_plant=False,
    can_build=False,
    image_path="sand.png",
)

PLOWLAND_DEF = BaseTileDef(
    id="plowland",
    name="Plowland",
    walk_speed=1.0,
    can_plant=True,
    can_build=False,
    image_path="plowland.png",
)


OBJECT_MAP = {
    "tree": TREE_DEF,
    "rock": ROCK_DEF,
    "wall_wood": WALL_WOOD_DEF,
    "wall_stone": WALL_STONE_DEF,
}

TILES_MAP = {
    "grass": GRASS_DEF,
    "water": WATER_DEF,
    "sand": SAND_DEF,
    "plowland": PLOWLAND_DEF,
}