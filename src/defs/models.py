from pydantic import BaseModel, Field, PositiveInt


class BaseItemDef(BaseModel):
    """Базовая схема для любого предмета (дрова, камень, сталь, ...)"""

    id: str
    name: str

    stack_limit: int = Field(default=75, gt=0)
    weight: float = Field(default=0.1, ge=0)
    nutrition: float = Field(default=0.0, ge=0)
    category: str = "resource"

    visual_size: tuple[int, int] = (12, 12)
    image_path: str


class BaseObjectDef(BaseModel):
    """Базовая схема для любого объекта на карте (дерево, скала, стена, ...)"""

    id: str
    name: str
    max_hp: int
    work_type: str
    loot: dict[str, int] = Field(default_factory=dict)

    is_fire: bool = True
    passable: bool = False

    visual_size: tuple[int, int] = (24, 24)
    image_path: str


class BaseTileDef(BaseModel):
    """Базовая схема для любого типа клетки на карте (почва, песок, вода, ...)"""

    id: str
    name: str
    walk_speed: float = 1.0
    can_plant: bool = False
    can_build: bool = True

    visual_size: tuple[int, int] = (24, 24)
    image_path: str

    visual_size: tuple[int, int] = (24, 24)
    image_path: str


class BaseRecipeDef(BaseModel):
    """Базовая схема для готовки блюд"""

    id: str
    name: str

    work_amount: int = Field(default=0, ge=0)
    ingredients: dict[str, int]
    result: str


class BaseBuildingDef(BaseModel):
    """Базовая схема для строительства"""

    id: str
    name: str

    work_amount: int = Field(default=0, ge=0)
    resources: dict[str, int]
    result: str


class SkillData(BaseModel):
    """Базовая схема для навыков колониста"""

    name: str
    level: int = Field(default=0, ge=0, le=20)
    xp: float = 0.0


class BasePawnSkillsDef(BaseModel):
    """Базовый набор навыков колониста"""

    shooting: SkillData = SkillData(name="Стрельба",level=0,xp=0.0)
    melee: SkillData = SkillData(name="Ближний бой",level=0,xp=0.0)
    construction: SkillData = SkillData(name="Строительство",level=0,xp=0.0)
    mining: SkillData = SkillData(name="Горное дело",level=0,xp=0.0)
    cooking: SkillData = SkillData(name="Кулинария",level=0,xp=0.0)
    medicine: SkillData = SkillData(name="Медицина",level=0,xp=0.0)


class BasePawnDef(BaseModel):
    """Базовая схема для любого колониста на карте"""

    id: str
    name: str

    base_health: int = Field(default=100, ge=0)
    base_speed: float = Field(default=2.5, gt=0.1)
    speed_work: float = Field(default=5, gt=0.1)
    inventory_slots: int = Field(default=10, ge=0)

    skills: BasePawnSkillsDef

    visual_size: tuple[int, int] = (24, 24)
    image_path: str = ("pawn_1.png",)
