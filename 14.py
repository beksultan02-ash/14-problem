import re
def find(s):
     charRe  = '^[a-zA-Z0-9_]*$'
     if  re.search(charRe, s):
         return "found a match"
     else :
         return "not matched"    


s= input()
print (find(s) )