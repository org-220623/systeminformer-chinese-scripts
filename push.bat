git add .
git commit -m "update data"
git push origin
cd ..
git add .i18n
git add .i18n_0
git commit -m "update submodule"
git push --all origin
git restore .
exit