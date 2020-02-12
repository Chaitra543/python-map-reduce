s = open("02.txt","r")
r = open("03.txt", "w")

count = 0
thiskey = ""



for line in s:
  data = line.strip().split('\t')
  paymentType, item = data

  if thiskey == "":
    if paymentType:
      thiskey = paymentType

  # increment the count whenever the existing key and the incoming key are same 
  
  if paymentType == thiskey:
    count = count + 1
  else:
    r.write( thiskey + '\t' + str(count)+'\n')
    # start over when changing keys
    thiskey = paymentType
    count = 1

  # output final entry

r.write( thiskey + '\t' + str(count)+'\n')

s.close()
r.close()