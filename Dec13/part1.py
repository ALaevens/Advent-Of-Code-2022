from enum import Enum

class Result(Enum):
    OUTOFORDER = 1
    INORDER = 2
    UNDECIDED = 3

ENABLE_DEBUG = False

def message(depth, *args, **kwargs):
    if ENABLE_DEBUG:
        print(f"{'  '*depth}", *args, **kwargs)

def compare(left, right, depth=0):
    message(depth, f"- Compare {left} vs {right}")
    if type(left) == int and type(right) == int:
        if left == right:
            message(depth, "-> Undecided")
            return Result.UNDECIDED
        elif left < right:
            message(depth, "-> In Order")
            return Result.INORDER
        else:
            message(depth, "-> Out of Order")
            return Result.OUTOFORDER

    elif type(left) == list and type(right) == list:
        i = 0
        left_len = len(left)
        right_len = len(right)

        while i < min(left_len, right_len):
            result = compare(left[i], right[i], depth+1)

            if result != result.UNDECIDED:
                return result
            
            i += 1
        
        # a list has now ran out of inputs
        if left_len == right_len:
            message(depth, "-> Undecided")
            return Result.UNDECIDED

        elif left_len < right_len:
            message(depth, "-> In Order")
            return Result.INORDER

        else:
            message(depth, "-> Out of Order")
            return Result.OUTOFORDER

    elif type(left) != type(right):
        message(depth, "-> Type mismatch")

        if type(left) == list:
            return compare(left, [right], depth+1)
        
        else:
            return compare([left], right, depth+1)
        


with open("input.txt") as f:
    packets = []

    for line in f:
        line = line.strip()

        if line != "":
            packets.append(eval(line))
    

    index_sum = 0
    for i in range(len(packets) // 2):
        left = packets[2*i]
        right = packets[2*i + 1]
        
        result = compare(left, right)

        if result == Result.INORDER:
            index_sum += i+1

    print(index_sum)