input="compuuter"
vowels="aeiou"
output=""
for x in input:
  if x in vowels:
    if input[input.index(x)+1] == x:
      output = output+x
    else:
      pass
  else:
    output = output+x
print(output)