class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #We can use a stack to keep track of the time taken for each car to reach the target. 
        #We will iterate through the cars in reverse order of their position and for each car, we will calculate the time taken to reach the target. 
        #If the time taken for the current car is greater than or equal to the time taken for the car in front of it, then they will form a fleet and we will not add the current car to the stack. 
        #If the time taken for the current car is less than the time taken for the car in front of it, then we will add the current car to the stack. 
        #Finally, we will return the number of fleets formed which is equal to the size of the stack.
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)