class StringEncodeAndDecode:

    seperator = "#"

    def run(self, strs: list[str]):
        encode_str = self.encode(strs)
        print(f"encoded string: {encode_str}")
        decoded_str_list = self.decode(encode_str)
        return decoded_str_list

    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for curr_str in strs:
            encoded_str += f"{len(curr_str)}{self.seperator}{curr_str}"
        return encoded_str

    def decode(self, encoded_str: str) -> list[str]:
        decoded_strs, i = [] , 0
        while i < len(encoded_str):
            j = i
            while encoded_str[j] != self.seperator:
                j += 1
            length = int(encoded_str[i:j])
            decoded_str = encoded_str[j+1:j+1+length]
            decoded_strs.append(decoded_str)
            i = j + 1 + length
        return  decoded_strs

