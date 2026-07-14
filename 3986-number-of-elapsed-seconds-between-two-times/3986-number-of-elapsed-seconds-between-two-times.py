class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start = [int(x) for x in startTime.split(":")]
        end = [int(x) for x in endTime.split(":")]

        s = start[0]*3600 + start[1] * 60 + start[2]
        e = end[0]*3600 + end[1] * 60 + end[2]

        return e - s



            
