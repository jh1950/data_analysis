#!/usr/bin/env python3

import uvicorn

from config.api import host, port, reload



if __name__ == "__main__":
    uvicorn.run("api:app", host=host, port=port, reload=reload)
