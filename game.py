"""First game"""

import numpy as np

number = np.random.randint(1,101) #Random number initialized
count = 0

while True:
    count+=1
    predict_number = int(input("Take a shot of number: from 1 to 100: "))
    
    if predict_number > number:
        print("Predicted number is high")
        
    elif predict_number < number:
        print("Predicted number is low")
    
    else:
        print(f"You right. Number = {number} with {count} shots")
        break #The end

