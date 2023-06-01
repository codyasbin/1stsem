class Quizgame:
    def __init__(self):
        self.Questions=[
            ["What is the Capital of Nepal?", "kathmandu", "chitwan","lumbini","pokhara",1],
            ["What is the temple in the nepal's highest position ?", "kedarnath","Badrinath","Pashupatinath","Muktinath", 4],
            ["Which language was used to create facebook?", "python","french","php","c#",3]
          ]
        self.levels= 1000  , 2000, 3000
        self.money= 0

    def start_game(self):
        for i in range (len(self.Questions)):
            question= self.Questions[i]

            print(f"1. {question[1]}     2.{question[2]}")
            print(f"3.{question[3]}  4..{question[4]}")

            reply =int(input("enter yor answer (1-4) or 0 to quit"))
            if reply ==0:
                if i ==0:
                    self.money=0
                else:
                    self.money= self.levels[i-1]
                break

            if reply ==question[-1]:
                print (f"correcr answer! you have won Rs. {self.levels[i]}")
                self.money =self.levels[i]
            else:
                print("wrong answer! ")
                break 
    
        else:
            print("Congratulations! youu have answered all the questions correctly.")

        print (f"your take home money is RS. {self.money} ")

game = Quizgame()
game.start_game()


 
        

