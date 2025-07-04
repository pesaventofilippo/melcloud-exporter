import os


class EnvironmentConfig:
    def __init__(self):
        self.PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", "8000"))
        self.PROMETHEUS_PREFIX = os.getenv("PROMETHEUS_PREFIX", "melcloud")
        self.MEL_USERNAME = os.getenv("MEL_USERNAME", None)
        self.MEL_PASSWORD = os.getenv("MEL_PASSWORD", None)


env = EnvironmentConfig()
