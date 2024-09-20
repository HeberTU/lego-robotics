# lego-robotics
This repo contains python code to operate various lego projects.

## Dependencies

1. PyEnv
2. Poetry

### PyEnv installation in macOS

In the terminal:

1. Update Homebrew and install it:
```
brew update
brew install pyenv
```

2. Set up the shell environment for PyEnv for ZSH:

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

3. Install python 3.8.6 using PyEnv

```
pyenv install 3.8.5
pyenv global 3.8.5
```

### Poetry installation
1. Install poetry using the following command:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

2. Add Poetry's bin directory to PATH environment variable.

```
source $HOME/.poetry/env
```
4. Set virtual env in project root.

```
poetry config virtualenvs.in-project true
```

### Dependencies Installation
1. Create python environment with all dependencies:
```
poetry install
```

2. Activate python environment:

```
source .venv/bin/activate
```

## Connect your Lego Hub

This project runs on LEGO® MINDSTORMS® and SPIKE® hubs. Follow these steps to get started: 

1. Install the Pybricks firmware on your hub by following the official [instructions](https://pybricks.com/learn/getting-started/install-pybricks/#installing-pybricks-on-the-hub)
2. Connect your hub to your computer via Bluetooth using the Pybricks [web-based code editor](https://code.pybricks.com/) at least once.
3. Run the following command in your terminal:

```
make run
```
You should hear a beep, and the hub's display will show "Hello world!".





