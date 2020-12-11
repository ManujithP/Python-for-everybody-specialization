text = "X-DSPAM-Confidence:    0.8475"
pos1 = text.find('0')
pos2 = text.find('5')
bit = text[pos1:pos2+1]
no = float(bit)
print(no)
