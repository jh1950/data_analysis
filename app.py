#!/usr/bin/env python3

import os, uvicorn
from dotenv import load_dotenv

load_dotenv()



def main():
    uvicorn.run(
        "api:app",
        host=os.getenv("HOST") or "127.0.0.1",
        port=int(os.getenv("PORT") or 8000),
        reload=str(os.getenv("RELOAD") or os.getenv("DEBUG")).lower() == "true",
    )



if __name__ == "__main__":
    main()
