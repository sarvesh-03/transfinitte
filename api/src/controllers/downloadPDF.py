import requests
import os

def download_pdf(url,state, dist,aconst,pconst):
    basepath="/server/src/pdfs"
    filepath=state
    path=os.path.join(basepath,filepath)
    if not os.path.isdir(path):
      os.mkdir(path)
    response = requests.get(url)
    fileName = f"{dist}-{aconst}-{pconst}.pdf"
    open(f"{path}/{fileName}", "wb").write(response.content)
