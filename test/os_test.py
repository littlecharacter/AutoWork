import os
import time
import subprocess


if __name__ == "__main__":
    pass
    op_content = "/Applications/微信.app"
    # p = subprocess.Popen(op_content)
    # time.sleep(3)
    # p.terminate()
    os.system(f'open \"{op_content}\"')
    # os.system("osascript -e 'tell application \"/Applications/微信.app\" to quit'")