# Moscow time app

## Table of Contents
1. [About the project](#About the project)
   - [Built with](#Built with)
2. [Getting started](#Getting started)
3. [License](#License)
4. [Docker activity](#Docker activity)

## About the project
Moscow time app is designed to help everyone know current time in Moscow

### Built with
Current app is built using Flask framework

## Getting started
1. Clone the repo
    ```sh
   git clone https://github.com/MrKasimov/labs.git
   ```
2. Run `moscow_time.py`

## License
Distributed under the MIT License

## Docker activity
Started with adding Dockerfile:
```
FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./app.py" ]
```
Install requirements `requirements.txt` and copies app to `/code` directory. 
Run the server by command `python python_app/moscow_time.py runserver 0.0.0.0:80` 

### How to Run using Docker:
1. Clone the repository
2. Enter application directory

    ``$ cd app_python``

3. Build the image

    `` $ docker build -t app_p .``

    or

    install image from Docker hub [TODO]

    `` $ docker pull MrKasimov/app_python ``

4. Check the image

    `` $ docker images ``

5. Run the container based on the image

    `` $ docker run -d -p 80:80 <image_name> ``

    where *image_name* either *app_p*

5. Run container:
```docker run -p 80:80 MrKasimov/app_python```