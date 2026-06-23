class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = "".join(strs)
        encoded += "|"

        for s in strs:
            encoded += str(len(s)) + "#"

        return encoded

    def decode(self, s: str) -> List[str]:
        
        lengths_str = s.split("|")
        lengths = (lengths_str[-1].split("#"))[:-1]

        start = 0
        decoded = []

        for length in lengths:
            decoded.append(s[start:(start + int(length))])
            start += int(length)

        return decoded


