from ctsf.core.handler import Config

from ctsf.modules.request import get_request
from ctsf.modules.who import get_who


class Runner:
    def __init__(self, config: Config):
        self.config = config

    def __str__(self) -> str:
        return f"{self.config}"

    def run(self):
        if self.config.domain is not None:
            get_request(self.config.domain)

            if self.config.who is True:
                get_who(self.config.domain)
