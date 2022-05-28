import random

i = 0
while i < 10:
    
    number_1 = random.randint(0,9)
    number_2 = random.randint(0,9)
    
    
    
    
    print('Ques{} {}*{}'.format(i+1,number_1,number_2))
    ans = int(input('Enter you answer: '))
    
    if ans==number_1*number_2:
         print('Right!')
    else :
        print('Wrong. The right answer is {}'.format(number_1*number_1))
        
    i+=1
             
         