from fastapi import FastAPI
import os

app = FastAPI(root_path= "/api/v1")

root = os.getenv('ROOT_PATH')

@app.get("/scan")
async def root(qr_code:str):
    return f"{qr_code} by fastAPI"  
    # return {"{UID}": "{item_num}"}
