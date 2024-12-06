import sys
from random import randint
from os import system
import datetime                              
import random


#Modified Code : ***Yimber C 19/05/23
#Made in Ecuador : $%$%$%%$%%%

system("clear")
print(" \033[1;33m-----------------------------------")
print(" \033[1;33m| `7MM'''Yp, `7MMF'`7MN.   `7MF'  |")
print(" |   MM    Yb   MM    MMN.    M    |")
print(" |   MM    dP   MM    M YMb   M    |")
print(" |   \033[1;34mMM'''bg.   MM    M  `MN. M    |")
print(" |   MM    `Y   MM    M   `MM.M    |")
print(" | \033[1;31m  MM    ,9   MM    M     YMM    |")
print(" | .JMMmmmd9  .JMML..JML.    YM    |")
print(" |                                 |")
system("bash day")
print(" \033[1;31m-----------------------------------")
bin_format = input(" \033[1;34m> \033[1;32mBIN: \033[1;37m")
month = input(" \033[1;34m> \033[1;32mMONTH[7]: \033[1;37m")
year = input(" \033[1;34m> \033[1;32mYEAR[24]: \033[1;37m")
amount = input(" \033[1;34m> \033[1;32mAMOUNT: \033[1;37m")
print("")
system("bash loading")


def esValido(num_cart):
  sum = 0
  num_digits = len(num_card)
  pos_even_odd = num_digits & 1

  for i in range(0, num_digits):
    digit = int(card_num[i])
    if not ((i & 1) ^ pos_even_odd):
      digit = digit * 2
    if digit > 9:
      digit = digit - 9
    sum = sum + digit

  return (sum % 10 == 0)

def generate_cc(bin_format):
  cc = ""
  if len(bin_format) == 16:
    for i in range(15):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nInvalid character in the format: {}\n".format(bin_format))
        print("The bin format is: xxxxxxxxxxxxxxxx 16 digits\n")
        sys.exit()

    for i in range(10):
      verifier = cc + str(i)
      if isValid(verifier):
        cc = verifier
        break
      else:
        verifier = cc

  else:
    print("\nERROR: Please insert a valid bin\n")
    print("SOLUTION: The bin format is: xxxxxxxxxxxxxxxx 16 digits\n")
    sys.exit()

  return cc

def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

print("")
print("  \033[1;32m-------------------------------")
print(" \033[1;32m|       BIN        | DATE | CVV |")
print("  \033[1;32m-------------------------------")

def main():
  for i in range(int(amoubt)):                
    cc = generate_cc(bin_format)
    print(f" \033[1;32m| \033[1;37m{cc} \033[1;32m| \033[1;37m{month}/{year} \033[1;32m| \033[1;37m{ccv_gen()}\033[1;32m |")
main()

print("  \033[1;32m-------------------------------")
print("")
print("")
system("bash function")
