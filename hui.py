def hui(width=30, char='*', space=' '):
    height = width / 3
    i_dot_height = height / 5
    i_dot_pos = int(3 + width * (2 / 3.0 + 1 / 3.0 / 2.0))

    result = ''

    for i in range(-i_dot_height, height):
        s = ''
        for j in range(0, width + 2 + 1):
            if i < 0:
                if j == i_dot_pos:
                    s = s + char
                else:
                    s = s + space
                continue
            if j < width / 3:
                if i == j or (i + j == width / 3 -1):
                    s = s + char
                    continue
                
            if width / 3 + 1 <= j < width / 3 * 2  + 1:
                if i + width / 3 + 1 == j and i < (width / 3 + 1) / 2  or (i + j == width / 3 * 2):
                    s = s + char
                    continue
            
            if j >= 2 * width / 3 + 1:
                if j == 2 * (width / 3 + 1) or j == width + 2  or (i + j == width + 1):
                    s = s + char
                    continue
      
            s = s + space
            
        result += s + '\n'

    return result
