class IsPalindrome:

    # This approach works. But it has data pre processing that uses more computing and memory.
    def sol1(self, s: str) -> bool:

        s_clean = ""
        # data cleaning
        for c in s:
            if c.isalnum():
                s_clean += c.lower()

        if s_clean == "":
            return True

        for i in range(len(s_clean)):
            rear_i = (len(s_clean) - 1) - i
            if i > rear_i or i ==  rear_i:
                return True
            elif s_clean[i] != s_clean[rear_i]:
                return False

    # more optimized solution
    def sol2(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.is_alnum(s[left]):
                left += 1
            while right > left and not self.is_alnum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True



    def is_alnum(self, c:str) -> bool:
        return (ord('a') <= ord(c) <= ord('z')
        or ord('A') <= ord(c) <= ord('Z')
        or ord('0') <= ord(c) <= ord('9'))