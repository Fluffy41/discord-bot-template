# Discord Bot Template

A simple and efficient template for creating a Discord bot using Python. This template is designed to help you kickstart your Discord bot development with essential features and best practices.

## Features

- Basic bot setup and login
- Environment variable management for secure token handling
- Logging setup for easy debugging and monitoring
- Flexible intents configuration for customized bot behavior

## Requirements

- Python 3.6 or newer
- `discord.py` library
- `python-dotenv` library for environment variable management

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in your project directory.
3. Create a `.env` file in the root directory of your project and add your Discord bot token like so: `DISCORD_TOKEN=your_token_here`.
4. Run `main.py` to start your bot.

## Configuration

The template uses Discord intents to control which events your bot can listen to. By default, it uses the recommended set of default intents. You can customize which intents to enable by uncommenting the relevant lines in `main.py`.

## Usage

After starting the bot, it will log its connection status to Discord. You can extend the bot's functionality by adding more event listeners and commands in `main.py`.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to improve the template or add new features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.