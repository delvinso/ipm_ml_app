# IPM ML App
## About

A web-app built using flask following factory guidelines for Piedimonte et al. 2021. The app is served using gunicorn with nginx acting as a reverse proxy and is containerized using docker-compose. 

The core of the app are two objective scoring models built to predict the probability of optimal (OPT) and no growth residual (NGR) cytoreduction. These two files, along with `jmp_score.py` (obtained by being a licensed JMP 15.2+) need to be placed inside the `flask/project/` folder for the app to work correctly.

The site can be visited at either ipm-ml.ccm.sickkids.ca or ipm.ccm.sickkids.ca.
