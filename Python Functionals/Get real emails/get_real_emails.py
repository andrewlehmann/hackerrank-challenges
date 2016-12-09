def finals(emails):
    unsorted = []    
    bool_list = list(map(lambda x: x.count('@') == 1 and x.split('@', 1)[1].count('.') == 1, emails))
    for i in range(0, len(emails)):
        if bool_list[i] == True:
            username, rest = emails[i].split('@', 1)
            domain, extension = rest.split('.', 1)
            if username.replace('-', '').replace('_', '').isalnum():
                if extension.isalnum():
                    unsorted.append(emails[i])
    return sorted(unsorted)   
            

if __name__ == '__main__':
    emails = []
    for _ in range(input()):
        emails.append(raw_input().strip())
    output = finals(emails) #finish return statement
    print output