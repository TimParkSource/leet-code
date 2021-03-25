class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        result = 0
        x = 0
        while x < len(s):
            if x < len(s) -1:
                if s[x] == "I" and s[x+1] == "V":
                    result += 4
                    x+=1
                elif s[x] == "I" and s[x+1] == "X":
                    result += 9
                    x+=1
                elif s[x] == "X" and s[x+1] == "L":
                    result += 40
                    x+=1
                elif s[x] == "X" and s[x+1] == "C":
                    result += 90
                    x+=1
                elif s[x] == "C" and s[x+1] == "D":
                    result += 400
                    x+=1
                elif s[x] == "C" and s[x+1] == "M":
                    result += 900
                    x+=1
                else:
                    result += roman[s[x]]
            else:
                result += roman[s[x]]
            x+=1
            print(result)
        return result

sol = Solution()
print(sol.romanToInt("III"))