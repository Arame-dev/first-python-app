number = 54 #110110
key = 106  #1101010

# ^ - XOR
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

print("Encrypting and Decrypting with XOR")
print("Number ^ Key")
print(f"Number \'{number}\', Key \'{key}\'")

#Encrypted
encrypt = number ^ key
print(f"Encrypted = {encrypt}") #92 - 1011100

#Decrypted
print("Decrypting = Encrypted ^ Key")
decrypt = encrypt ^ key 
print(f"Decrypted = {encrypt}") # 54 - 110110