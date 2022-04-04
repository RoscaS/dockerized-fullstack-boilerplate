# Dockerized Django, Postgres and Nuxt local environment with auto reload on code change

## Requirement

* [docker](https://docs.docker.com/engine/install/ubuntu/)
* [docker-compose](https://docs.docker.com/compose/install/)

## Build

1. Rename *.env.sample* to *.env* in both *backend* and *frontend* folders and update environment variables if needed
2. [Optional] Update *docker-compose.dev.yml*
3. Build the images and run the containers:
    ```sh
    $ docker-compose -f docker-compose.dev.yml up
    ```

    * Test the backend: [http://localhost:8000/api](http://localhost:8000/api)
        * go to [/articles](http://localhost:8000/api/articles) and create a couple of articles
        * if databases issues arise:
            * stop the container: `ctrl + c`
            * restart it: `docker-compose -f docker-compose.dev.yml up`
    * Test frontend connectivity: [http://localhost:3000](http://localhost:3000) and click on *Fetch data*'

## Run
   ```sh
   $ docker-compose -f docker-compose.dev.yml up
   ```

## Migrations
1. Make sure the containers are running and you're at the root of the project
2. Make the migrations
    ```sh
    $ docker-compose -f docker-compose.dev.yml exec backend python manage.py makemigrations
    ```
3. Either restart the containers, either run:
    ```
    $ docker-compose -f docker-compose.dev.yml exec backend python manage.py migrate
    ```


## Useful
* spin up: `docker-compose -f docker-compose.dev.yml up`
* spin down: `docker-compose -f docker-compose.dev.yml down`
* build and run: `docker-compose -f docker-compose.dev.yml up --build`
* logs: `docker-compose -f docker-compose.dev.yml logs -f`
* exec a command in a container: `docker-compose -f docker-compose.dev.yml exec <container-name> <command>`
    