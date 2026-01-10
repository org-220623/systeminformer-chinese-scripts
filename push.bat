git add .
git commit -m "update data"
git push origin
git push gitee
git push github
git push gitea
cd ..
git add .python.patch
git commit -m "update submodule"
git push --all --delete --prune origin
git push --all --delete --prune gitee
git push --all --delete --prune gitlab
git push --all --delete --prune gitea
git restore .
pause