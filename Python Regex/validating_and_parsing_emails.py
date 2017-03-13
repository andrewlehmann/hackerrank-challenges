import re
import email.utils


def fun(s):
    return bool(re.match(r'^([A-Za-z][A-Za-z0-9_\-.]*)@([A-Za-z]+)\.([A-Za-z]{1,3})$', email.utils.parseaddr(s)[1]))

def filterEmails(entries):
    return list(filter(fun, entries))

def main():
    n = int(input())
    entries = []
    for item in range(n):
        entries.append(input())
    filtered = filterEmails(entries)
    for item in filtered:
        print(item)
if __name__ == '__main__':
    main()
