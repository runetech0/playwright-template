# Store Checkout Links Checker

A powerful automated tool that checks product checkout links across multiple e-commerce platforms to verify their functionality. The bot automatically navigates through product pages, adds items to cart, and validates that checkout processes work correctly.

## 🚀 Features

- **Multi-Platform Support**: Automatically detects and handles different e-commerce platforms (Shopify, WooCommerce, etc.)
- **Automated Testing**: Simulates real user behavior by clicking "Buy Now" buttons and navigating through checkout flows
- **Screenshot Capture**: Takes screenshots when issues are detected for debugging
- **Telegram Integration**: Sends real-time notifications and status updates via Telegram
- **Headless Mode**: Runs in background without opening browser windows
- **Configurable Timeouts**: Adjustable page load and network idle timeouts
- **Comprehensive Logging**: Detailed logs for monitoring and debugging

## 📋 Prerequisites

- **Python 3.12+** - [Download Python](https://www.python.org/downloads/)
- **Git** (optional, for cloning) - [Download Git](https://git-scm.com/downloads)

## 🛠️ Installation

### 1. Extract the Project

If you received this as a zip file, extract it to your desired location:

```bash
# If you have the zip file
unzip store-checkout-links-checker.zip
cd store-checkout-links-checker
```

### 2. Install Python Dependencies

This project uses `uv` for fast Python package management. If you don't have `uv` installed:

```bash
# Install uv (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or use pip if you prefer
pip install uv
```

Then install the project dependencies:

```bash
# Install dependencies
uv sync

# Or if you don't have uv, use pip
pip install -r requirements.txt  # if available
```

### 3. Install Playwright Browsers

The project uses Playwright for browser automation. Install the required browsers:

```bash
# Install Playwright browsers
uv run playwright install

# Or with pip
playwright install
```

This will install Chromium, Firefox, and WebKit browsers that Playwright needs.

## ⚙️ Configuration

### 1. Set Up Telegram Bot (Optional but Recommended)

1. **Create a Telegram Bot**:
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Send `/newbot` and follow the instructions
   - Save your bot token (looks like `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

2. **Get Channel ID**:
   - For public channels: Use the channel username with `@` prefix (e.g., `@mychannel`)
   - For private channels: Add your bot to the channel as admin, send a message, then visit:
     `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
     - Find the `chat_id` in the response (usually starts with `-100`)

### 2. Configure the Application

1. **Copy the sample configuration**:
   ```bash
   cp sample-config.toml config.toml
   ```

2. **Edit `config.toml`** with your settings:
   ```toml
   [TELEGRAM]
   BOT_TOKEN = "your_bot_token_here"
   CHANNEL_ID = "@your_channel_username"

   [BROWSER]
   HEADLESS = true
   PAGE_LOAD_TIMEOUT_SECONDS = 30
   ```

   **Configuration Options**:
   - `BOT_TOKEN`: Your Telegram bot token (leave empty if not using Telegram)
   - `CHANNEL_ID`: Your Telegram channel ID or username
   - `HEADLESS`: Set to `true` for background operation, `false` to see browser windows
   - `PAGE_LOAD_TIMEOUT_SECONDS`: Maximum time to wait for pages to load

### 3. Add Product URLs

Edit `input/products.txt` and add the product URLs you want to check, one per line:

```txt
https://example-store.com/products/product-1
https://another-store.com/products/product-2
https://shop.example.com/products/product-3
```

## 🚀 Usage

### Basic Usage

Run the main application:

```bash
# Using uv (recommended)
uv run main.py

# Or with Python directly
python main.py
```

### What Happens

1. **Initialization**: The bot loads configuration and starts the Telegram worker
2. **Browser Launch**: Opens a browser (headless or visible based on config)
3. **URL Processing**: Goes through each URL in `input/products.txt`
4. **Platform Detection**: Automatically detects the e-commerce platform
5. **Testing Process**:
   - Finds and clicks "Buy Now" or "Add to Cart" buttons
   - Waits for cart page to load
   - Clicks checkout button
   - Verifies payment page loads correctly
6. **Results**: Sends status updates to Telegram and logs results

### Output

- **Console Logs**: Real-time status updates in the terminal
- **Telegram Notifications**: Status messages sent to your configured channel
- **Screenshots**: Saved in `screenshots/` directory when issues are detected
- **Log File**: Detailed logs saved to `logs.log`

## 📁 Project Structure

```
store-checkout-links-checker/
├── app/                          # Application modules
│   ├── __init__.py
│   ├── browser.py               # Browser automation logic
│   ├── config_reader.py         # Configuration management
│   ├── exceptions.py            # Custom exceptions
│   ├── gvs.py                   # Global variables and setup
│   ├── logs_config.py           # Logging configuration
│   ├── shopify_handler.py       # Shopify-specific handling
│   └── telegram.py              # Telegram bot integration
├── input/                       # Input files
│   └── products.txt             # Product URLs to check
├── screenshots/                 # Screenshots taken during testing
├── sessions/                    # Browser session data
├── config.toml                  # Application configuration
├── sample-config.toml           # Sample configuration file
├── main.py                      # Main application entry point
├── pyproject.toml               # Project dependencies
└── README.md                    # This file
```

## 🔧 Advanced Configuration

### Custom Selectors

The bot automatically tries multiple selectors for different e-commerce platforms. If you need custom selectors, you can modify the handler files in the `app/` directory.

### Timeout Settings

Adjust timeouts in `config.toml`:

```toml
[BROWSER]
PAGE_LOAD_TIMEOUT_SECONDS = 30  # Increase for slower sites
```

### Headless Mode

For production use, keep `HEADLESS = true`. For debugging, set to `false` to see browser windows.

## 📊 Understanding Results

### Success Messages
```
✅ https://example.com/products/product (Shopify) — Payment page working!
```

### Error Messages
```
❌ https://example.com/products/product (Shopify) — No buy now button found
❌ https://example.com/products/product (Shopify) — Checkout button not found
```

### Screenshots
When issues are detected, screenshots are automatically saved to the `screenshots/` directory with descriptive filenames.

## 🐛 Troubleshooting

### Common Issues

1. **"Playwright browsers not found"**
   ```bash
   uv run playwright install
   ```

2. **"Telegram bot connection failed"**
   - Check your bot token and channel ID in `config.toml`
   - Ensure the bot is added to your channel as an admin

3. **"No buy now button found"**
   - The product might be out of stock
   - The site might use different button selectors
   - Check the screenshot in `screenshots/` directory

4. **"Page load timeout"**
   - Increase `PAGE_LOAD_TIMEOUT_SECONDS` in config
   - Check your internet connection
   - The site might be slow or down

### Debug Mode

To see browser windows and debug issues:

```toml
[BROWSER]
HEADLESS = false
```

### Logs

Check `logs.log` for detailed error information and debugging.

## 🔒 Security Notes

- **Bot Tokens**: Never commit your Telegram bot token to version control
- **URLs**: Be careful with sensitive product URLs
- **Rate Limiting**: The bot includes delays to avoid overwhelming servers

## 🤝 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review the logs in `logs.log`
3. Check screenshots in `screenshots/` directory
4. Contact support on Telegram: @runetech

## 📝 License

This project is provided as-is for educational and testing purposes.

## 🔄 Updates

To update the project:

1. Download the latest version
2. Backup your `config.toml` and `input/products.txt`
3. Replace the project files
4. Restore your configuration files
5. Run `uv sync` to update dependencies

---

**Happy Testing! 🚀**
