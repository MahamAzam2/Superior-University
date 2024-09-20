
#TASK-1 

# def remove_punctuation(n):
#     punctuation = '''!()-[]{}?\/$#@<>*+=-_.,:;@&'''
#     result = "" 
#     for char in n:
#         if char not in punctuation:
#             result = result + char
#     return result
# user_input ="hello, maham! how's everything going?"
# remove_punctuation = remove_punctuation(user_input)
# print(remove_punctuation)

#TASK-2

# def sort_words(text):
#     words = text.split()
    
#     for i in range(len(words)):
#         for j in range(0,len(words)-i-1):
#             if words[j] > words[j+1]:
#                 words[j], words[j+1] = words[j+1], words[j]
#     return " ".join(words)
# input = "maham noor ali ayesha aqsa"
# sorted_words = sort_words(input)
# print(sorted_words)

#task3

# def luhn_code():
#     def digitsof(number):
#         return [int(digit) for digit in str(number)]

#     cardnumber = input("enter the card number: ")
#     digits = digitsof(cardnumber)
#     last_digit = digits.pop()#will remove the last digit
#     digits = digits[::-1]# reverse the digits after rempving the last one
    
#     for i in range(0,len(digits),2):
#         digits[i] *= 2
#         if digits[i] > 9:
#             digits[i] -= 9
            
#     total = sum(digits) + last_digit
            
#     if total % 10 == 0:
#         print("card number is valid: ")
    
#     else:
#         print("card number is not valid: ")
        
# luhn_code()
        





