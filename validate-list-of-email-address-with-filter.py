ltrs_lower='abcdefghijklmnopqrstuvwxyz'
ltrs_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbs = '0123456789'
smbs='_-'
username_cond = ltrs_lower + ltrs_upper + numbs + smbs
webname_cond =  ltrs_lower + ltrs_upper + numbs
ext_cond = ltrs_lower + ltrs_upper

def fun(s):
    ls = list(s)
    if '@' in ls:
        dog_index = ls.index('@')
        username_ls = ls[:dog_index]
        if len(username_ls) > 0 and all( (x in username_cond) for x in username_ls):
            after_dog_ls = ls[dog_index+1:] 
            if '.' in after_dog_ls:
                dot_index = after_dog_ls.index('.')
                webname_ls = after_dog_ls[:dot_index]
                ext_ls = after_dog_ls[dot_index+1:]
                if len(webname_ls) > 0 and all( (x in webname_cond) for x in webname_ls):
                    if len(ext_ls) <= 3 and len(ext_ls) > 0 and all( (x in ext_cond) for x in ext_ls):
                        return True
    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)