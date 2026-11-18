class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        n = len(heights)
        mono_inc_stack = []
        pse = [-1] * n
        nse = [n] * n

        for i in range(len(heights)):
            while mono_inc_stack and heights[mono_inc_stack[-1]] >= heights[i]:
                nse[mono_inc_stack.pop()] = i
            if mono_inc_stack:
                pse[i] = mono_inc_stack[-1]
            mono_inc_stack.append(i)
        
        # print(pse, nse)
        for i in range(len(heights)):
            ns = nse[i]
            ps = pse[i]
            # print(ns, ps)
            width = ns - ps - 1
            area = width * heights[i]
            # print(width, heights[i], area)
            if area > largest_area:
                largest_area = area

        return largest_area


