Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

Constant, because no matter what the capacity is, the steps are always the same.

2. What is the space complexity of your ring buffer's `append` function?

Constant because the array has a max capacity and each time append is called, it overrides the oldest value in the array so the array doesn't scale with inputs.

3. What is the runtime complexity of your ring buffer's `get` method?

O(n) because it scales with how many inputs are in the array.

4. What is the space complexity of your ring buffer's `get` method?

O(n) because at best it can be constant but there is a chance it needs to loop through to the end of the array and check each number to make sure its not none.


5. What is the runtime complexity of the provided code in `names.py`?

O(n^2) because there are two for loops that it has to loop through.

6. What is the space complexity of the provided code in `names.py`?
O(n^2)

7. What is the runtime complexity of your optimized code in `names.py`?

O(log n) because it sorted the data into a heap and then took that out into a sorted array. Then it just compares the two sorted arrays to see if the values match.

8. What is the space complexity of your optimized code in `names.py`?

O(log n)
