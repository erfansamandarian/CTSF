from ctsf.core.handler import Config

from ctsf.modules.request import get_request
from ctsf.modules.who import get_who


class Runner:
    def __init__(self, config: Config):
        self.config = config

    def __str__(self) -> str:
        return f"{self.config}"

    def run(self):  # this code is disgusting
        if self.config.domain is not None and self.config.who is False:
            get_request(self.config.domain)
        elif self.config.domain is not None and self.config.who is True:
            get_request(self.config.domain)
            get_who(self.config.domain)
