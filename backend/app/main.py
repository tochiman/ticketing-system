from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from env import ORIGINS, ROOT
from router import org, store, customer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(org.router, prefix=f'{ROOT}/org')
app.include_router(store.router, prefix=f'{ROOT}/store')
app.include_router(customer.router, prefix=f'{ROOT}/customer')