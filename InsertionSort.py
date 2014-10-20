def InsertionSort(List):
    for CurrentPtr in range(1, len(List)):
        CurrentValue = List[CurrentPtr]
        Ptr = CurrentPtr - 1
        while (List[Ptr] > CurrentValue) and (Ptr >= 0):
            List[Ptr+1] = List[Ptr]
            Ptr -=1
        List[Ptr+1] = CurrentValue


if __name__ == "__main__":
    List = ["z","f","c","b","d"]
    InsertionSort(List)
    print(List)
