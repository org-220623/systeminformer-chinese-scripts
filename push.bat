git add .
git commit -m "update data"
git push origin
git push gitee
git push github
git push gitea
cd ..
git add .python.patch
git commit -m "update submodule"
git push origin
git push gitee
git push gitlab
git push gitea
git restore .
pause