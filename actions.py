import os


def main():
    os.chdir("/rt-thread/actions")
    os.system("pip install selenium")
    os.system("sudo apt install chromium-chromedriver")
    os.system("python rt-thread-club.py")


if __name__ == "__main__":
    main()
