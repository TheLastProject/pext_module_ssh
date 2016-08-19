# Quick SSH connector module for Pext
This module allows [Pext](https://github.com/Pext/Pext) to quickly open a
terminal with SSH connecting to your favourite server of choice. The server
list is parsed from ~/.ssh/config.

# Supported flags
- terminal: Use a custom terminal. Must support the -e flag to start with a specific command (default: "xterm")

# Dependencies
## Debian

    sudo apt-get install python3 openssh-client xterm

## Fedora

    sudo dnf install python3 openssh-clients xterm

# License
GPLv3+.
