cd ~/workspace/

git clone https://github.com/yyuu/pyenv.git ~/workspace/.pyenv

export PYENV_ROOT="$HOME/workspace/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv install anaconda3-4.1.1
pyenv rehash
pyenv global anaconda3-4.1.1

sudo pip install seaborn

echo 'export PYENV_ROOT="$HOME/workspace/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

jupyter notebook --generate-config
echo 'c.NotebookApp.ip = "*"' >> ~/.jupyter/jupyter_notebook_config.py
echo 'c.NotebookApp.open_browser = False' >> ~/.jupyter/jupyter_notebook_config.py
echo 'c.NotebookApp.notebook_dir = "/home/ubuntu/workspace"' >> ~/.jupyter/jupyter_notebook_config.py
echo 'c.NotebookApp.port = 8080' >> ~/.jupyter/jupyter_notebook_config.py
