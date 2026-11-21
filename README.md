# discord-translation-bot

## Technology

[![Python](https://img.shields.io/badge/python-language-dimgray?style=for-the-badge&logo=python)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-discord_api-dimgray?style=for-the-badge&logo=discord)](https://discordpy.readthedocs.io/ja/latest/index.html)
[![railway](https://img.shields.io/badge/railway-deploy-dimgray?style=for-the-badge&logo=railway)](https://railway.app/)
[![Github Actions](https://img.shields.io/badge/github_actions-ci/cd-dimgray?style=for-the-badge&logo=github)](https://github.com/features/actions)
[![flake8](https://img.shields.io/badge/flake8-linter-dimgray?style=for-the-badge&logo=flake8)](https://flake8.pycqa.org/en/latest/)

### Development

Requires Python 3.13 (see `.python-version`).

Installing dependent libraries

```sh
$ python3 -m pip install -r requirements.txt
```

To add or update a dependency, edit `requirements.in` and regenerate the lock file `requirements.txt`:

```sh
$ uv pip compile requirements.in -o requirements.txt --python-version 3.13
```

discord.bot startup

```sh
python3 bot.py
```

Running tests

```sh
python3 -m unittest discover
```
