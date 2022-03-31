# Dockerized Django, Postgres and Nuxt local environment with auto reload on code change

## Build

1. Rename *.env.sample* to *.env* in both *backend* and *frontend* folders and update environment variables if needed
2. [Optional] Update *docker-compose.dev.yml* to your linking
3. Build the images and run the containers:
    ```sh
    $ docker-compose -f docker-compose.dev.yml up -d --build
    ```

   * Test the backend: [http://localhost:8000/api](http://localhost:8000/api).
   * Test the frontend: [http://localhost:3000](http://localhost:3000).

## Run
1. Run:
   ```sh
   $ docker-compose -f docker-compose.dev.yml up
   ```
   Done.

## Usefull
* logs: `docker-compose -f docker-compose.dev.yml logs -f`
* spin down: `docker-compose -f docker-compose.dev.yml down`
    