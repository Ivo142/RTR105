text = 'X-DSPAM-Confidence:    0.8475'
pos=text.find('0')
print(pos)
sos = text.find('5')
print(sos)
host = text[pos+1-sos]
print(host)
print(text[23:29])
