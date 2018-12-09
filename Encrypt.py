# def main():
#   message ="Hello my friend"
#   encryptedMessage = ""
#   decryptedMessage = ""
#   key = "as"
#   createTable()
#   mappedKey = ""
#
#   j = 0
#
#   for i in message:
#
#     if i == chr(32):
#       mappedKey += chr(32)
#     else:
#       if j < len(key):
#         mappedKey += key[j]
#         j += 1
#       else:
#         j = 0
#         mappedKey += key[j]
#         j += 1
#
#   message = message.upper()
#   mappedKey = mappedKey.upper()
#
#   print(message)
#   print(mappedKey)
#
#   encryptedMessage = encryption(message, mappedKey)
#
#   print(encryptedMessage)
#
#   decryptedMessage = decryption(encryptedMessage, mappedKey)
#
#   print(decryptedMessage)




def createTable():
  w, h = 26, 26;
  table = [[0 for x in range(w)] for y in range(h)]
  x = 0
  for i in range(26):
      for j in range(26):

        if ( (i+65)+j > 90):

          x = ( (i+65) + j) -26
          table[i][j] = x
        else:
          x = (i+65)+j
          table[i][j] = x

  return table


def encryption(message, mappedKey):
  vigenereTable = createTable()
  encryptedMsg = ""

  for i in range(len(message)):

    if message[i] == chr(32):
      encryptedMsg += " "
    else:
      if ord(message[i]) > 47 and ord(message[i]) <57:
        encryptedMsg += message[i]
      else:
        if ord(message[i]) > 64 and ord(message[i]) < 91:
          encryptedMsg += chr(vigenereTable[((ord(message[i]))-65)][((ord(mappedKey[i]))-65)])
        else:
          encryptedMsg += message[i]

  return encryptedMsg


def count(charAt, charAt2):
  counter = 0
  temp = ""
  for i in range(26):

    if (charAt + i) > 90:
      temp += chr(charAt +(i-26))

    else:
      temp += chr(charAt+i)
  for i in range(len(temp)):

    if temp[i] == chr(charAt2):
      break
    else:
      counter = counter + 1

  return counter

def decryption(encryptedMessage, mappedKey):
  vigenereTable = createTable()
  decryptedMsg = ""

  for i in range(len(encryptedMessage)):
    if encryptedMessage[i] == chr(32):
      decryptedMsg += " "
    else:
      if ord(encryptedMessage[i]) > 64 and ord(encryptedMessage[i]) < 91:
        decryptedMsg += chr(65 + count(ord(mappedKey[i]), ord(encryptedMessage[i]) ))
      else:
        decryptedMsg += encryptedMessage[i]

  return decryptedMsg





# main()
