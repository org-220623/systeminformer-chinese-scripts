git add .
git commit -m "update data"
git push gitee --all
git push origin
cd ..
git add .i18n
git commit -m "update submodule"
git push --all origin
git restore .