#!/usr/bin/env python2
# -*- coding:utf-8 -*-
#
# 文件: pycode0x0015.py
# 功能: 将整数转成其英语形式
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.02.11

# 基本数字的英文字典
ENGLISH_NUMBER_NAMES = \
    {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
     '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
     '01': 'one', '02': 'two', '03': 'three', '04': 'four', '05': 'five',
     '06': 'six', '07': 'seven', '08': 'eight', '09': 'nine', '10': 'ten',
     '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
     '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen',
     '19': 'nineteen', '20': 'twenty', '21': 'twenty-one', '22': 'twenty-two',
     '23': 'twenty-three', '24': 'twenty-four', '25': 'twenty-five',
     '26': 'twenty-six', '27': 'twenty-seven', '28': 'twenty-eight',
     '29': 'twenty-nine', '30': 'thirty', '31': 'thirty-one',
     '32': 'thirty-two', '33': 'thirty-three', '34': 'thirty-four',
     '35': 'thirty-five', '36': 'thirty-six', '37': 'thirty-seven',
     '38': 'thirty-eight', '39': 'thirty-nine', '40': 'forty',
     '41': 'forty-one', '42': 'forty-two', '43': 'forty-three',
     '44': 'forty-four', '45': 'forty-five', '46': 'forty-six',
     '47': 'forty-seven', '48': 'forty-eight', '49': 'forty-nine',
     '50': 'fifty', '51': 'fifty-one', '52': 'fifty-two', '53': 'fifty-three',
     '54': 'fifty-four', '55': 'fifty-five', '56': 'fifty-six',
     '57': 'fifty-seven', '58': 'fifty-eight', '59': 'fifty-nine',
     '60': 'sixty', '61': 'sixty-one', '62': 'sixty-two', '63': 'sixty-three',
     '64': 'sixty-four', '65': 'sixty-five', '66': 'sixty-six',
     '67': 'sixty-seven', '68': 'sixty-eight', '69': 'sixty-nine',
     '70': 'seventy', '71': 'seventy-one', '72': 'seventy-two',
     '73': 'seventy-three', '74': 'seventy-four', '75': 'seventy-five',
     '76': 'seventy-six', '77': 'seventy-seven', '78': 'seventy-eight',
     '79': 'seventy-nine', '80': 'eighty', '81': 'eighty-one',
     '82': 'eighty-two', '83': 'eighty-three', '84': 'eighty-four',
     '85': 'eighty-five', '86': 'eighty-six', '87': 'eighty-seven',
     '88': 'eighty-eight', '89': 'eighty-nine', '90': 'ninety',
     '91': 'ninety-one', '92': 'ninety-two', '93': 'ninety-three',
     '94': 'ninety-four', '95': 'ninety-five', '96': 'ninety-six',
     '97': 'ninety-seven', '98': 'ninety-eight', '99': 'ninety-nine'}


def num2eng(number, mag=None):
    if isinstance(number, int):
        if number == 0:
            return 'zero'
        elif number > 999999999999:
            return str(number)
        else:
            number = '%012d' % number
            lst = [x for x in [num2eng(number[:-9], 'billion'),
                               num2eng(number[-9:-6], 'million'),
                               num2eng(number[-6:-3], 'thousand'),
                               num2eng(number[-3:])] if x]
            res = ' '.join(lst)
            if res.startswith('and '):
                res = res[4:]
            return res
    elif isinstance(number, str) and len(number) == 3:
        if number == '000':
            return None
        else:
            lst = []
            if not number.startswith('0'):
                lst.append(ENGLISH_NUMBER_NAMES[number[0]] + ' hundred')
            if not number.endswith('00'):
                lst.append('and ' + ENGLISH_NUMBER_NAMES[number[-2:]])
            if mag:
                lst.append(mag)
            res = ' '.join(lst)
            return res


if __name__ == '__main__':
    assert(num2eng(0) == 'zero')
    assert(num2eng(2) == 'two')
    assert(num2eng(10) == 'ten')
    assert(num2eng(25) == 'twenty-five')
    assert(num2eng(93) == 'ninety-three')
    assert(num2eng(406) == 'four hundred and six')
    assert(num2eng(7000) == 'seven thousand')
    assert(num2eng(8396) == 'eight thousand three hundred and ninety-six')
    assert(num2eng(10203) == 'ten thousand two hundred and three')
