[ ![Wine](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/WINE-logo.png/120px-WINE-logo.png) ](https://cli.github.com/)

# Remove [Wine](https://www.winehq.org/) from [Ubuntu](https://ubuntu.com/) based distros

## Remove all dependencies and remaining files from wine

<br />
<br />

To `run` use:

```bash
chmod +x remove-wine.py
sudo ./remove-wine.py

or 

sudo python3 remove-wine.py
```

`SUDO` is needed, without superuser access we can't remove some files and configs

<br />
<br />


## Explanations

* This script will not remove plugins and files from vim, oh-my-zsh, compose, and other files created by user, unless if these files are in any target directories.

* Be Careful, use this script if you know what are you doing, maybe it can break other stuffs that you might want to use


<br />
<br />


### Made with 🥰 by [Dpbm](https://github.com/Dpbm)
