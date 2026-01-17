cd ..
git add .python.patch
git commit -m "update submodule"
git push --all origin
git push --all gitee
git push --all gitea
git restore .