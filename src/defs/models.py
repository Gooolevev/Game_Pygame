from pydantic import BaseModel, Field


class BaseItemDef(BaseModel):
    """Basic class for any items (wood, stone, steel ...)"""

    id: str
    name: str

    weight: float = Field(default=0.1, ge=0)
    nutrition: float = Field(default=0.0, ge=0)
    category: str = "resource"

    visual_size: tuple[int, int] = (12, 12)
    image_path: str


class BaseObjectDef(BaseModel):
    """Basic class for any objects in the map (tree, rock, wall, ...)"""

    id: str
    name: str
    max_hp: int
    work_type: str
    loot: dict[str, int] = Field(default_factory=dict)

    passable: bool = False

    visual_size: tuple[int, int] = (28, 28)
    image_path: str


class BaseTileDef(BaseModel):
    """Basic class for any type tiles in the map (почва, песок, вода, ...)"""

    id: str
    name: str
    walk_speed: float = 1.0
    can_build: bool = True

    max_hp: float = 0.0
    work_type: str ="None"
    loot: dict[str, int] = {"None": 0}
    passable: bool = True


    visual_size: tuple[int, int] = (30, 30)
    image_path: str


class BaseRecipeDef(BaseModel):
    """Basic class for cooking dishes"""

    id: str
    name: str

    work_amount: int = Field(default=0, ge=0)
    ingredients: dict[str, int]
    result: str


class BaseBuildingDef(BaseModel):
    """Basic class in construction"""

    id: str
    name: str

    work_amount: int = Field(default=0, ge=0)
    resources: dict[str, int]
    result: str


class SkillData(BaseModel):
    """Basic class for colonist skill progression"""

    name: str
    level: int = Field(default=0, ge=0, le=20)
    xp: float = 0.0


class BasePawnSkillsDef(BaseModel):
    """Basic сlass for colonist skills"""

    shooting: SkillData = SkillData(name="Стрельба", level=0, xp=0.0)
    melee: SkillData = SkillData(name="Ближний бой", level=0, xp=0.0)
    construction: SkillData = SkillData(name="Строительство", level=0, xp=0.0)
    mining: SkillData = SkillData(name="Горное дело", level=0, xp=0.0)
    cooking: SkillData = SkillData(name="Кулинария", level=0, xp=0.0)
    medicine: SkillData = SkillData(name="Медицина", level=0, xp=0.0)


class BasePawnDef(BaseModel):
    """A basic class for any colonist on the map"""

    id: str
    name: str

    base_health: int = Field(default=100, ge=0)
    base_speed: float = Field(default=0.5, gt=0.1)
    speed_work: float = Field(default=5, gt=0.1)

    skills: BasePawnSkillsDef

    visual_size: tuple[int, int] = (30, 30)
    image_path: str = ("pawn_1.png",)
