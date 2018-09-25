# Redis + Elastic

## Setup

### Install and Run the Docker Images

Use the `docker-compose` command to download and run all of the Docker images.

```
docker-compose up -d
```

This will run:

* Elasticsearch 6.4.0
* Logstash 6.4.0
* Kibana 6.4.0
* Cerebro 0.8.1
* Redis Unstable

You can access the web UI's on the following URLs:

* Kibana: [http://localhost:5601](http://localhost:5601)
* Cerebro: [http://localhost:9000](http://localhost:9000)


### Install and Run Redis Commander

[Redis Commander](https://www.npmjs.com/package/redis-commander) is a node.js application and requires [npm](https://www.npmjs.com/) be installed on your computer. Assuming it is:

```
sudo npm install -g redis-commander
redis-commander
```

Access it on [http://localhost:8081](http://localhost:8081)