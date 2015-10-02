# http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/
class Solution:
    def selectActivity(self, activities):
        activities.sort(key=lambda x: x[1])
        result = []
        result.append(activities[0])
        prev_selected = activities[0]
        for i in range(1, len(activities)):
            if prev_selected[1] <= activities[i][0]:
                result.append(activities[i])
                prev_selected = activities[i]
        return result

if __name__ == "__main__":
    # [(start_time, end_time), ...]
    activities = [(1,2), (3,4), (8,9), (0,6), (5,7), (5,9)]
    # output: activities selected
    sol = Solution()
    print sol.selectActivity(activities)
    # output: right answer
    print [(1,2), (3,4), (5,7), (8,9)]
