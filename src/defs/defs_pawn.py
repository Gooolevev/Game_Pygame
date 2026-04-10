from src.defs.models import BasePawnDef, BasePawnSkillsDef, SkillData

PAWN_0 = BasePawnDef(
    id="pawn_0",
    name="Vasilia",
    base_health=100,
    base_speed=0.5,
    speed_work=4,
    skills=BasePawnSkillsDef(
        shooting=SkillData(name="Стрельба", level=0, xp=0.0),
        melee=SkillData(name="Ближний бой", level=2, xp=0.0),
        construction=SkillData(name="Строительство", level=9, xp=0.0),
        mining=SkillData(name="Горное дело", level=1, xp=0.0),
        cooking=SkillData(name="Кулинария", level=0, xp=0.0),
        medicine=SkillData(name="Медицина", level=12, xp=0.0),
    ),
    visual_size=(30, 30),
    image_path="pawn_0.png",
)

PAWN_1 = BasePawnDef(
    id="pawn_1",
    name="Artem",
    base_health=100,
    base_speed=0.5,
    speed_work=4,
    skills=BasePawnSkillsDef(
        shooting=SkillData(name="Стрельба", level=5, xp=0.0),
        melee=SkillData(name="Ближний бой", level=15, xp=0.0),
        construction=SkillData(name="Строительство", level=2, xp=0.0),
        mining=SkillData(name="Горное дело", level=0, xp=0.0),
        cooking=SkillData(name="Кулинария", level=6, xp=0.0),
        medicine=SkillData(name="Медицина", level=9, xp=0.0),
    ),
    visual_size=(30, 30),
    image_path="pawn_1.png",
)

PAWN_2 = BasePawnDef(
    id="pawn_2",
    name="Timur",
    base_health=100,
    base_speed=0.5,
    speed_work=4,
    skills=BasePawnSkillsDef(
        shooting=SkillData(name="Стрельба", level=1, xp=0.0),
        melee=SkillData(name="Ближний бой", level=0, xp=0.0),
        construction=SkillData(name="Строительство", level=14, xp=0.0),
        mining=SkillData(name="Горное дело", level=17, xp=0.0),
        cooking=SkillData(name="Кулинария", level=3, xp=0.0),
        medicine=SkillData(name="Медицина", level=6, xp=0.0),
    ),
    visual_size=(30, 30),
    image_path="pawn_2.png",
)

PAWNS = {"pawn_0": PAWN_0, "pawn_1": PAWN_1, "pawn_2": PAWN_2}
