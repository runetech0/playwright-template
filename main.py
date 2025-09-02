import asyncio

from app.browser import Browser
from app.config_reader import Config
from app.logs_config import get_logger

logger = get_logger()


async def main() -> None:
    browser = Browser(
        headless=Config.BROWSER.HEADLESS,
        page_load_timeout_seconds=Config.BROWSER.PAGE_LOAD_TIMEOUT_SECONDS,
    )

    await browser.start()


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except Exception as e:
        logger.error(f"ERROR: {e}", exc_info=True)

    finally:
        logger.info("Bot exiting... If you need any help get on Telegram || @runetech")
        input("Press 'Enter' to close the bot <- ")
        input("Press 'Enter' 2 times more ... <- ")
        input("Press 'Enter' one more time to complete exit <- ")
