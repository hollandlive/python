# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
score = raw_input("Enter a Score between 0.0 and 1.0:")
s = float(score)
if s > 1:
    print 'The range is between 0.0 and 1.0'
elif s < 0:
    print 'The range is between 0.0 and 1.0'
else:
    if 0.9 < s <= 1:
        print 'A'
    elif 0.8 <= s < 0.9:
        print 'B'
    elif 0.7 <= s < 0.8:
        print 'C'
    elif 0.6 <= s < 0.7:
        print 'D'
    else:
        print 'F'


