# A program to find two numbers that can multiply and add
# to give another number

class QuadraticEquation:
    def __init__(self, b, c):
        self.c = c
        self.b = b

    def quad1(self):
        numbering = range(-100, 100)
        return numbering

    def quad2(self):
        numbering = range(-10, 9)
        return numbering

    def user__b(self):
        answer = self.b
        return answer

    def user__c(self):
        answer = self.c
        return answer


Quadrant = QuadraticEquation(2, 15)

num1 = Quadrant.quad1()
num2 = Quadrant.quad2()

b = Quadrant.user__b()
c = Quadrant.user__c()

for i in num1:
    for j in num2:
        if i * j == c:
            numbers = [i, j]
            if numbers[0] + numbers[1] == b:
                print(f"{numbers[0]} and {numbers[1]}")