#!/usr/bin/env python3

import sys



def usage():
    print(f"Usage: {sys.argv[0]} Command [OPTION]")
    print()
    print(f"Command:")
    print(f"  runserver                 Start the API Server")
    print(f"  runclient [PATH]          Start the API Client")
    print(f"                            The default value of PATH is /NN01/fakeStream")
    print(f"  migrate [TABLE_NAME]...   DB Migration")
    print(f"                            Migrate only those tables when TABLE_NAME is specified")
    print(f"  harvest                   Data Harvest and Save as Excel")

def run(command=None, *args, **kwargs):
    match command:
        case "runserver":
            import api
            api.run("api:server")
        case "runclient":
            import api
            api.run("client", *args, **kwargs)
        case "migrate":
            from db import migration
            migration(*args, **kwargs)
        case "harvest":
            from data import harvest
            harvest(*args, **kwargs)
        case _:
            usage()



if __name__ == "__main__":
    run(*sys.argv[1:])
