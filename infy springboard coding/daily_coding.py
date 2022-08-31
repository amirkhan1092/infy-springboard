'''
This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
'''
def rotate(ls: list)-> list:
    'rotate the elements'
    ls.append(ls.pop(0))

def permutations(ls: list)->list:
    '''permutations combinations'''
    for i in range(len(ls)):
        ls[i]

lst = [1, 2, 3]
rotate(lst)
rotate(lst)

# out = permutations(lst)
# print(out)