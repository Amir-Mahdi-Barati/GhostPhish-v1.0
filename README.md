
# GhostPhish v1.0
**Phishing Simulation Framework for Cybersecurity Education**

Developed by: **Amir Mahdi Barati**  
GitHub: [https://github.com/Amir-Mahdi-Barati](https://github.com/Amir-Mahdi-Barati)  

---

## Overview
GhostPhish is a **terminal-based phishing simulation tool** designed for **cybersecurity training, red team exercises, and social engineering demonstrations**.  
It emulates login pages of popular platforms in a **safe and controlled environment**, allowing analysis of credential capture behavior for educational purposes.

> ⚠️ **For ethical and educational use only.**  

---

## Features
- Terminal-based CLI interface with structured and intuitive menus  
- Flask-powered local web server for serving templates  
- Realistic login templates: Instagram, Gmail, GitHub, LinkedIn  
- Credential logging with precise timestamps  
- Customizable CSS for accurate UI replication  
- Safe local testing (**localhost only**)  
- Modular and extensible architecture for template addition  

---

## Technologies Used
- Python 3.x  
- Flask  
- HTML5 / CSS3  
- ANSI escape codes for terminal formatting  
- Local file logging  

---

## Installation
```bash
git clone https://github.com/Amir-Mahdi-Barati/GhostPhish.git
cd GhostPhish
pip install -r requirements.txt
```

---

## Usage
1. Launch the CLI tool:
```bash
python phishing.py
```

2. Select the target platform from the interactive menu:
```
[1] Instagram
[2] Gmail
[3] GitHub
[4] LinkedIn
```

3. Open your web browser and navigate to the local server:
```
http://localhost:5000
```

4. Monitor captured credentials in the `/logs/` directory. Each login attempt is timestamped and saved in a corresponding file for analysis.

---

## License & Disclaimer
MIT License.  

This tool is **strictly for educational and ethical purposes**.  
Unauthorized or illegal usage is prohibited. The author is not responsible for misuse.

---

## Future Development
- Ngrok integration for remote simulation  
- Live analytics dashboard  
- GUI with drag-and-drop template management  
- AI-driven phishing awareness modules  

---

**GhostPhish — Learn, Experiment, Analyze.**
