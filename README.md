# geohandler
Flask App that handles Geospatial Data

[![CircleCI](https://circleci.com/gh/sinwoobang/geohandler.svg?style=svg)](https://circleci.com/gh/sinwoobang/geohandler)

## Goal
- Remind how to make a structrue of Flask from the bottom
- Try to dockerize most of things for Web Application
- Try to use geojson

## Used
- REST API with Flask(**only tried structures** so it doesn't work like a real one)
  - Assets API
- Test with pytest, coverage
  - Check the package tests/
  - Run automatically on [CircleCI](https://circleci.com/gh/sinwoobang/geohandler)
- Pre-commit hooks(will be operated automatically if you try to commit)
  - Flake8
  - trailing-whitespace

## How to run
### Docker-compose
```bash
docker-compose build
docker-compose up
```
<img src="https://github.com/sinwoobang/geohandler/blob/master/.images/docker.png">

### Runserver
```bash
python manage.py
```

### Test
```bash
pytest
```
<img src="https://github.com/sinwoobang/geohandler/blob/master/.images/test.png">

### Pre-commit hooks
```bash
pre-commit
```

### Reference
- Steerpath API
