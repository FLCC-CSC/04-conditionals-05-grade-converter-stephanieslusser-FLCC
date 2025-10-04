# FILE NAME - grade_converter.py

# NAME: Stephanie Slusser
# DATE: 10/04/2025
# BRIEF DESCRIPTION: Grade converter



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print('===== Grade Converter =====')
grade = int(input('Enter a numerical grade (1-100): '))

if grade < 65:
    print('F')
elif 65 <= grade < 70:
    print ('D')
elif 70 <= grade < 80:
    print ('C')
elif 80 <= grade < 90:
   print ('B')
elif 90 <= grade <= 100:
   print ('A')
elif 100 < grade:
   print ('A+')
else:
   print('F')

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?
Pay attention to when numbers are to be included in a grade tier. [ and ( look the same if you aren't looking carefully.






'''
