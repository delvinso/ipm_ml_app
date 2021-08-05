## TODO

- remove username/password from forms.css
- CCM specific stuff in layout.jinja2
- remove index.jinja2,signup.jinja2, success.jinja2
- add models and jmp_score, RENAME VARIABLES SO THEY ARE INLINE WITH THE FIELD NAMES. this way when we call form.data() the data will be good to go wrt to prediction.
- likewise for css fields


## IPM ML App

Please contact ...


## About

This is a web-app built using flask following factory guidelines containerized using docker-compose.

The core of the app are two objective scoring models built to predict the probability of optimal (OPT) and no growth residual (NGR) cytoreduction. These two files, along with `jmp_score.py` (obtained by being a licensed JMP 15.2+) need to be placed inside the `flask/project/` folder for the app to work correctly.

docker build -t test .   # uses dockerfile
docker run -p 5000:5000 test # port to expose and tag
docker exec -it 2cda2b0643f8 bash 