from token_type import Type
from token import Token

def string_end(code, index):
    """
    code = "abc"
    index = 1
    """
    lc = {
        'b': '\b',
        'f': '\f',
        'n': '\n',
        'r': '\r',
        't': '\t',
        '/': '/',
        '"': '"',
        '\\': '\\',
    }
    s = ''
    offset = index
    while offset < len(code):
        c = code[offset]
        if c == '"':
            # 找到了字符串的结尾
            # s = code[index:offset]
            return (s, offset)
        elif c == '\\':
            # 处理转义符, 现在只支持 \"
            b = code[offset+1]
            if b in lc:
                s += lc[b]
                offset += 2
        else:
            s += c
            offset += 1
    # 程序出错, 没有找到反引号 "
    pass

def guanjian_panduan(code, index, type):
    offset = index - 1
    lens = len(type)
    s = code[offset : offset + lens]
    if s == type:
        return s
    else:
        return -1
    pass

def json_tokens(code):
    length = len(code)
    tokens = []
    spaces = '\n\t\r'
    digits = '1234567890'
    # 当前下标
    i = 0
    while i < length:
        # 先看看当前应该处理啥
        c = code[i]
        i += 1
        if c in spaces:
            # 空白符号要跳过, space tab return
            continue
        elif c in ':,{}[]':
            # 处理 6 种单个符号
            t = Token(Type.auto, c)
            tokens.append(t)
        elif c == '"':
            # 处理字符串
            s, offset = string_end(code, i)
            i = offset + 1
            # print('i, offset', i, offset, s, code[offset])
            t = Token(Type.string, s)
            tokens.append(t)
        elif c in digits:
            # 处理数字, 现在不支持小数和负数
            end = 0
            for offset, char in enumerate(code[i:]):
                if char not in digits:
                    end = offset
                    break
            n = code[i-1:i+end]
            i += end
            t = Token(Type.number, n)
            tokens.append(t)
        elif c in 'tfn':
            m = {
             't': 'true',
             'f': 'false',
             'n': 'null'
            }
            t = Token(Type.keyword)
            t.value = m[c]
            tokens.append(t)
            i += len(m[c])
        else:
            # 出错了
            pass
    return tokens
