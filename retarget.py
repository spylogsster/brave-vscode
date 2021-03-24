import os
os.system('git remote remove origin')
os.system('git remote add origin git@spylogsster:brave/brave-core.git')
os.system('git pull')
os.system('git branch --set-upstream-to=origin/master master')
os.system('git config user.name "Sergey P"')
os.system('git config user.email "spylogsster@gmail.com"')
os.system('git config --global pull.rebase true')