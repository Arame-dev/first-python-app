number = 54 #110110
key = 106  #1101010

# ^ - XOR
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

#Encrypted
encrypt = number ^ key
print(f"Encrypted {encrypt}") #92 - 1011100

#Decrypted
encrypt = encrypt ^ key 
print(f"Decrypted {encrypt}") # 54 - 110110