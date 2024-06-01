import os, logging.handlers
from dotenv import load_dotenv

load_dotenv()



log_level = os.getenv("LOG_LEVEL")
log_level = int(log_level) if log_level.isdigit() else logging._nameToLevel.get(log_level.upper(), 20)
backupCount = int(os.getenv("LOG_BACKUP_COUNT") or 10)
opts = {
    "filename": os.getenv("LOG_PATH") or "./access.log",
    "handler": {},
    "config": {
        "level": log_level,
        "format": os.getenv("LOG_FORMAT", "%(asctime)s %(levelname)s %(message)s"),
        "datefmt": os.getenv("LOG_DATE_FORMAT", "%m/%d/%Y %I:%M:%S %p"),
        "handlers": [],
    },
}

opts["handler"]["default"] = {
    "filename": opts["filename"],
}
opts["handler"]["size"] = {
    "filename": opts["filename"],
    "maxBytes": eval(os.getenv("LOG_MAXSIZE") or str(1024 * 1024 * 100)),
    "backupCount": backupCount,
}
opts["handler"]["time"] = {
    "filename": opts["filename"],
    "when": os.getenv("LOG_WHEN") or "d",
    "backupCount": backupCount,
}
opts["handler"]["stream"] = {}



handlers = []
htypes = map(lambda x: x.strip(), (os.getenv("LOG_ROTATE") or "default").split(","))
for htype in htypes:
    handler = None
    match htype:
        case "default":
            handler = logging.FileHandler
        case "size":
            handler = logging.handlers.RotatingFileHandler
        case "time":
            handler = logging.handlers.TimedRotatingFileHandler
        case "stream":
            handler = logging.StreamHandler
    if handler:
        handlers.append((htype, handler))
for htype, handler in handlers:
    opts["config"]["handlers"].append( handler(**opts["handler"][htype]) )



logging.basicConfig(**opts["config"])
