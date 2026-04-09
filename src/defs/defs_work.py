from src.defs.models import BaseRecipeDef, BaseBuildingDef

COOK_FOOD_MEAL_DEF = BaseRecipeDef(
    id="cook_food_meal",
    name="Приготовить еду",
    work_amount=100,
    ingredients={"food_meal": 10},
    result="food_meal",
)

COOK_FOOD_NATURAL_DEF = BaseRecipeDef(
    id="cook_food_natural",
    name="Приготовить еду",
    work_amount=100,
    ingredients={"food_natural": 10},
    result="food_natural",
)


BUILD_WALL_STONE_DEF = BaseBuildingDef(
    id="build_wall_stone",
    name="построить каменную стену",
    work_amount=500,
    resources={"stone": 5},
    result="wall_stone",
)

BUILD_WALL_STONE_DEF = BaseBuildingDef(
    id="build_wall_wood",
    name="построить каменную стену",
    work_amount=250,
    resources={"wood": 5},
    result="wall_wood",
)

BUILD = {
    "build_wall_stone": BUILD_WALL_STONE_DEF,
    "build_wall_stone": BUILD_WALL_STONE_DEF,
}

COOK = {
    "cook_food_meal": COOK_FOOD_MEAL_DEF,
    "cook_food_natural": COOK_FOOD_NATURAL_DEF,
}
