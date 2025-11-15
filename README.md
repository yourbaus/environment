# Table of contents
1. [Setup git](#git)
2. [Virtual environment](#venv)
2. [Git login script](#gitlogin)
4. [Git usage](#gitusage)

## Setup git <a name="git"></a>

1. Install and open git bash https://gitforwindows.org/
2. Create `.ssh` folder in home dir if it does not exist `$ mkdir ~/.ssh`
3. Create ssh key (for more details https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
```
$ cd ~/.ssh
$ ssh-keygen -t ed25519 -C john.doe@gmail.com
Generating public/private ed25519 key pair.
Enter file in which to save the key (/c/Users/Nanoelectronics/.ssh/id_ed25519): ./id_heliox_jdoe
Enter passphrase for "id_heliox_jdoe" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in id_heliox_jdoe
Your public key has been saved in id_heliox_jdoe.pub
...
```
4. Add ssh key to your git account
- `$ clip < ~/.ssh/id_heliox_jdoe.pub` -> copies to clipboard. If clip does work simply copy from the file. 
- Go to github -> settings -> ssh and gpg keys -> new ssh key (paste content, add descriptive name)
5. Relaunch git bash and add ssh key to the current session
```
$ eval `ssh-agent` 
$ ssh-add ~/.ssh/id_heliox_jdoe
```
Now you can clone repositories with ssh:
```
$ mkdir ~/src
$ cd ~/src
$ git clone git@github.com:yourbaus/environment.git
```

## Create python virtual environment <a name="venv"></a>
1. Download and install python from https://www.python.org/downloads/. Important to download the version < Python 3.13. On the first page of the installation page, check the box: add python.exe to PATH 
2. Check that python is in PATH (on some systems `python` should be used instead of `python3`)
```
$ python3 --version
Python 3.12.7
```
the version should match the one just installed

3. Create a new virtual environment
```
$ cd ~/src/environment
$ python3 -m venv leklab_env
```
Virtual environment can be created at a different location and\or with a different name. If it is created in the git repo folder (like in this example) with a different name make sure you change `.gitignore` accordingly.

4. Activate new environment (on Unix-like `bin` instead of `Scripts`)
```
$ source ./leklab_env/Scripts/activate
```

5. Install all packages. In case you need extra dependencies modify `requirements.txt` accordingly
```
$ pip install -r ./requirements.txt
```

6. Install repo packages (e.g. for environment):
```
$ cd ~/src/environment
$ pip install -e .
```
This command creates config file `~/.leklab/leklab.json`. Modify it if different paths were used during installation.
Also for `plottr` nerds `~/.plottr/plottrcfg_main.py` is created where you can change `plottr` appearance.

7. Now you are ready to code. Don't forget to activate the virtual environment in your IDE.

For Visual Studio Code: 
- open Visual Studio Code
- Press `Ctrl + Shift + P` to open the command palette
- Type and select `Python: Select Interpreter` -> `Enter interpreter path` -> `Find` -> `.\environment\leklab_env\Scripts\python.exe`

## Setup git login script <a name="gitlogin"></a>
1. Check that your credentials are added to the `~/.leklab/users.txt`. If file does not exist create it and add your credentials like:
```
...
jdoe, id_helix_jdoe, johndoe_gitname, john.doe@gmail.com
```

2. Create `.bash_profile` file (if it was not created before):
```
if [ -f ~/.bashrc ]
then
    . ~/.bashrc
fi
```

3. Create `.bashrc` file (if it was not created before):
```
scripts_path=$(awk -F'"' '/"scripts_path"/ {print $4}' ~/.leklab/leklab.json)
SCRIPTS_PATH=$(eval echo "$scripts_path")

connect_github() {
    source $SCRIPTS_PATH/environment/connect_github.sh
}
```

4. Run `$ test -f ~/.bashrc && . ~/.bashrc`


## Usage when everything is installed <a name="gitusage"></a>
1. Connect by ssh with our homemade script
```
$ connect_github jdoe
```
2. Go to repo directory and work with code. There is a good and simple git guide https://rogerdudler.github.io/git-guide
