class Solution_1:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = []
        cow = 0
        dict1 = {}
        dict2 = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull.append(secret[i])
        for iterm in secret:
            if iterm not in dict1:
                dict1[iterm] = 1
            else:
                dict1[iterm] += 1
        for iterm in guess:
            if iterm not in dict2:
                dict2[iterm] = 1
            else:
                dict2[iterm] += 1
        for iterm in dict1:
            if iterm in dict2:
                cow += (min(dict1[iterm],dict2[iterm]) - bull.count(iterm))
        return ("%dA%dB" % (len(bull),cow))


class Solution_2:
    def getHint(self,secret,guess):
        bull = 0
        cow = 0
        dict1 = [0]*10
        dict2 = [0]*10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
        for i in range(len(secret)):
            dict1[int(secret[i])] += 1
            dict2[int(guess[i])] += 1
        for i in range(10):
            cow += min(dict1[i],dict2[i])
        cow = cow - bull
        return ("%dA%dB" % (bull,cow))


def stringToString(input):
    return input[1:-1]


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            secret = stringToString(line)
            line = next(lines)
            guess = stringToString(line)

            ret = Solution_2().getHint(secret, guess)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()