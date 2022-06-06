We are given an array named nums containing n distinct numbers in the range [0, 9]. So there are no duplicates and the value of each distinct number starts from 0 till the lenght size of the array. 

Intuition 1:

We can just think and realize if the array is sorted then each index should contain value similar to index number. And there should be one index where containing value doesn't match with index number and it is must beacuse the range is from 0 till n, so the array will contain n-1 elements. We can just loop over the sorted array and see if any value doesn't match. If there exists one index where index number doesn't match with the value then stop the iteration and return the index number as the only number in the range that is missing from the array. If the loop exists without finding any missing number then the length of the array must be the missing number. 

Time complexity:

Sorting - O(nlog(n))
Searching - O(n)
Overall - O(nlog(n))

Space complexity: O(1)
