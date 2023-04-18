from itertools import chain
import subprocess
if __name__ == '__main__':
    out_list = []
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    for i in out.splitlines():
        out_list.append(i)
    if result.returncode == 0:
        if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in chain(out_list) and \
                "VERSION_CODENAME=jammy" in chain(out_list):
            print("SUCCESS")
        else:
            print("FAIL")
    else:
        print("FAIL")