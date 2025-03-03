class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_num = len(nums)
        import heapq
        heap = []
        for idx, n in enumerate(nums):
            heap.append([n, idx])
        heap.sort(key=lambda x: x[0])
        for i in range(len_num):
            q = heap[i][0]
            remain_target = target - q
            start = i+1
            end = len_num - 1
            while start <= end:
                mid = (end + start) // 2
                q_2 = heap[mid][0]
                if (remain_target - q_2) == 0:
                    return [heap[i][1], heap[mid][1]]
                if (remain_target - q_2) > 0:
                    start = mid + 1
                    end = end
                else:
                    start = start
                    end = mid - 1