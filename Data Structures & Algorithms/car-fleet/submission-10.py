class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        stack = []

        for car in cars:
            stack.append((target-car[0])/car[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        # print(cars)
        return len(stack)
