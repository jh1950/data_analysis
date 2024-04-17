#!/usr/bin/env python3

import uvicorn

from config.server import host, port, reload



if __name__ == "__main__":
    uvicorn.run("server:app", host=host, port=port, reload=reload)
