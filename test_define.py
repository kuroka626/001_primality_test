def judge(m):
    if m <= 0:
        return '判定不能'
    elif m < 3:
        return '素数です'
    else:
        for n in range(2,m):
            if m % n == 0:
                return '素数ではない'
        
    return '素数です'