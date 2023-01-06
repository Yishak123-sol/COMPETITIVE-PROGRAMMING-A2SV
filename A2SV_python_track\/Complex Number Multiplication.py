class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        real_1, imaginary_1 = num1.split("+")
        real_2, imaginary_2 = num2.split("+")
        
        real_1 = int(real_1)
        real_2 = int(real_2)
        
        imaginary_1 = int(imaginary_1[:-1])
        imaginary_2 = int(imaginary_2[:-1])
        
        
        real = (real_1 * real_2) - (imaginary_1 * imaginary_2)
        imaginary = (real_1 * imaginary_2) + (real_2 * imaginary_1)

        complex_number = f"{str(real)}+{str(imaginary)}i"


        
        return complex_number
