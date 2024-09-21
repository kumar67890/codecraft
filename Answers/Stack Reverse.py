# Function to insert an element at the bottom of a stack
def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        # Pop all elements and hold them in the recursion stack
        temp = stack.pop()
        insert_at_bottom(stack, item)
        # Push all elements back after inserting the item at the bottom
        stack.append(temp)

# Function to reverse the stack using recursion
def reverse_stack(stack):
    if len(stack) > 0:
        # Pop the top element and reverse the remaining stack
        temp = stack.pop()
        reverse_stack(stack)
        # Insert the popped element at the bottom of the stack
        insert_at_bottom(stack, temp)

# Example usage
stack = [1, 2, 3, 4, 5]
print("Original Stack:", stack)

reverse_stack(stack)
print("Reversed Stack:", stack)