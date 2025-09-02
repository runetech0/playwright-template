import asyncio
import os
import random
from pathlib import Path

from playwright.async_api import async_playwright

from app.logs_config import get_logger

from .gvs import SCREENSHOTS_DIR, SESSIONS_DIR

logger = get_logger()


class Browser:
    def __init__(
        self,
        headless: bool = False,
        session_dir_name: str | None = None,
        page_load_timeout_seconds: int = 10,
    ):
        self.headless = headless
        if self.headless:
            logger.info("Running in headless mode")

        self._page_load_timeout_seconds = page_load_timeout_seconds
        session_dir_name = session_dir_name or "default"

        self._session_dir = (
            Path(os.path.join(SESSIONS_DIR, session_dir_name)).absolute().__str__()
        )

        self._screenshots_dir = (
            Path(os.path.join(SCREENSHOTS_DIR, f"{session_dir_name}-screenshots"))
            .absolute()
            .__str__()
        )

        os.makedirs(self._screenshots_dir, exist_ok=True)

    async def start(self) -> None:
        try:
            await self.main()

        except Exception as e:
            try:
                logger.error(
                    f"Error when handling product links: {e}. Closing the browser ...",
                    exc_info=True,
                )
                await self.browser.close()

            except Exception as e:
                logger.error(f"Error when closing the browser: {e}", exc_info=True)

    async def _random_wait(self, min: int = 1, max: int = 1) -> None:
        await asyncio.sleep(random.randint(min, max))

    async def page_screenshot(self, name: str) -> None:
        await self.page.screenshot(path=f"{self._screenshots_dir}/{name}.png")

    async def main(self) -> None:
        async with async_playwright() as p:
            logger.info("Launching browser ...")

            self.browser = await p.chromium.launch_persistent_context(
                headless=self.headless,
                user_data_dir=self._session_dir,
                args=["--disable-blink-features=AutomationControlled"],
            )

            self.page = await self.browser.new_page()
            await asyncio.sleep(1)
            if len(self.browser.pages) > 1:
                await self.browser.pages[0].close()
