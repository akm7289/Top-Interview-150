class Solution(object):
    def signed_int_to_32bit_binary(self,num):
        # Convert negative numbers to 32-bit two's complement
        if num < 0:
            num += 2 ** 32
        # Convert the number to its binary representation
        binary = bin(num)[2:]
        # Pad the binary representation with zeros to make it 32 bits long
        padded_binary = binary.zfill(32)
        return padded_binary

    def signed_binary_to_int(self,binary):
        # Convert binary to integer
        result = int(binary, 2)
        # Check if the most significant bit is 1 (indicating a negative number)
        if binary[0] == '1':
            # Convert the result to a negative number
            result -= 1 << len(binary)
        return result

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumsOfOnes = [0] * 32
        result = ['0'] * 32
        for num in nums:
            binaryNum = self.signed_int_to_32bit_binary(num)
            for i in range(32):
                sumsOfOnes[i] = sumsOfOnes[i] + int(binaryNum[i])
        returnValue = 0

        for i in range(32):
            result[i] = str(sumsOfOnes[i] % 3)

        bin=''.join(result)
        return self.signed_binary_to_int(bin)

if __name__=='__main__':
    # Example usage
    print(Solution().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))