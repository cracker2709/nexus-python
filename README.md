# nexus-python


# Heroku

## Install heroku cli
```shell
$ sudo snap install --classic heroku
```

## Connect to heroku
```shell
$ heroku login
$ heroku container:login
```

## Create the app
```shell
heroku create nexus-requester
```

## Build dockerfile and push to heroku registry
```shell
$ heroku container:push web -a nexus-requester
```

## Publish the container
```shell
$ heroku container:release web -a nexus-requester
```

## Access
[Nexus Requester via Heroku]("https://nexus-requester.herokuapp.com/")


# Okteto

* Delivery thanks to docker-compose file based on docker hub image
* Access [Nexus Requster via Okteto](https://nexus-search-cracker2709.cloud.okteto.net)