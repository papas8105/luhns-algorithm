'''This is a short program to test the validity of a SIM card navigate python 3 to the folder that contains the file and type luhn()'''
def luhn():
  card_id = input('Enter the card identification number: ')
  #create a list with the digits that consist the card id number
  digits = []
  for i in range(len(card_id)):
    digits.append(int(card_id[i]))
  #Create the sublists with the odd indexed digits and even indexed digits *note that python counts from 0
  odd_index_digits = digits[0::2];even_index_digits = digits[1::2];
  #Sum of the odd indexed digits
  odd_digits_sum = sum(odd_index_digits)
  #Every second digit of the card_id must be doubled and appended to a new list
  doubled_even_index = []
  for i in range(len(even_index_digits)):
    doubled_even_index.append(2*even_index_digits[i])
  #In the new list if an element is greater that 9 it should be substituted with the sum of its two digits
  for i in range(len(doubled_even_index)):
    if doubled_even_index[i]>9:
      doubled_even_index[i] =  (doubled_even_index[i]%10) + 1 
  #We need to sum the odd_digits_sum and the new doubled_even_index sum
  total_sum = odd_digits_sum + sum(doubled_even_index)
  #Check if the total sum modulo 10 is 0 i
  check = total_sum%10;
  if check == 0:
    return 'The card is valid'
  else:
    return 'The card is invalid'
