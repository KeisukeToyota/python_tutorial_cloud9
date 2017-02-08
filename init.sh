cd ~/workspace/

git clone https://github.com/yyuu/pyenv.git ~/workspace/.pyenv

export PYENV_ROOT="$HOME/workspace/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv install anaconda3-4.1.1
pyenv rehash
pyenv global anaconda3-4.1.1
conda update conda

sudo pip install seaborn

echo 'export PYENV_ROOT="$HOME/workspace/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

mkdir ~/workspace/src
touch ~/workspace/src/tutorial.py
