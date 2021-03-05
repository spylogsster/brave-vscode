#!/bin/bash
set -x
set -e
rm -rf brave-browser
git clone git@github.com:brave/brave-browser.git
cd brave-browser
npm install
cd src
git clone git@github.com:spylogsster/brave-vscode.git 
mv brave-vscode .vscode
npm run init
cd brave
./../../../retarget.sh
