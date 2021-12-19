# extract the number 0.8475
text = "X-DSPAM-Confidence:    0.8475"
x= text.find('0')
y= text.find('5',x)
answer=text[x:y+1] # <=  <
fanswer=float(answer)
print(fanswer)
# answer
str = "X-DSPAM-Confidence:    0.8475"
ipo = str.find(':')
piece = str[ipo+6:] # : to the end
value=float(piece) # string >> numbers
print(value)
