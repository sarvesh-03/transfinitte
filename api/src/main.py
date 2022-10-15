"""
Main File
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import directLinkRoute
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from src.routes import electoral



server = FastAPI()
server.include_router(directLinkRoute.router)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=chrome_options)

server.include_router(electoral.router)


server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
