import hashlib
print (hashlib.algorithms_guaranteed)

str = "Altered2020"

result = hashlib.sha256(str.encode()) 
print(result.hexdigest()) 

result = hashlib.sha384(str.encode())
print(result.hexdigest()) 

result = hashlib.sha224(str.encode()) 
print(result.hexdigest())

result = hashlib.sha512(str.encode()) 
print(result.hexdigest()) 

result = hashlib.sha1(str.encode()) 
print(result.hexdigest())
