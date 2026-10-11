import os
import sys
import uvicorn

# Add modules folder to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    uvicorn.run("module_4.main:app", host="127.0.0.1", port=8080, reload=True)