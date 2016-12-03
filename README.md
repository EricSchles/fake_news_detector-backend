# Fake News Detector Backend

This repository's main purpose is to accept connections from the fake news detector browser extension.  It then stores all urls collected.  And finally will pass them to the fact checker website [github repo found here](https://github.com/EricSchles/fact_checker_website)

## Installation

The first thing you'll need to do is clone this repo, it's preferred that you fork it and then submit pull requests from your fork.  This way we have clear providence of who did what, but also, it will be easier to roll back changes, should something be wrong, before committing to the canonical master repository.

You'll need [Python 3](https://www.python.org/downloads/) (Python 3.5 is preferred), [pip3](https://pip.pypa.io/en/stable/
installing/) (1.8.2 is preferred), and the heroku toolbelt and a heroku account to deploy this repository.

After you install Python simply run:

`pip install -r requirements.txt` (which is found in the top level directory of the main repo)

If you have python 2 installed, you might need to do:

`pip3 install -r requirements.txt`

Everything regarding deploying to heroku should be in 

`setup.md` (in the base directory).

## Docker Insructions
Building the image:
`docker build -t fake_news .`

Running the image:
If you  haven't uploaded to docker hub:
    and want to destoy the container when stopping (will lose data)
    `docker run --rm -it --name fake_news -p 80:80 -e FLASK_APP=run_server.py fake_news`
    without destroying the container
    `docker run -it --name fake_news -p 80:80 -e FLASK_APP=run_server.py fake_news`
If you have uploaded to docker hub:
    replace fake_news at the end with `<your docker hub username>/fake_news:latest`

You should see the image running on `http://localhost/`
If it complains about port conflict or you see some other site running change `-p 80:80` to `-p <some open port>:80`
and access at `http://localhost:<port you picked>/`

Push image to docker hub: 
Tag the image:
`docker images | grep fake_news`
    output should look like: 
    `fake_news           latest              581a331523bf        31 minutes ago      718.6 MB`
    take 3rd param, in this case `581a331523bf`
`docker tag 7d9495d03763 <your docker hub username>/fake_news:latest`

Push to docker hub:
`docker login`
    enter username and password
    `docker push <your docker hub username>/fake_news:latest`