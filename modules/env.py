import os


class EnvironmentConfig:
    def __init__(self):
        self.PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", "8000"))
        self.PROMETHEUS_PREFIX = os.getenv("PROMETHEUS_PREFIX", "melcloud")
        self.USERNAME = os.getenv("USERNSME", None)
        self.PASSWORD = os.getenv("PASSWORD", None)


env = EnvironmentConfig()
