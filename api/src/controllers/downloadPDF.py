import requests
import os
from dotenv import load_dotenv
load_dotenv()
def download_pdf(url,state, dist,aconst,pconst):
    basepath=os.getenv("base_path")+"/src/pdfs"
    filepath=state
    path=os.path.join(basepath,filepath)
    if not os.path.isdir(path):
      os.mkdir(path)
    response = requests.get(url)
    fileName = f"{dist}-{aconst}-{pconst}.pdf"
    open(f"{path}/{fileName}", "wb").write(response.content)
