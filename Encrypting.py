number = 54 # 110110
key = 104 # 1101000

# Write in this version if you wnat User write number and key
# number = int(input("Write the number you want to encrypt: ")) #number is swaping in binary
# key = int(input("Write the key for encrypt: ")) #key is swaping in binary

# XOR binary encrypt
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
print(f"Encrypted = {encrypt}")

#Decrypted
print("Decrypting = Encrypted ^ Key")
decrypt = encrypt ^ key 
print(f"Decrypted = {decrypt}")