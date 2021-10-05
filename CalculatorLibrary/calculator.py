from robot.api.deco import keyword,library
@library(scope='GLOBAL', auto_keywords=True)
class CalculatorKeywords:
    def __init__(self) -> None:
        pass
    @keyword
    def add_numbers2(self,num1, num2):
        return num1 + num2
    @keyword
    def subtract_numbers(self,num1, num2):
        return num1 - num2
    @keyword
    def multiply_numbers(self,num1, num2):
        return num1 * num2
    @keyword
    def divide_numbers(self,num1, num2):
        return num1 / num2
