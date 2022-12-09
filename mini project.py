n=int(input("Enter number of e-mails:"))
for i in range(n):
    email = input("Enter Your Email: ").strip()
    username =email[:email.index("@")]
    domain_name = email[email.index("@")+1:]
    result= (f"username: '{username}' and  domain name '{domain_name}'"
print(result)
