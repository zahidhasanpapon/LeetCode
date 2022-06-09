// O(n)
// O(n)
class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    vector<int> answer;
    unordered_map<int, int> hash_map;
    for (int i = 0, n = nums.size(); i < n; ++i) {
      int number_to_find = target - nums[i];
      if (hash_map.find(number_to_find) != hash_map.end()) {
        answer.push_back(i);
        answer.push_back(hash_map[number_to_find]);
        return answer;
      }
      hash_map[nums[i]] = i;
    }
    return answer;
  }
};

// o(n^2)
class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    vector<int> answer;
    for (int i = 0; i < nums.size() - 1; i++) {
      for (int j = i + 1; j < nums.size(); j++) {
        if ((nums[i] + nums[j]) == target) {
          answer.push_back(i);
          answer.push_back(j);
          return answer;
        }
      }
    }
    return answer;
  }
};