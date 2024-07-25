from ctsf.core.handler import Config

from ctsf.modules.request import get_request
from ctsf.modules.who import get_who

version = "1.0.6" # NOTE: Do this in setup.py or something

class Runner:
    def __init__(self, config: Config):
        self.config = config

    def __str__(self) -> str:
        return f"{self.config}"

    def run(self):
        if self.config.domain is not None:
            get_request(self.config.domain, version)

            if self.config.who is True:
                get_who(self.config.domain)
