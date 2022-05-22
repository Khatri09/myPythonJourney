text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find('0')
rpos = text[atpos:]
rpos = float(rpos)
print(rpos)
