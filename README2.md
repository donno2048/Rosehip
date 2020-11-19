# Rosehip
Reliable Operating System by Elisha Hollander Implemented Python

```diff
- this only works on windows
```
<br><details>
<summary><b>Info about other platforms</b></summary><br>
 
There is also a [version for linux](https://github.com/donno2048/Rosehip-L), more specifically for ubuntu debian and mint.

There is also a [version for web](https://github.com/donno2048/Rosehip-repl), which is not recommended

There is no version for Android but you can install [Pydroid](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) and download the source code, open _os.py_ in Pydroid, then by running in the Pydroid terminal `pip install pygame pyttsx3 pygame-gui Js2Py html2text markdown2` and pressing the play button on landscape mode you will enter Rosehip, from the programming apps only python, JavaScript and html are working on Android, and from the utilities only the Chrome app and the Camera app won't..

Since Android is built on linux you should be using the linux version of Rosehip mentioned above
</details>
<br><details>
<summary><b>You can run the .exe version from the <a href="https://github.com/donno2048/Rosehip/releases">releases section</a> (not recommended):</b></summary><br>

download the zip file named _exe.zip_ then extract it then just double click on _Rosehip.exe_

this is not recommended due to the unstable state of _Rosehip.exe_

___note: you don't need python to run Rosehip.exe___
</details>
<br><details>
<summary><b>How to install the source version (recommended):</b></summary><br>

download the project from the releases section or [go there directly](https://github.com/donno2048/Rosehip/releases), extract the folder then:
###### If you have python in your PATH:
double click on _a_
###### Else:
double click on _b_
</details>
<br><details>
<summary><b>How to use it</b></summary><br>

###### If you're using a PC:

double click on _start_

###### If you're using a laptop:

double click on _laptop_start_
</details>
<br><details>
<summary><b>What can you do with it</b></summary><br>

* press HOME button to open the menu bar or FN+LEFT_ARROW if you don't have any
* press INSERT button to open the painter
  * scroll up and down to change the size of the brush
  * scroll up and down while holding ALT button to change the color of the brush
  * scroll up and down while holding CTRL button to change the shape of the brush
</details>
<br><details>
<summary><b>To do</b></summary><br>

- [x] ~~[animations](https://en.wikipedia.org/wiki/Stop_motion)~~
- [x] ~~[pong](https://en.wikipedia.org/wiki/Pong)~~
- [x] ~~variety of compilers ([python](https://www.python.org/), [html](https://en.wikipedia.org/wiki/HTML), [batch](https://en.wikipedia.org/wiki/Batch_file), [c#](https://docs.microsoft.com/en-us/dotnet/csharp/), [javascript](https://www.javascript.com/), [visual basic](https://docs.microsoft.com/en-us/dotnet/visual-basic/) and [powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7))~~
- [x] ~~[chrome](https://en.wikipedia.org/wiki/Google_Chrome)~~
- [x] ~~[text based web-browser](https://en.wikipedia.org/wiki/Text-based_web_browser)~~
- [x] ~~[ogg music player](https://en.wikipedia.org/wiki/Ogg)~~
- [x] ~~[calculator](https://en.wikipedia.org/wiki/Calculator)~~
- [x] ~~[clock](https://en.wikipedia.org/wiki/Clock)~~
- [x] ~~[background color picker](https://en.wikipedia.org/wiki/Wallpaper_(computing))~~
- [x] ~~[background image picker](https://en.wikipedia.org/wiki/Wallpaper_(computing))~~
- [x] ~~[camera](https://en.wikipedia.org/wiki/Camera)~~
- [x] ~~[mp4 viewer](https://en.wikipedia.org/wiki/MPEG-4_Part_14)~~
- [x] ~~[maze](https://en.wikipedia.org/wiki/Maze)~~
- [ ] [CLI](https://en.wikipedia.org/wiki/Command-line_interface)
- [ ] [stable version of rosehip in pypi](https://pypi.org/project/rosehip/)
</details>
<br><details>
<summary><b>For developers:</b></summary><br>

if you want to use it as an .iso you can run [another code I wrote](https://github.com/donno2048/CITUR) but it's currently having some issues, as specified is the [README](https://github.com/donno2048/CITUR/blob/master/README.md)...

or you can either use the [.iso builder](https://github.com/donno2048/CITUR-L) for the [linux version of Rosehip](https://github.com/donno2048/Rosehip-L)
</details>
<br><details>
<summary><b>For extreme developers:</b></summary><br>

if you want to create the .exe yourself you need to install [cx_Freeze](https://cx-freeze.readthedocs.io/en/latest/) version 6.1 using `pip install cx_Freeze==6.1` then change __every__ `os.path.realpath(__file__)` to `sys.executable` you might need to use `import sys` then in the directory of _os.py_ run:
```python3
from cx_Freeze import Executable,setup
setup(name='Rosehip',options={'build_exe':{'packages':['roin'],'include_files':['image.jpg',('musics','musics'),('images','images'),('apps','apps')]}},executables=[Executable('os.py',base='Win32GUI')])
```
</details>
