string = input().lower()
var = ".".join([v for v in string if not v in "aiueoy"])

print ("." + var)