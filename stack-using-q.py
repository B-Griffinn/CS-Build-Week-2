class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # keeps track of the size of our Q/Stack
        self.size = 0

        # create a stroage to use in the Q
        # naive aproach is a []
        self.storage = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # print("pushing")
        # print(x)
        self.storage.append(x)
        # print(self.storage)
        self.size += 1
        # return self.storage

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # print("popping")

#         removed_head = self.storage[0]
#         # print('removed_head', removed_head)
#         self.size -= 1

#         return removed_head

        return self.storage.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        # print("peeking")

        return self.storage[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.storage:
            return True
        return False

#         if self.size == 0:
#             return True

#         if self.size <= 0:
#             return True
#         elif self.size > 1:
#             return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
