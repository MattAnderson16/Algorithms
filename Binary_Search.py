import pdb

def BinarySearch(List, First, Last, ItemSought):
    ItemFound = False
    SearchFailed = False
    while not ItemFound or not SearchFailed:
        pdb.set_trace()
        Midpoint = (First + Last)//2
        if List[Midpoint] == ItemSought:
            ItemFound = True
        else:
            if First >= Last:
                SearchFailed = True
            else:
                if List[Midpoint] > ItemSought:
                    Last = Midpoint - 1
                else:
                    First = Midpoint + 1
    if ItemFound:
        return True
    else:
        return False

if __name__ == "__main__":
    List = [1,2,3,4,5,6,7,8]
    Found = BinarySearch(List,0, len(List)-1,7)
    if Found:
        print("Item found in the list")
    else:
        print("Item not in list")
