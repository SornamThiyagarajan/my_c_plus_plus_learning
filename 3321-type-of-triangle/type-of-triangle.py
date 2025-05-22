class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums

        # First check if it's a valid triangle
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"

        # Now determine the type
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"