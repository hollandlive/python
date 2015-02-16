#my python program salary 1.0. program calculates ur weekly salary. it pays you 1.5 times extra money for extra hours (above 40 hours)
print 'Step 2\n', 'I gonna calculate ur salary,\n'
hours = raw_input('Enter hours u worked this week\n')
hours = float(hours)
rate = raw_input('Enter ur rate\n')
rate = float(rate)
print 'your hours worked: \n', hours, '\n', 'ur rate is: \n', rate, ' per hour\n'
if hours <= 40:
    sal = hours * rate
    print 'ur salary this week is ', sal
else: 
    hours_extra = hours - 40
    sal = ((hours - 40) * rate * 1.5) + (40 * rate)
print 'congrats Mr\n, u worked ', hours, '\n', ' ur salary is \n', sal
