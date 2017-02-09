sudo rm -f /usr/bin/python
sudo ln -s /usr/bin/python3 /usr/bin/python

# pip install numpy # already satisfied
# pip install scipy # already satisfied
# pip install matplotlib # already satisfied
pip install pandas --user
pip install seaborn --user
pip install jupyter --user
pip install scikit-learn --user
pip install ipython -U --user

echo 'export PATH=/home/ubuntu/.local/bin:$PATH' >> ~/.bashrc

jupyter notebook --generate-config
echo 'c.NotebookApp.ip = "*"' >> ~/.jupyter/jupyter_notebook_config.py
echo 'c.NotebookApp.open_browser = False' >> ~/.jupyter/jupyter_notebook_config.py
echo 'c.NotebookApp.notebook_dir = "/home/ubuntu/workspace"' >> ~/.jupyter/jupyter_notebook_config.py
echo 'c.NotebookApp.port = 8080' >> ~/.jupyter/jupyter_notebook_config.py

jupyter notebook
