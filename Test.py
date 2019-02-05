while True:
    print('hey there')
    try:
        val1=int(input('input a number:'))
    except ValueError:
        val1=int(input('please input a number:'))
    try:
        val2=int(input('and another:'))
    except ValueError:
        val2=int(input('please input a number:'))
    sum=val1 +val2
    print('The sum of those values is:', sum)
    again=input('add again?:')
    if again=='no':
        break
