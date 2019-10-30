#!python3
import re
import pyperclip
phone_reg=re.compile(r'''(
(\+\d{2})?
(\s|-)?
(\d{5})
(\s|-)?
(\d{5})
)''', re.VERBOSE)

email_reg=re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

data=str(pyperclip.paste())
phone_numbers=[]
for groups in phone_reg.findall(data):
    phone = '-'.join([groups[1] , groups[3] , groups[5]])
    phone_numbers.append(phone)
emails=[]
for new in email_reg.findall(data):
   emails.append(new[0])

if len(phone_numbers)>0:
    pyperclip.copy('\n'.join(phone_numbers))
    print('Copied to clipboard:')
    print('\n'.join(phone_numbers))
else:
    print('no phone nubers found')
if  len(emails)>0:
    pyperclip.copy('\n'.join(emails))
    print('Copied to Clipboard')
    print('\n'.join(emails))
else:
    print('no emails found')


