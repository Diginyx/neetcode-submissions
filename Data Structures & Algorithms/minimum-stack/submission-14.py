import math

class MinStack:

    def __init__(self):
        self.minstack = []
        self.minstack_partner = []
        self.min = math.inf

    def push(self, val: int) -> None:
        if val <= self.min:
            self.min = val
            self.minstack_partner.append(val)
        self.minstack.append(val)

    def pop(self) -> None:
        val = self.minstack.pop() 
        if val == self.min:
            self.minstack_partner.pop()
            if len(self.minstack_partner) > 0:
                self.min = self.minstack_partner[-1]
            else:
                self.min = math.inf

    def top(self) -> int:
        if len(self.minstack) > 0:
            return self.minstack[-1]

    def getMin(self) -> int:
        if len(self.minstack_partner) > 0:
            return self.minstack_partner[-1]
        else:
            return self.minstack[-1]
