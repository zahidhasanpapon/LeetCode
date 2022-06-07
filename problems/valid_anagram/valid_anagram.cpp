// Since the problem statement says that "the string contains only lowercase
// alphabets", we can simply use an array to simulate the unordered_map and
// speed up the code.
// Implementing Hashmap as an Array of constant size
class Solution {
public:
  bool isAnagram(string s, string t) {
    int len_s = s.length();
    int len_t = t.length();
    if (s == t) {
      return true;
    }
    if (len_s != len_t) {
      return false;
    }
    int unordered_map[26] = {0};
    for (int i = 0; i < len_s; i++) {
      unordered_map[s[i] - 'a']++;
      unordered_map[t[i] - 'a']--;
    }
    for (int i = 0; i < 26; i++) {
      if (unordered_map[i]) {
        return false;
      }
    }

    return true;
  }
};

// O(n)
class Solution {
public:
  bool isAnagram(string s, string t) {
    if (s == t) {
      return true;
    }
    if (s.length() != t.length()) {
      return false;
    }
    unordered_map<char, int> alphabet;
    for (int i = 0; i < s.length(); i++) {
      alphabet[s[i]]++;
      alphabet[t[i]]--;
    }
    for (int i = 0; i < s.length(); i++) {
      if (alphabet[s[i]] != 0 || alphabet[t[i]] != 0) {
        return false;
      }
    }
    return true;
  }
};

// O(nlogn)
class Solution {
public:
  bool isAnagram(string s, string t) {
    if (s == t) {
      return true;
    }
    if (s.length() != t.length()) {
      return false;
    }
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    return s == t;
  }
};