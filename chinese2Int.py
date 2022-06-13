class HanziToNumber():
    def __init__(self):
        self.CN_NUM = {
            u'一': 1,
            u'二': 2,
            u'三': 3,
            u'四': 4,
            u'五': 5,
            u'六': 6,
            u'七': 7,
            u'八': 8,
            u'九': 9,

            u'零': 0,
            u'壹': 1,
            u'貳': 2,
            u'參': 3,
            u'肆': 4,
            u'伍': 5,
            u'陸': 6,
            u'柒': 7,
            u'捌': 8,
            u'玖': 9,

            u'貳': 2,
            u'兩': 2,
        }
        self.CN_UNIT = {
            u'十': 10,
            u'拾': 10,
            u'百': 100,
            u'佰': 100,
            u'千': 1000,
            u'仟': 1000,
            u'萬': 10000,
            u'萬': 10000,
            u'億': 100000000,
            u'億': 100000000,
            u'兆': 1000000000000,
        }

    def cn2dig(self, cn):
        lcn = list(cn)
        unit = 0  # 當前的單位
        ldig = []  # 臨時數組
        otherStr = ""
        while lcn:
            cndig = lcn.pop()
            if cndig in self.CN_UNIT: # python2: CN_UNIT.has_key(cndig)
                unit = self.CN_UNIT.get(cndig)
                if unit == 10000:
                    ldig.append('w')  # 標示萬位
                    unit = 1
                elif unit == 100000000:
                    ldig.append('y')  # 標示億位
                    unit = 1
                elif unit == 1000000000000:  # 標示兆位
                    ldig.append('z')
                    unit = 1
                continue
            elif cndig in self.CN_NUM:
                dig = self.CN_NUM.get(cndig)
                if unit:
                    dig = dig * unit
                    unit = 0
                ldig.append(dig)
            else :
                otherStr += cndig

        if unit == 10:  # 處理10-19的數字
            ldig.append(10)

        ret = 0
        tmp = 0
        while ldig:
            x = ldig.pop()
            if x == 'w':
                tmp *= 10000
                ret += tmp
                tmp = 0
            elif x == 'y':
                tmp *= 100000000
                ret += tmp
                tmp = 0
            elif x == 'z':
                tmp *= 1000000000000
                ret += tmp
                tmp = 0
            else:
                tmp += x
        ret += tmp
        return str(ret), otherStr


def main(str):
    num, unit = HanziToNumber().cn2dig(str)
    return num, unit
if __name__ == '__main__':
    main()