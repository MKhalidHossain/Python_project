l, u, s, d = 0, 0, 0, 0
p= input("Input your password :")

if (len(p) >= 8):
    for i in p:

        # counting lowercase alphabets
        if (i.islower()):
            l += 1

            # counting uppercase alphabets
        if (i.isupper()):
            u += 1

            # counting digits
        if (i.isdigit()):
            d += 1

            # counting the mentioned special characters
        if (i == '@' or i == '$' or i == '_'):
            s += 1
if (l >= 1 and u >= 1 and s >= 1 and d >= 1 and l + s + u + d == len(p)):
    print("Valid Password")
else:
    print("Invalid Password")