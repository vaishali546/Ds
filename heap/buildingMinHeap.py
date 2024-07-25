def heapify(arr,n,i):
    smallest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[l] < arr[smallest]:
        smallest = l
    if r<n and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapify(arr,n,smallest)

def buildMinHeap(arr,n):
    startIndex = n//2 - 1
    for i in range(startIndex,-1,-1):
        heapify(arr,n,i)

if __name__ == "__main__":
    arr = [75,25,35,45,90,80,60,20,30]
    n = len(arr)
    print("Initial array: ",*arr,sep=" ")
    buildMinHeap(arr,n)
    print("Build MinHeap: ",*arr,sep=" ")
    