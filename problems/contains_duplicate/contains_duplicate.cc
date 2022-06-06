// O(n^2) TLE
class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {
    int len = nums.size();
    for (int i = 0; i < len; i++) {
      for (int j = i + 1; j < len; j++) {
        if (nums[i] == nums[j]) {
          return true;
        }
      }
    }
    return false;
  }
};

// O(nlogn)
class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {
    int len = nums.size();
    if (len < 2) {
      return false;
    }
    sort(nums.begin(), nums.end());
    for (int i = 0; i < len - 1; i++) {
      if (nums[i] == nums[i + 1]) {
        return true;
      }
    }
    return false;
  }
};

// O(n)
class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {
    unordered_map<int, bool> exist;
    for (int i = 0; i < nums.size(); ++i) {
      if (exist[nums[i]]) {
        return true;
      } else {
        exist[nums[i]] = true;
      }
    }
    return false;
  }
};