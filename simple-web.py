import web
import time
import random
from time import sleep
from datadog import initialize
from datadog import statsd

options = {
    'api_key':'055b39f0a3d1d078d89d5d4a51f5d23a',
    'app_key':'988c7fdc589ee268c1ec30d06b5453490eb8a8e8'
}

initialize(**options)

urls = (
    '/index', 'index',
    '/settings','settings',
    '/messages','messages'
)


class index:
    def GET(self):
        start = time.time()
        delay=random.uniform(0.01,0.1)
        sleep(delay)
        statsd.increment('web.get.count', tags = ["support","page:home"])
        duration = time.time() - start
        statsd.histogram('web.get.latency', duration, tags = ["support","page:home"])
        return "Index Page"

class settings:
    def GET(self):
        start = time.time()
        delay=random.uniform(0.2,0.6)
        sleep(delay)
        statsd.increment('web.get.count', tags = ["support","page:page1"])
        duration = time.time() - start
        statsd.histogram('web.get.latency', duration, tags = ["support","page:page1"])
        return "Settings Page"

class messages:
    def GET(self):
        start = time.time()
        delay=random.uniform(0.4,0.9)
        sleep(delay)
        statsd.increment('web.get.count', tags = ["support","page:page2"])
        duration = time.time() - start
        statsd.histogram('web.get.latency', duration, tags = ["support","page:page2"])
        return "Messages Page"

def dogstats(pagetag):
    start = time.time()
    statsd.increment('web.get.count', tags = ["support",pagetag])
    duration = time.time() - start
    statsd.histogram('web.get.latency', duration, tags = ["support",pagetag])


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
