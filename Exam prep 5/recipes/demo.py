# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start <= self.end:
#             i = self.start
#             self.start += 1
#             return i
#         else:
#             raise StopIteration()
#
#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)
#
#

class Reverse_iter:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        x = self.obj.reverse()
        if len(x)< 
