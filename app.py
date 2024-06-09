#!/usr/bin/env python3

import sys



def usage():
    print(f"Usage: {sys.argv[0]} Command")
    print()
    print(f"Command:")
    print(f"  runserver     Start the API Server")
    print(f"  migrate       DB Migration")
    print(f"  harvest       Data Harvest and Save as Excel")

def run(command):
    match command:
        case "runserver":
            import api, logs
            api.run("api:app")
        case "migrate":
            import asyncio
            from db import migration
            asyncio.run(migration())
        case "harvest":
            from data import harvest
            harvest()
        case _:
            usage()



if __name__ == "__main__":
    run( (sys.argv[1:] or [None])[0] )
