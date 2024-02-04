def circular_find_helper(needle, haystack, start, end):
    def between(x, y, z):
        return (x <= y and y<=z) or (z <= y and y <= x)
    
    if start > end: 
        return -1
    
    if start == end:
        if haystack[start] == needle:
            return start
        else:
            return -1

    mid = (start+end)//2

    if haystack[mid] == needle:
        return mid
    if (haystack[start] < haystack[mid-1]) and between(haystack[start], needle, haystack[mid-1]) or (haystack[start] > haystack[mid-1] and not between(haystack[start], needle, haystack[mid-1])):
            return circular_find_helper(needle, haystack, start, mid)
    else:
        return circular_find_helper(needle, haystack, mid+1, end)


def circular_find(needle, haystack):
    return circular_find_helper(needle, haystack, 0, len(haystack)-1)


def main():
    haystack = [int(x) for x in input().split()]
    needle = int(input())
    print(circular_find(needle, haystack))

if __name__=="__main__":
    main()
