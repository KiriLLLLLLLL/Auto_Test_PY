# Доработать тест на питоне из предыдущего задания таким образом,
# чтобы вывод сохранялся построчно в список и в тесте проверялось,
# что в этом списке есть строки VERSION="22.04.1 LTS (Jammy Jellyfish)" и
# VERSION_CODENAME=jammy . Проверка должна выполняться только если код возврата равен 0.



# from itertools import chain
import subprocess
# if __name__ == '__main__':
#     out_list = []
#     result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
#     out = result.stdout
#     for i in out.splitlines():
#         out_list.append(i)
#     if result.returncode == 0:
#         if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in chain(out_list) and \
#                 "VERSION_CODENAME=jammy" in chain(out_list):
#             print("SUCCESS")
#         else:
#             print("FAIL")
#     else:
#         print("FAIL")

# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден
# в её выводе и False в противном случае. Передаваться должна только одна строка,
# разбиение вывода использовать не нужно.


command = 'cat /etc/os-release'
text = "VERSION_CODENAME=jammy"


def func(cmd, txt):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    if result.returncode == 0:
        if txt in out:
            return True
        else:
            return False
    else:
        return False


print(func(command, text))
