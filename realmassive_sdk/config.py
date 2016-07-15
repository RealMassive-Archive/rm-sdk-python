
from os import getenv


class Config(object):
    # NOTE: Change this to public endpoint before distribution
    ENDPOINT = getenv("REALMASSIVE_API_ENDPOINT", "http://localhost:8080")
    # NOTE: Change this to public endpoint before distribution
    AUTH_ENDPOINT = getenv("AUTH_ENDPOINT", "http://localhost:5000")
    USER = getenv("REALMASSIVE_USER", None)
    PASSWORD = getenv("REALMASSIVE_PASSWORD", None)
