class Solution:



    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maximumArea = 0

        for pos, height in enumerate(heights):
            added_pos = pos
            while stack and stack[-1][0] > height:
                local_height , added_pos = stack.pop()
                maximumArea = max(maximumArea, local_height * (pos - added_pos))

            stack.append((height, added_pos))

         

        for h, i in stack:
            maximumArea = max(maximumArea, h * (len(heights) - i))



        return maximumArea