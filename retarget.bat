git remote remove origin
git remote add origin git@brave:brave/brave-core.git
git pull
git branch --set-upstream-to=origin/master master
git config user.name "Sergey P"
git config user.email "spylogsster@gmail.com"
git config --global pull.rebase true