# example gradient of real function 
# real function : (x-3)^2 +5
gradient = lambda x: (2*x) -6
# starting number
x = 2
# our alpha number or learning rate
learning_rate = 0.1
# for tracking number of attempt
i = 1
# main loop
while True:
    # put old x in variable to track it 
    old_x= x
    # calculate new x
    x = x - learning_rate*gradient(x)
    # calculate diffrence
    diffrence = x-old_x
    # condition for our desirable answer
    if diffrence < 0.005:
        break
    print(f'attempt {i} new x: {x:.3f} and old x: {old_x:.3f}')
    i+=1
