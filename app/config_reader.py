from dataclasses import dataclass

import toml
import os, sys

_CONFIG_FILE = 'config.toml'

if not os.path.exists(_CONFIG_FILE):
    print(
        """❌ config.toml file is missing.
          👉 Please rename 'sample-config.toml' to 'config.toml'
          or ask the developer to send you 'sample-config.toml' file."""
    )
    input("Press 'Enter' 3-times to exit...")
    input("Press 'Enter' 2-times more...")
    input("Press 'Enter' to exit now...")
    sys.exit(1)

_CONFIG_DATA = toml.load(_CONFIG_FILE)

@dataclass
class BROWSER:
    HEADLESS: bool = True
    PAGE_LOAD_TIMEOUT_SECONDS: int = 30

class Config:
    BROWSER: 'BROWSER'

    @classmethod
    def load(cls) -> None:
        cls.BROWSER = BROWSER(
            HEADLESS=_CONFIG_DATA['BROWSER']['HEADLESS'],
            PAGE_LOAD_TIMEOUT_SECONDS=_CONFIG_DATA['BROWSER']['PAGE_LOAD_TIMEOUT_SECONDS']
        )

Config.load()
