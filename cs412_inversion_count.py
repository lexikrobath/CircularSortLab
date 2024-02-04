def mergesort(A, count):
    if len(A) > 1:
        # Get the mid point
        m = len(A) // 2
        
        # Get the left and right halves
        left, right = A[:m], A[m:]

        # sort the left and right halves
        mergesort(left, count)
        mergesort(right, count)

        # Copy the sorted left and right halves back to A.
        for i in range(m):
            A[i] = left[i]
        for j in range(m, len(A)):
            A[j] = right[j - m]
        
        merge(A,m, count)


def merge(A, m, count):
    i, j = 0, m
    n = len(A)
    B = [0 for _ in range(n)]
    for k in range(n):
        if j >= n:
            B[k] = A[i]
            i += 1
        elif i >= m:
            B[k] = A[j]
            j += 1
        elif A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            count[0]+=1
            j += 1
    for k in range(n):
        A[k] = B[k]



def main():
    A = [int(x) for x in input().split()]
    count = [0]
    mergesort(A, count)
    print(count[0])

if __name__ == "__main__":
    main()
