import random

class Solution:

    def __init__(self, nums):
        self.ori = nums

    def reset(self):
        return self.ori
        """
        Resets the array to its original configuration and return it.
        """

    def shuffle(self):
        ramdom_times = random.randrange(0, len(self.ori))
        chacnge_x = [random.randrange(0, len(self.ori)) for i in range(ramdom_times)]
        chacnge_y = [random.randrange(0, len(self.ori)) for i in range(ramdom_times)]

        shuffle_list = self.ori
        for i in range(len(chacnge_x)):
            temp = shuffle_list[chacnge_x[i]]
            shuffle_list[chacnge_x[i]] = shuffle_list[chacnge_y[i]]
            shuffle_list[chacnge_y[i]] = temp

        return shuffle_list




obj = Solution([])
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)