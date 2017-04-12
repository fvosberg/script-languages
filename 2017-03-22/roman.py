class Roman:
    letterDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }


    def __init__(self, value):
        self.value = value

    def toArabic(self):
        result = 0
        lastArabic = 0
        numberOfLastArabic = 0
        for c in self.value:
            currentArabic = Roman.letterDict[c]
            result += currentArabic

            if currentArabic > lastArabic:
                result -= numberOfLastArabic * 2 * lastArabic


            if lastArabic == currentArabic:
                numberOfLastArabic += 1
            else:
                numberOfLastArabic = 1

            lastArabic = currentArabic
        return result
