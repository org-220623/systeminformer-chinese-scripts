git config --global push.prune true
git add .
git commit -m "update data"
git push origin
git push gitee
git push github
git push gitea
git push jihulab
cd ..
git add .python.patch
git commit -m "update submodule"
git push --all origin
git push --all gitee
git push --all gitlab
git push --all gitea
git restore .
pause