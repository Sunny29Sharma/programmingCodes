s = "abcABCd"
upper = 0
lower = 0
for i in range(len(s)):

    # For lower letters
    if (ord(s[i]) >= 97 and
            ord(s[i]) <= 122):
        lower += 1

    # For upper letters
    elif (ord(s[i]) >= 65 and
          ord(s[i]) <= 90):
        upper += 1

print(f"upper : {upper}")
print(f"lower : {lower}")