class StringEncodeAndDecode:

    seperator = ">*|*<"

    def Run(self, strs: list[str]):
        encodedStr = self.Encode(strs)
        print(f"Encoded String: {encodedStr}")

        decodedStrList = self.Decode(encodedStr)

        return decodedStrList

    def Encode(self, strs: list[str]) -> str:

        if len(strs) == 0:
            return ""

        resultStr = ""
        for i in range(len(strs)):
            resultStr += strs[i] + self.seperator

        return resultStr

    def Decode(self, s: str) -> list[str]:

        if s == "":
            return []

        seperatorLen = len(self.seperator)
        sLen = len(s)
        i = 0
        word = ""
        strs = []

        while i < sLen:
            if s[i] == self.seperator[0] and i + seperatorLen:
                if s[i:i + seperatorLen] == self.seperator:
                    strs.append(word)
                    word = ""
                    i = i + seperatorLen
                    continue

            word += s[i]
            i += 1

        if word != "":
            strs.append(word)

        return strs
