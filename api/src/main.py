"""
Main File
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import directLinkRoute


server = FastAPI()
server.include_router(directLinkRoute.router)
server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
