"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

1. Clarified the problem.
2. Made examples.
3. Outlined algorithm
4. Ran few examples on the algorithm.
5. Wrote code.
6. Ran few examples again.
7. DID NOT DISCUSS TIME COMPLEXITY.  T = O(nlogn) S = O(1)

How would you sort a array of objects.
arr.sort(key=lambda x: x.start)

"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def do_overlap_merge_if_true(self, interval1, interval2):
        """
        """
        if interval1.end >= interval2.start:
            return True, Interval(min(interval1.start, interval2.start),
                                  max(interval1.end, interval2.end))
        return False, None

    def merge_intervals(self, intervals):
        result = []
        if not intervals:
            return result
        index = 0
        while index < len(intervals):
            cur_interval = intervals[index]
            while index + 1 < len(intervals):
                overlap, new_interval = self.do_overlap_merge_if_true(cur_interval, intervals[index + 1])
                if not overlap:
                    break
                cur_interval = new_interval
                index += 1
            result.append(cur_interval)
            index += 1
        return result

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        return self.merge_intervals(intervals)
