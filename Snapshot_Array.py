class SnapshotArray:

    def __init__(self, length: int):
        
        self.arr=[[(0,0)] for _ in range(length)]
        
        self.cnt_snap=0

    def set(self, index: int, val: int) -> None:

        self.arr[index].append((self.cnt_snap,val))

        # return self.arr
        

    def snap(self) -> int:

        self.cnt_snap+=1

        return self.cnt_snap-1
        

    def get(self, index: int, snap_id: int) -> int:

        res=self.arr[index]

        l,r=0,len(res)-1

        while l<=r:

            mid=(l+r)//2

            if res[mid][0]<=snap_id:

                l=mid+1

            else:

                r=mid-1

        return res[r][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)