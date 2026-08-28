class Solution:

    def encode(self, strs):
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):

            j = i

            # Find the '#'
            while s[j] != "#":
                j += 1

            # Get the length
            length = int(s[i:j])

            # Get the actual word
            word = s[j + 1 : j + 1 + length]

            result.append(word)

            # Move i to the beginning of next encoded word
            i = j + 1 + length

        return result