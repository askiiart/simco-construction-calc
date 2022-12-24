# SimCo Construction Calculator
This is a tool to calculate the construction price of things.

# How to use

## Windows
1. Install [git](https://git-scm.com/download/win)
2. Install [Python](https://python.org/downloads)
   - Make sure to check the box that says "Add Python to PATH" when installing Python

![Add Python to PATH](/images/windows/python-install.png "Add Python to PATH")

2. Open your Documents folder
3. Hold shift and right-click, then click "Open PowerShell window here"

![Open PowerShell](/images/windows/open-powershell.png "Open PowerShell")

4. Run `git clone https://github.com/askiiart/simco-construction-calculator` to clone the repository.
5. Run `cd simco-construction-calculator/` to go into the folder.
6. Run `python main.py` to run the program.

## Mac
1. Open the terminal

![Open the terminal](/images/mac/terminal.png "Open the terminal")

2. Run `xcode-select --install` to install xcode (we need `git` and `python3`, which are both installed with xcode)

![Install xcode](/images/mac/xcode-install.png "Install xcode")

3. Click "Install", and agree to the terms, then wait for xcode to install.
4. Run `cd ~/Documents` to go to your Documents folder.
5. Run `git clone https://github.com/askiiart/simco-construction-calculator` to clone the repository.
6. Run `cd simco-construction-calculator/` to go into the folder.
7. Run `python3 main.py` to run the program.


## Linux
This won't be as detailed, because Linux varies so much, and because Linux users tend to know how to do this anyways.
P.S. this is all in the terminal.
1. Install git - this varies by distro (well, your package manager, like apt, dnf, etc.), but is usually `sudo apt install git` or `sudo dnf install git` or something like that.
2. Run `cd ~/Documents` to go to your Documents folder.
2. Run `git clone https://github.com/askiiart/simco-construction-calculator` to clone the repository.
3. Run `cd simco-construction-calculator/` to go into the folder.
4. Run `python3 main.py` to run the program.


## Android
Sorry for the odd aspect ratio, it's a long story*

1. Install [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3), **and** the [Pydroid repository plugin](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3.quickinstallrepo) from the Google Play Store

![Pydroid 3](/images/android/install-pydroid.png "Pydroid 3")

2. Open Pydroid 3, and click through the first few screens. When you get to this screen, enable "Preserve files on exit" and "Tab inserts spaces".

![Pydroid 3 settings](/images/android/pydroid-settings.png "Pydroid 3 settings")

3. Click through the rest, then press the X button in the top right to exit the ad. You do NOT need to pay.

![Exit the ad](/images/android/exit-ad.png "Exit the ad")

4. Click the hamburger menu (the 3 bars), then click "Pip". Type "wget", then click install, and wait for it to install. This shouldn't take too long.

![Install wget](/images/android/install-wget.gif "Install wget")

5. Click the back arrow, then copy the code from [here](https://raw.githubusercontent.com/askiiart/simco-construction-calc/master/main.py). Paste the code into Pydroid 3, then click the run button in the bottom right.


## iOS
Try [Pyto](https://apps.apple.com/us/app/pyto-python-3/id1436650069). I can't provide detailed instructions because:

1. I don't have any iPhones or iPads that are new enough to run this (iOS 14 is required)
2. I don't want to deal with it.

You could also run this in a Jupyter notebook on Google Colab, but that would be tricky because it's a Jupyter notebook, and so isn't very interactive. Feel free to fork this and make a Colab version, though. Or maybe I'll make a Colab version, but don't count on it.


*I'm running this on Android-x86 in a virtual machine. Android-x86 is a project that allows Android to run on desktop computer hardware, and a virtual machine is a virtual computer.
