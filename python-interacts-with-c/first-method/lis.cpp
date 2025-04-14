#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <algorithm>

std::vector<int> longest_increasing_subsequence(const std::vector<int>& nums) {
    if (nums.empty()) return {};
    std::vector<int> dp(nums.size(), 1);
    std::vector<int> prev(nums.size(), -1);
    int max_length = 1;
    int max_index = 0;

    for (size_t i = 1; i < nums.size(); ++i) {
        for (size_t j = 0; j < i; ++j) {
            if (nums[i] > nums[j] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
        if (dp[i] > max_length) {
            max_length = dp[i];
            max_index = i;
        }
    }

    std::vector<int> result;
    while (max_index != -1) {
        result.push_back(nums[max_index]);
        max_index = prev[max_index];
    }
    std::reverse(result.begin(), result.end());
    return result;
}

PYBIND11_MODULE(lis, m) {
    m.def("longest_increasing_subsequence", &longest_increasing_subsequence,
          "Find the longest increasing subsequence in an array");
}