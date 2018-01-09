# MoulinetteEvaluator
Service for evaluating programs server-side, using dynamic docker instances for sandboxing of external code.

# Setting up
1. Install Docker CE (https://docs.docker.com/engine/installation/)
2. Install Redis (used for background execution of worker threads, https://redis.io/).

3. Enable and start the Docker and Redis Server services. For systemd:
```bash
$ sudo systemctl enable docker
$ sudo systemctl start docker
$ sudo systemctl enable redis-server
$ sudo systemctl start redis-server
```

4. Clone repository:
```bash
$ git clone git@github.com:molguin92/MoulinetteEvaluator.git
$ cd MoulinetteEvaluator
```

5. Create a virtualenv for Python 3.6 and activate it: 
```bash
$ virtualenv --python3.6 ./venv
$ . venv/bin/activate
```

6. Install libraries:
```bash
(virtualenv) $ pip install -r ./requirements.txt
```

7. Start a (or more) RQ worker in a background thread (for instance, using screen):
```bash
$ screen -d -m rq worker
```

8. Finally, start the web service...

    i. ... either directly, for testing:
    ```bash
    (virtualenv) $ python run.py
    ```
    
    ii. ... using gunicorn:
    ```bash
    (virtualenv) $ gunicorn moulinette:app
    ```
