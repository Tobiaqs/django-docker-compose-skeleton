# Basic Django / Docker Compose skeleton
## Setting your project name in the code
There are a few file/folder name changes that need to happen before you can start coding.

First, replace the word `skeleton` by something of your choosing (`<your-project-name>`), preferably without any special characters and all lowercase, in the following files:

- `docker/prod/docker-compose.yml`
- `backend/skeleton/wsgi.py`
- `backend/skeleton/settings.py`
- `backend/manage.py`

Then, rename the folder `backend/skeleton` to `backend/<your-project-name>`

## Development setup
### Development and production environments
Let `$DOCKER` be a folder where you keep your docker-compose projects (i.e. `/opt/docker`, `~/docker`). Let `$REPO` be the root folder of your repo.

In `$DOCKER`, create two directories:

- `<your-project-name>_dev`
- `<your-project-name>_prod`

In `$DOCKER/<your-project-name>_dev`:

```
ln -s $REPO src
ln -s $REPO/docker/dev/docker-compose.yml
ln -s $REPO/docker/dev/.env.example
cp .env.example .env
```

Set `VIRTUAL_HOST_DJANGO` and `VIRTUAL_HOST_ADMINER` in `.env` to hostnames of your choosing, i.e. `<your-project-name>.local` and `adminer.<your-project-name>.local`.

In `$DOCKER/<your-project-name>_prod`:

```
ln -s $REPO src
ln -s $REPO/docker/prod/docker-compose.yml
ln -s $REPO/docker/prod/.env.example
cp .env.example .env
```

Set `VIRTUAL_HOST_DJANGO` in `.env` to a hostname of your choosing, i.e. `<your-project-name>.local`.

### NGINX proxy
Furthermore,

- Run `cp -r $REPO/docker/proxy/ $DOCKER/`
- In `$DOCKER/proxy/docker-compose.yml`, `$DOCKER/<your-project-name>_dev/docker-compose.yml`, `$DOCKER/<your-project-name>_prod/docker-compose.yml`, replace `<your-project-name>` with your actual project name (lowercase, only use alphanumerics and underscores).

### Networks
Then,

- Run `docker network create proxy_<your-project-name>_dev`
- Run `docker network create proxy_<your-project-name>_prod`
- In `$DOCKER/proxy`, run `docker-compose up -d`
- In `$DOCKER/<your-project-name>_dev`, run `docker-compose up -d`
- In `$DOCKER/<your-project-name>_prod`, run `docker-compose up -d`

Finally, add the chosen hostnames to the bottom of your `/etc/hosts` file:

```
127.0.0.1   <your-project-name>.local
127.0.0.1   adminer.<your-project-name>.local
127.0.0.1   prod.<your-project-name>.local
```

### Rebuilding containers
Go to `$DOCKER/<your-project-name>_dev` or `$DOCKER/<your-project-name>_prod`, and run `docker-compose up --build -d` to rebuild all containers where necessary.

## Production setup
We assume you already run an instance of NGINX proxy.

Let `$DOCKER` be the folder where you keep your docker-compose installations. Create a folder such as `$DOCKER/tenant-01`. Let `$REPO` be the root folder of your repo. 

Then, in `$DOCKER/tenant-01`:

```
ln -s $REPO src
ln -s $REPO/config/prod/docker-compose.yml
ln -s $REPO/config/prod/.env.example
cp .env.example .env
```

In `.env`, set a generated `SECRET_KEY` and a unique hostname that points to your NGINX proxy, such as `tenant-01.softwarecorp.com`.
