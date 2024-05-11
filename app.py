#!/usr/bin/env python3

import uvicorn

from config import api



if __name__ == "__main__":
    uvicorn.run("api:app", **api)
