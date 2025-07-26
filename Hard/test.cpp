#define ll long long
class Solution {
public:
    long long maxSubarrays(int n, vector<vector<int>>& conflictingPairs) {
        vector<vector<int>> lefts(n + 1);
        for (auto& pair : conflictingPairs) {
            int a = min(pair[0], pair[1]), b = max(pair[0], pair[1]);
            lefts[b].push_back(a);
        }

        ll ans = 0, top1 = 0, top2 = 0;
        vector<ll> bonus(n + 1);

        for (int b = 1; b <= n; ++b) {
            for (auto a : lefts[b]) {
                if (a > top1) {
                    top2 = top1;
                    top1 = a;
                } else if (a > top2) {
                    top2 = a;
                }
            }
            ans += (b - top1);
            if (top1 > 0) {
                bonus[top1] += (top1 - top2);
            }
        }

        ll mx = 0;
        for (auto x : bonus) mx = max(mx, x);
        return ans + mx;
    }
};
