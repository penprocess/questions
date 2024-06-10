def frequency(lst, k):
    freq = []
    for i in lst:
        if i not in freq:
          count_i = lst.count(i)
          if count_i >= k:
            freq.append(i)

    return freq
    
print(frequency([1,1,4,1,4,3,0, 2], 2))