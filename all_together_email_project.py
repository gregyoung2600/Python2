Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> email = input("What is your email address? ").strip()
What is your email address? bkguest@bestbuy.com
>>> user = email[:email.index("@")]
>>> print(user)
bkguest
>>> domain = email[email.index("@"):]
>>> print(domain)
@bestbuy.com
>>> domain = email[email.index("@" ) + 1:]
>>> print(domain)
bestbuy.com
>>> string = "Your email address is {}. Your user name is {}, and your domain name is {}."
>>> output = string.format(email,user,domain)
>>> print(output)
Your email address is bkguest@bestbuy.com. Your user name is bkguest, and your domain name is bestbuy.com.
>>> 



>>> email = input("What is your email address? ").strip("./")
What is your email address? ...../////go daddy.com....////
>>> print(email)
go daddy.com
