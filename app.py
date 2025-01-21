number = 54 #110110
key = 106  #1101010

encrypt = number ^ key
print(encrypt) #92 - 1011100

encrypt = encrypt ^ key 
print(encrypt) # 54 - 110110