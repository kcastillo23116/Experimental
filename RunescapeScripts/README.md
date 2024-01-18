# Runescape Scripts

## General Setup

1. Setup config file with below:
	```json
	    -Config:
		    client_title: Runelite - <username>
		    enable_on_start: false
		    file_path_to_client: \.runelite\
		    pc_profile: C:\Users\kcast\.runelite\
		    tesseract_path: C:\Program Files\Tesseract-OCR\
	```
1. Install latest tesseract from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
1. If getting errors about Tesseract language files try copying  the **C:\Program Files\Tesseract-OCR\tessdata\eng.traineddata** file to the **C:\Program Files\Tesseract-OCR** folder
1. Set runescape to modern resizeable in Interface options
1. Run Pycharm as admin?
1. Download and install Python 3.10
1. Download packages in requirements.txt using this command in terminal: **pip install -r requirements.txt** or using pycharm sync requirements tool
   - If doesn't work try installing latest
1. Upgrade numpy, opencv-python, pillow to latest
1. If any other packages causing errors try uninstalling and reinstalling from pycharm interpareter settings dialog

## Combat Scripts Setup
1. Update enemy name
1. Enable NPC highlighting and set to specified color: #ff00ffff
1. Right click tag all enemy so they're highlighted
1. Turn on Opponent information plugin in runelite

## Other
- Setup runelite discord notification plugin for level up messages and screenshots
  - Use these steps: https://github.com/ATremonte/Discord-Level-Notifications 
