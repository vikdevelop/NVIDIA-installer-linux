#!/usr/bin/python3
import os

nvidiagpu = input("Enter series number of your NVIDIA Graphic card (e.g. GTX10xx, GTX7xx, RTX30xx...): ")

if nvidiagpu == 'GTX7xx':
    print("Adding RPM Fusion - Nonfree repository...")
    os.system("sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")
    print("Installing NVIDIA Driver v. 470...")
    os.system("sudo dnf install -y xorg-x11-drv-nvidia-470xx.x86_64")
    print("NVIDIA Driver for your NVIDIA Graphic card '% s' was installed successfully!" % nvidiagpu)
    exit()

if nvidiagpu == 'GTX6xx':
    print("Adding RPM Fusion - Nonfree repository...")
    os.system("sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")
    print("Installing NVIDIA Driver v. 470...")
    os.system("sudo dnf install -y xorg-x11-drv-nvidia-470xx.x86_64")
    print("NVIDIA Driver for your NVIDIA Graphic card '% s' was installed successfully!" % nvidiagpu)
    exit()

if nvidiagpu == 'GTX9xx':
    print("Adding RPM Fusion - Nonfree repository...")
    os.system("sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")
    print("Installing NVIDIA Driver - latest version...")
    os.system("sudo dnf install -y akmod-nvidia")
    print("NVIDIA Driver for you NVIDIA Graphic card '% s' was installed successfully!" % nvidiagpu)
    exit()

if nvidiagpu == 'GTX10xx':
    print("Adding RPM Fusion - Nonfree repository...")
    os.system("sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")
    print("Installing NVIDIA Driver - latest version...")
    os.system("sudo dnf install -y akmod-nvidia")
    print("NVIDIA Driver for you NVIDIA Graphic card '% s' was installed successfully!" % nvidiagpu)
    exit()

if nvidiagpu == 'RTX20xx':
    print("Adding RPM Fusion - Nonfree repository...")
    os.system("sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")
    print("Installing NVIDIA Driver - latest version...")
    os.system("sudo dnf install -y akmod-nvidia")
    print("NVIDIA Driver for you NVIDIA Graphic card '% s' was installed successfully!" % nvidiagpu)
    exit()

if nvidiagpu == 'RTX30xx':
    print("Adding RPM Fusion - Nonfree repository...")
    os.system("sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")
    print("Installing NVIDIA Driver - latest version...")
    os.system("sudo dnf install -y akmod-nvidia")
    print("NVIDIA Driver for you NVIDIA Graphic card '% s' was installed successfully!" % nvidiagpu)
    exit()

if nvidiagpu == 'GTX5xx':
    print("Your GPU '% s' is not supported. Nothing to do." % nvidiagpu)
    exit()
