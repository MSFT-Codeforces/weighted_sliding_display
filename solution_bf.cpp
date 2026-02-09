#include <algorithm>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>

using namespace std;

/*
    Brute-force baseline (intentionally non-optimal):

    For each starting position s in the sorted array v, enumerate all valid ways
    to expand the taken interval by choosing left/right adjacent elements.
    This is exponential in n (roughly 2^(n-1)) and is only suitable for small n.

    Correctness notes:
    - The chosen positions in v always form a contiguous interval [L, R].
    - For each step i, we compute the range (max_i - min_i) among chosen values
      and add w_i * range to the score.
*/

struct State {
    int l;
    int r;
    int step;              // how many elements have been taken so far (1..n)
    long long currentMin;  // min among chosen p_1..p_step
    long long currentMax;  // max among chosen p_1..p_step
    long long score;       // accumulated score so far
};

static long long bruteFromStart(const vector<long long>& v, const vector<long long>& w, int s) {
    int n = (int)v.size();
    if (n == 1) {
        return 0LL;
    }

    long long best = numeric_limits<long long>::min();

    vector<State> st;
    // For step = 1, range is 0, so the contribution w_1 * 0 is always 0.
    st.push_back(State{s, s, 1, v[s], v[s], 0LL});

    while (!st.empty()) {
        State cur = st.back();
        st.pop_back();

        if (cur.step == n) {
            best = max(best, cur.score);
            continue;
        }

        int nextStep = cur.step + 1;

        // Try taking from the left.
        if (cur.l > 0) {
            long long newVal = v[cur.l - 1];
            long long newMin = min(cur.currentMin, newVal);
            long long newMax = max(cur.currentMax, newVal);
            long long range = newMax - newMin;
            long long newScore = cur.score + w[nextStep] * range;
            st.push_back(State{cur.l - 1, cur.r, nextStep, newMin, newMax, newScore});
        }

        // Try taking from the right.
        if (cur.r + 1 < n) {
            long long newVal = v[cur.r + 1];
            long long newMin = min(cur.currentMin, newVal);
            long long newMax = max(cur.currentMax, newVal);
            long long range = newMax - newMin;
            long long newScore = cur.score + w[nextStep] * range;
            st.push_back(State{cur.l, cur.r + 1, nextStep, newMin, newMax, newScore});
        }
    }

    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<long long> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        // w is 1-indexed for convenience.
        vector<long long> w(n + 1, 0LL);
        for (int i = 1; i <= n; i++) {
            cin >> w[i];
        }

        vector<pair<long long, int>> paired(n);
        for (int i = 0; i < n; i++) {
            paired[i] = {a[i], i + 1}; // store original 1-based index for tie-break
        }

        sort(paired.begin(), paired.end(),
             [](const pair<long long, int>& x, const pair<long long, int>& y) {
                 if (x.first != y.first) return x.first < y.first;
                 return x.second < y.second;
             });

        vector<long long> v(n);
        for (int i = 0; i < n; i++) {
            v[i] = paired[i].first;
        }

        long long answer = (n == 1) ? 0LL : numeric_limits<long long>::min();
        if (n > 1) {
            for (int s = 0; s < n; s++) {
                answer = max(answer, bruteFromStart(v, w, s));
            }
        }

        cout << answer << "\n";
    }

    return 0;
}