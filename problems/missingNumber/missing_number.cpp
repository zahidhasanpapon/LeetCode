#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int missingNumber(vector<int> &nums) {
    if (nums.empty())
      return 0;
    int length = nums.size();
    for (int i = 0; i < length;) {
      if (nums[i] < length and nums[i] != i) {
        swap(nums[i], nums[nums[i]]);
      } else {
        ++i;
      }
      for (int i = 0; i < length; ++i) {
        if (nums[i] != i) {
          return i;
        }
      }
      return length;
    }
  }
};