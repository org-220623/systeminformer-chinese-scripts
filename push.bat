git add .
git commit -m "update data"
git push gitee
git push origin
cd ..
git add .python.patch
git commit -m "update submodule"
git push --all origin
git restore .
pause