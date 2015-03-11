'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        car_gas = 0
        station_ptr = 0
        for i in range(len(gas)):
            car_gas += gas[i]-cost[i]
            if car_gas<0:
                car_gas = 0
                station_ptr = i+1

        return station_ptr




def main():
    gas = [2,2,3,5]
    cost= [4,2,4,2]
    s = Solution()
    print s.canCompleteCircuit(gas,cost)


if __name__ == "__main__":
    main()

