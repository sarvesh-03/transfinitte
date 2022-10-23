# Family-Tree
FullStack Family-Tree generator Application for TransfiNITTe'22
Our Solution consists of the following steps:
Break/Bypass the Captcha, in the worst case present the captcha to the user.
Get The Ac No, Part No from electoralsearch.in
Using this, get the appropiate pdf from the respective state's website (Some states host theiir files in an unprotected endpoint allowing for easy access, while some use an out-dated captcha but some are well-protected)
Parse the PDF and extract the data using OCR
Query the Necessary Data and Provide it to the User and show it in a family tree
Note: We had another approach where we can locally host the pdfs after downloading them to totally avoid the captchas and faster access speeds. However, with storage limitations, we won't be able to cover as many states as we can in our solution.

* [Frontend Github Repo Link](https://github.com/vigneshd332/hack-frontend/)
#### FastAPI, React
---
### Requirements
* [Pipenv](https://pipenv.pypa.io/en/latest/install/)
* [Docker](https://www.docker.com/get-started)

#### Setup
 * Fork and Clone the Repo
    sh
    git clone <YOUR_FORK_URL>
    
 * Add remote upstream
    sh
    git remote add upstream <MAIN_REPO_URL>
    
 * Create dotenv
    sh
    cp .env.example .env
    

#### Run the application
 * Build docker Image.
    sh
    docker-compose build 
    
 *  Run docker Container.
    sh
    docker-compose up
    
## Development
#### api
   * Go to backend directory.
        sh
        cd api
        
   * Create a virtualenv for this project.
        sh
        pipenv shell
        
   * Install Dependencies.
        sh
        pipenv install
        
#### Frontend 
  * Go to frontend directory
    sh
    cd web    
   
   * Install Dependencies.
       sh
        npm install
## Live Depoloyment:

    http://hacksparrow.muhesh.studio:3000/
