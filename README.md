# Quick SSH connector module for Pext
This module allows [Pext](https://github.com/Pext/Pext) to quickly open a
terminal with SSH connecting to your favourite server of choice. The server
list is parsed from ~/.ssh/config.

Currently, the terminal opened is always xterm. In the future, this will likely
become a setting.

# Dependencies
## Debian

    sudo apt-get install python3 openssh-client xterm

## Fedora

    sudo dnf install python3 openssh-clients xterm

# License
GPLv3+.
