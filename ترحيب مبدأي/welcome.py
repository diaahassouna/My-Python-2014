print 'Welcome to Dia\'a\'s Productions'
print '---------------------------------'
name = raw_input('Please Enter your name: ')
print 'Nice to meet you , ',name
gender = raw_input('Please define your gender: ')
if gender=='male':
    print "It's an honor to know you Mr.",name
elif gender=='female':
    print "I'm pleased to know you Ms.",name
else:
    print "I'm interested to know you , ",name
mast = raw_input('Please define your marital status: ')
if mast=='single':
    if gender=='male':
        print 'Being single is being free Mr.',name
    elif gender=='female':
        print 'Being single is being free Ms.',name
    else:
        print 'Being single is the best choice ,',name
if mast=='married' or mast=='in a relationship':
    if gender=='male':
        print 'I hope for you to be pleased with her Mr.',name
    elif gender=='female':
        print 'I hope for you to be happy with him Mrs.',name
    else:
        print 'I hope for you to have the best , ',name
age = input('Please define your age: ')
if age>0 and age<=10:
    print 'You\'re ',age,' ? , what a nice child you are'
elif age>10 and age<=20:
    if gender=='male':
        print 'You\'re ',age,' ? , young man'
    elif gender=='female':
        print 'You\'re ',age,' ? , young lady'
elif age<0:
    print 'that means you haven\'t born yet'
elif age>20:
    if gender=='male':
        print 'You\'re ',age,' ? good , Mr.',name
    elif gender=='female':
        if mast=='married' or mast=='in a relationship':
            print 'You\'re ',age,' ? good , Mrs.',name
        else:
            print 'You\'re ',age,' ? good , Ms.',name
    else:
        print 'You\'re ',age,' ? good , ',name
print '------------------------------------'
print 'Thank you for this conversation , Press Enter to Exit'
input()
