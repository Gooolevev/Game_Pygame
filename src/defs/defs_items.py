from src.defs.models import BaseItemDef


WOOD_DEF = BaseItemDef(
    id="wood",
    name="Древесина",
    stack_limit=75,
    weight=0.2,
    nutrition=0,
    category="resource",
    image_path="wood.png",
)

STONE_DEF = BaseItemDef(
    id="stone",
    name="Камень",
    stack_limit=75,
    weight=0.5,
    nutrition=0,
    category="resource",
    image_path="stone.png",
)

STEEL_DEF = BaseItemDef(
    id="steel",
    name="Сталь",
    stack_limit=75,
    weight=1,
    nutrition=0,
    category="resource",
    image_path="steel.png",
)

FOOD_MEAL_DEF = BaseItemDef(
    id="food_meal",
    name="Еда из мяса",
    stack_limit=75,
    weight=0.1,
    nutrition=1,
    category="food",
    image_path="food_meal.png",
)

FOOD_NATURAL_DEF = BaseItemDef(
    id="food_natural",
    name="Еда из растений",
    stack_limit=75,
    weight=0.1,
    nutrition=1,
    category="food",
    image_path="food_natural.png",
)

AXE_DEF = BaseItemDef(
    id="axe",
    name="топор",
    stack_limit=1,
    weight=5,
    nutrition=0,
    category="weapon",
    image_path="axe.png",
)


ITEMS = {
    "wood": WOOD_DEF,
    "stone": STONE_DEF,
    "steel": STEEL_DEF,
    "food_meal": FOOD_MEAL_DEF,
    "food_natural": FOOD_NATURAL_DEF,
    "axe": AXE_DEF,
}
