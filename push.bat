git add .
git commit -m "update data"
git push origin
git push gitee
git push github
git push gitea
cd ..
git add .python.patch
git commit -m "update submodule"
git push --prune origin
git push --prune gitee
git push --prune gitlab
git push --prune gitea
git push --all origin
git push --all gitee
git push --all gitlab
git push --all gitea
git restore .
pause