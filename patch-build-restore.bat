push-system-informer-project.bat
cd .python.patch
python main.py --nodebug
cd ..\build
build_release.cmd
git restore .
pause