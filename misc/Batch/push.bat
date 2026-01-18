git add .
git commit -m "update data"
git push gitee
git push github
git push jihulab
cd ..
git add .python.patch
git commit -m "update submodule"
git push --all origin
git push --all gitee
git restore .