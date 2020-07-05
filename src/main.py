# Resolve the problem!!
import re

def run():
   with open('/mnt/c/users/apjai/documents/developer/challenge3_py/src/encoded.txt', 'r', encoding='utf-8') as f:
    # code
    message = f.read()
    real_message = re.findall('[a-z]', message)
    print(real_message)


if __name__ == '__main__':
    run()
