HUI = u'ХУЙ'


def hui(width=30, char='*', space=' '):
    chars_count = len(HUI)
    height = width / chars_count
    i_dot_height = height / 5
    i_dot_pos = int(chars_count - 1 + width * (2 / float(chars_count) + 1 / float(chars_count) / 2.0))

    result = ''

    for i in range(-i_dot_height, height):
        s = ''
        for j in range(0, width + 2 + 1):
            if i < 0:
                if j == i_dot_pos:
                    s += char
                else:
                    s += space
                continue
            if j < width / chars_count:
                if i == j or (i + j == width / chars_count -1):
                    s += char
                    continue
                
            if width / chars_count + 1 <= j < width / chars_count * 2  + 1:
                if i + width / chars_count + 1 == j and i < (width / chars_count + 1) / 2  or (i + j == width / chars_count * 2):
                    s += char
                    continue
            
            if j >= 2 * width / chars_count + 1:
                if j == 2 * (width / chars_count + 1) or j == width + 2  or (i + j == width + 1):
                    s = += char
                    continue
      
            s += space
            
        result += s + '\n'

    return result
