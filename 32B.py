code = input()
length = len(code)

i = 0
text = ""
while i < length:
  if code[i] == ".":
    text += "0"
    i += 1
  elif code[i:i+2] == "-.":
    text += "1"
    i+= 2
  else:
    text += "2"
    i+=2
    
print (text)

