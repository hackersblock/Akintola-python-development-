#this method is used when working with user inputs
while True:
    try:
        x = int(input('enter a number: '))
        x += 20
        break
    except:
        print('that\'s not a vaild number!')
    finally:
        print('\nAttempetd input\n')
print(x)