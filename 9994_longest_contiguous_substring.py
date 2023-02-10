def lcss(tmp_str):
    result = 0
    tmp_len = len(tmp_str) - 1
    tmp = 0

    for i in range(len(tmp_str)):
        for j in range(len(tmp_str) - 1, i - 1, -1):
            # uncomment below to allow overlapping
            if (j <= i + tmp):
                break

            if (tmp_str[i + tmp] == tmp_str[j]):
                tmp += 1
            else:
                tmp = 0

            result = max(tmp, result)
        
        tmp = 0

    return result


print(lcss("redivide"))
print(lcss("dynamicpromanytimes"))