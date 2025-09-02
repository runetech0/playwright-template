# Browser Automation Template

A Python-based browser automation framework built with Playwright for web scraping, testing, and automation tasks.

## Features

- **Headless/Headful Browser Control**: Run browsers in background or visible mode
- **Session Management**: Persistent browser sessions with user data directories
- **Screenshot Capture**: Automatic screenshot functionality with organized storage
- **Configurable Timeouts**: Customizable page load timeouts
- **Logging System**: Comprehensive logging with configurable levels
- **Async Support**: Built on asyncio for efficient concurrent operations

## Requirements

- Python 3.12+
- Playwright browser binaries

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd basic-automation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
# or using uv (recommended)
uv sync
```

3. Install Playwright browsers:
```bash
playwright install
```

## Configuration

Copy the sample configuration file and customize it:

```bash
cp sample-config.toml config.toml
```

Edit `config.toml`:
```toml
[BROWSER]
HEADLESS = false  # Set to true for headless mode
PAGE_LOAD_TIMEOUT_SECONDS = 10
```

## Usage

### Basic Usage

Run the automation:
```bash
python main.py
```

### Programmatic Usage

```python
from app.browser import Browser

async def run_automation():
    browser = Browser(
        headless=False,
        page_load_timeout_seconds=10
    )
    await browser.start()
```

## Project Structure

```
basic-automation/
├── app/
│   ├── __init__.py          # Package initialization
│   ├── browser.py           # Main browser automation class
│   ├── config_reader.py     # Configuration file parser
│   ├── exceptions.py        # Custom exception classes
│   ├── gvs.py              # Global variables and constants
│   ├── logs_config.py      # Logging configuration
│   ├── metadata.py         # Project metadata
│   └── _version.py         # Version information
├── config.toml              # Configuration file (create from sample)
├── main.py                  # Main entry point
├── pyproject.toml          # Project configuration and dependencies
├── sample-config.toml      # Sample configuration template
└── README.md               # This file
```

## Key Components

### Browser Class
- Handles browser lifecycle and automation
- Supports persistent sessions
- Automatic screenshot capture
- Configurable timeouts and wait strategies

### Configuration System
- TOML-based configuration
- Environment-specific settings
- Easy customization of browser behavior

### Logging
- Structured logging with configurable levels
- File and console output
- Error tracking and debugging support

## Dependencies

- **playwright**: Browser automation framework
- **toml/tomlkit**: Configuration file parsing
- **colorama**: Terminal color support
- **httpx**: HTTP client library

## Development

### Adding New Features
1. Extend the `Browser` class in `app/browser.py`
2. Add configuration options to `sample-config.toml`
3. Update logging in `app/logs_config.py`

### Testing
```bash
# Run tests (if implemented)
python -m pytest

# Lint code
python -m flake8
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Support

For help and support, contact: @runetech on Telegram

---

**Note**: This is a template project. Customize the automation logic in the `Browser.main()` method according to your specific use case.
