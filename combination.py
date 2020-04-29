import itertools
# リストの組み合わせの合計と任意の数字が同地である場合、その組み合わせを返す
def find_combination(num, lis):
    ans = []
    for n in range(1,len(lis)+1):
        for conb in itertools.combinations(lis, n):
            if(sum(conb) == num):
                ans.append(list(conb))
    return ans