# MoulinetteEvaluator
Service for evaluating programs server-side, using dynamic docker instances for sandboxing of external code.

# Setting up
1. Install Docker CE (https://docs.docker.com/engine/installation/)
2. Install RabbitMQ (used for background execution of worker threads, http://www.rabbitmq.com/download.html), and set it up for use with the evaluator:
    
    i. Create the moulinette user:
    ```bash
    >>> sudo rabbitmqctl add_user <user> <pass>
    >>> sudo rabbitmqctl add_vhost <vhost>
    >>> sudo rabbitmqctl set_user_tags <user> <tag>
    >>> sudo rabbitmqctl set_permissions -p <vhost> <user> ".*" ".*" ".*"
    ```
    
    ii. Store the values for \<user\>, \<pass\>, \<vhost\> and \<tag\> as the following environment variables:
    ```bash
    export MOULINETTE_RABBIT_USER=<user>
    export MOULINETTE_RABBIT_PASS=<pass>
    export MOULINETTE_RABBIT_VHOST=<vhost>
    export MOULINETTE_RABBIT_TAG=<tag>
    ```
    
    (for instance, put these values in your .bashrc/.zhrc or in an .env file you can then source - do not version this file)

3. Enable and start the Docker and RabbitMQ Server services. For systemd:
```bash
>>> sudo systemctl enable docker
>>> sudo systemctl start docker
>>> sudo systemctl enable rabbitmq-server
>>> sudo systemctl start rabbitmq-server
```

4. Clone repository:
```bash
>>> git clone git@github.com:molguin92/MoulinetteEvaluator.git
>>> cd MoulinetteEvaluator
```

5. Create a virtualenv for Python 3.6: 
```bash
>>> virtualenv --python3.6 ./venv
```

6. Install libraries:
```bash
>>> pip install -r ./requirements.txt
```
