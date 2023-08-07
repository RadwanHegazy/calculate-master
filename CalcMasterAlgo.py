'''
Create by : Radwan Gaber Hijazi

facebook : https://www.facebook.com/radwan.gaber.hijazi
'''


import random
import fractions



class CalcMaster :


    def __init__(self) :
        self.lits_of_games = []

    # Easy Level

    def Easy_Level (self) :
        my_numbers = []
        n1 = 0

        for i in range(4) :
            n1 = n1 + 2
            my_numbers.append(n1)

        for i in range(50) :
            operations = ['-','+','/','*']
            first_number = int(my_numbers[random.randint(0,len(my_numbers) - 1 )])
            secend_number = int(my_numbers[random.randint(0,len(my_numbers) - 1)])
            if secend_number > first_number :
                game = f"X {operations[random.randrange(0,4)]} {first_number} = {secend_number}"
                self.lits_of_games.append(game)

        points = 0

        for i in self.lits_of_games :
            

            problem = str(i).split(' ')
            
            num_1 = int(problem[2])
            num_2 = int(problem[-1])

            #  [ - ]
            if problem[1] == '-' :
                result = num_1 + num_2
            
            #  [ / ]
            if problem[1] == '/' :
                result = num_1 * num_2
            
            #  [ x ]
            if problem[1] == '*' :
                result = fractions.Fraction(num_2 / num_1).limit_denominator()
            
            #  [ + ]
            if problem[1] == '+' :
                result = num_2 - num_1
            
            print(i)
            print('X = ',result)
            
            print('_'*30)



    def in_block_operation(self,num_1, num_2, operation) :
        num_1 = int(num_1)
        num_2 = int(num_2)
        
        if operation == '-' :
            Sum = num_1 - num_2
        
        if operation == '+' :
            Sum = num_1 + num_2
        
        if operation == '*' :
            Sum = num_1 * num_2
        
        if operation == '/' :
            Sum =  num_1 / num_2
        
        return Sum

    # Medium Level
    def Medium_Level (self) :
        my_numbers2 = []
        n2 = 0

        for i in range(20) :
            n2 = n2 + 2
            my_numbers2.append(n2)

        for i in range (15) :
            operations = ['-','+','/','*']
            first_number = int(random.randrange(0,len(my_numbers2) - 1))
            third_number = int(random.randrange(0,len(my_numbers2) - 1))
            secend_number = int(random.randrange(0,len(my_numbers2) - 1))
            calc_operation1 = operations[random.randrange(0,4)]
            calc_operation2 = operations[random.randrange(0,4)]
            game = f"X {calc_operation1} ( {third_number} {calc_operation2} {first_number} ) = {secend_number}"
            self.lits_of_games.append(game)


        for i in self.lits_of_games :
            problem = str(i).split(' ')
            in_block = self.in_block_operation(num_1=problem[3],num_2=problem[5],operation=problem[4])
            last_number = int(problem[-1])

            #  [ - ]
            if problem[1] == '-' :
                result = last_number + in_block

            
            #  [ / ]
            if problem[1] == '/' :
                result = last_number * in_block
            
            #  [ x ]
            if problem[1] == '*' :
                result = last_number / in_block
            
            #  [ + ]
            if problem[1] == '+' :
                result = fractions.Fraction(last_number - in_block).as_integer_ratio()

            print(' '.join(problem))
            print('X = ',result)
            print('_'*20)

    # Hard Level
    def Hard_level (self):
        my_numbers = []
        n1 = 0

        for i in range(4) :
            n1 = n1 + 2
            my_numbers.append(n1)

        for i in range(50) :
            operations = ['-','+','*']
            first_number = random.randint(1,15)
            secend_number = random.randint(1,15)
            third_number = random.randint(1,15)
            fourth_number = random.randint(1,15)
            o1 = operations[random.randrange(0,2)]
            o2 = operations[random.randrange(0,3)]
            if secend_number > first_number :
                game = f"X {o1} ( {first_number} {o2} {third_number} ) / {fourth_number} = {secend_number}X"
                self.lits_of_games.append(game)


        for i in self.lits_of_games :
            problem = str(i).split(' ')
            
            down_num = int(problem[8])
            last_number = int(problem[-1].split('X')[0])

            in_block_number = self.in_block_operation(num_1=problem[3],num_2=problem[5],operation=problem[4])
            result_1 = ( down_num * last_number ) - 1
            u_number = int(f'{problem[1]}1') * in_block_number
            try :

                prob = ' '.join(problem)
                answer = fractions.Fraction( u_number / result_1).limit_denominator()
                print(u_number / result_1)
                print(f"{prob}\n{answer}\n{ str('_')*10 }")

            except ZeroDivisionError :
                pass    



# For Easy Level
# CalcMaster().Easy_Level()

# For Medium Level
# CalcMaster().Medium_Level()

# For Hard Level
# CalcMaster().Hard_level()