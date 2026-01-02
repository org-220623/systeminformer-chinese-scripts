push-system-informer-project.bat
python main.py --nodebug
cd ..\build
build_release.cmd
git restore .
pause