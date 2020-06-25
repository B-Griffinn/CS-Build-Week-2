"""

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

"""


class Solution:
    def decodeString(self, s: str) -> str:
        # save the length of our string in a var
        input_length = len(s)

        # create a list to hold our variables that are non ints
        storage = []

        # loop through our entire input_length
        for i in range(input_length):

            # if we find a closing bracket, create a var to hold our soon to be decoded str
            if s[i] == ']':
                decoded_string = ""

                # begin decoding the string while looping backwards from ']' until we reach '['
                while storage[-1] != "[":

                    # pop the last item from our storage and concat it with our current decoded string
                    decoded_string = storage.pop() + decoded_string

                # then we can get rid of '['
                storage.pop()

                place_holder = ""

                # loop while we put together the entire length of place_holder
                while storage and storage[-1].isdigit():

                    # udpate our place_holder string to be the next item(s) after we read an integer
                    place_holder = storage.pop() + place_holder

                # finish decoding the string and append the result to our storage
                decoded_string = int(place_holder) * decoded_string
                storage.append(decoded_string)

            else:
                # append all the remaining chars in the storage arr
                storage.append(s[i])

        # return the joined version of our storage arr
        return "".join(storage)
