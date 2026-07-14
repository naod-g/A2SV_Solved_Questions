class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        # start = [int(x) for x in startTime.split(":")]
        # end = [int(x) for x in endTime.split(":")]


        # s = start[0]*3600 + start[1] * 60 + start[2]
        # e = end[0]*3600 + end[1] * 60 + end[2]

        # return e - s

        return (int(endTime[0:2]) * 3600 - int(startTime[0:2]) * 3600) +  (int(endTime[3:5]) * 60 - int(startTime[3:5]) * 60) + (int(endTime[6:]) - int(startTime[6:]))

            
