# Dockerized Django, Postgres and Nuxt local environment with auto reload on code change

## Build

1. Rename *.env.sample* to *.env* in both *backend* and *frontend* folders and update environment variables if needed
2. [Optional] Update *docker-compose.dev.yml* to your linking
3. Build the images and run the containers:
    ```sh
    $ docker-compose -f docker-compose.dev.yml up -d --build
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
1. Stop the container if it's running
2. Setup locally a venv and install the backend requirements. From the *backend* folder run:
   ```sh
   $ python manage.py makemigrations
   ```
3. Build and run the project:
   ```
   $ docker-compose -f docker-compose.dev.yml up -d --build`
   ```


## Usefull
* logs: `docker-compose -f docker-compose.dev.yml logs -f`
    