import sys
from pathlib import Path
from loguru import logger

def setup_logging():
    log_dir = Path("debug_logs")
    log_dir.mkdir(exist_ok=True)

    logger.remove()

    logger.add(sys.stderr, format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>", level="INFO")

    logger.add(
        log_dir / "rimworld_debug_{time:YYYY-MM-DD}.log", 
        level="DEBUG",
        rotation="10 MB",
        compression="zip",
        encoding="utf-8",
        enqueue=True
    )
    return logger

game_logger = setup_logging()
