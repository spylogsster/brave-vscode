import os
os.system('rm -rf brave-browser')
os.system('git clone git@github.com:brave/brave-browser.git')
os.system('cd brave-browser')
os.system('npm install')
os.system('cd src')
os.system('git clone git@github.com:spylogsster/brave-vscode.git ')
os.system('mv brave-vscode .vscode')
os.system('npm run init')
os.system('cd brave')

