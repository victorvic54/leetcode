class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of 1's in num2
        num2_ones = bin(num2).count('1')

        # Get the binary representation of num1 as a list of bits
        num1_bits = list(bin(num1)[2:])

        result_bits = []

        for bit in num1_bits:
            if bit == '1' and num2_ones > 0:
                result_bits.append('1')
                num2_ones -= 1
            else:
                result_bits.append('0')

        for i in range(len(result_bits) - 1, -1, -1):
            if num2_ones == 0:
                break
            if result_bits[i] == '0':
                result_bits[i] = '1'
                num2_ones -= 1

        # Add extra 1's to the most significant positions if needed
        if num2_ones > 0:
            result_bits = ['1'] * num2_ones + result_bits

        return int(''.join(result_bits), 2)
