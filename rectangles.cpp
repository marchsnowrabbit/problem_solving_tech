#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

#define MAX_LEAF 20000
#define OFFSET 10000

class Info {
public:
    int x, y1, y2;
    bool left;
    Info() {}
    Info(int x, int y1, int y2, bool left) {
        this->x = x;
        this->y1 = y1;
        this->y2 = y2;
        this->left = left;
    }
    bool operator < (const Info &b) const {
        return this->x < b.x;
    }
};

int tree[MAX_LEAF * 4];
int cnt[MAX_LEAF * 4];

void update_tree(int now, int left, int right, int start, int end, int value) {
    if (left > end || right < start) {
        return;
    }

    if (left <= start && end <= right) {
        cnt[now] += value;
    } else {
        int mid = (start + end) / 2;
        update_tree(now * 2, left, right, start, mid, value);
        update_tree(now * 2 + 1, left, right, mid + 1, end, value);
    }

    if (!cnt[now]) {
        if (start != end) {
            tree[now] = tree[now * 2] + tree[now * 2 + 1];
        } else {
            tree[now] = 0;
        }
    } else {
        tree[now] = end - start + 1;
    }
}

int main() {
    ifstream input("rectangles.inp");
    ofstream output("rectangles.out");

    int N;
    input >> N;

    vector<Info> vec;

    for (int i = 0; i < N; i++) {
        int x1, y1, x2, y2;
        input >> x1 >> y1 >> x2 >> y2;

        vec.push_back(Info(x1, y1, y2, true));
        vec.push_back(Info(x2, y1, y2, false));
    }

    sort(vec.begin(), vec.end());

    int ans = 0;
    for (int i = 0; i < vec.size(); i++) {
        if (i) {
            ans += (vec[i].x - vec[i - 1].x) * tree[1];
        }

        int value = (vec[i].left == true) ? 1 : -1;
        update_tree(1, vec[i].y1 + OFFSET, vec[i].y2 - 1 + OFFSET, 0, MAX_LEAF - 1, value);
    }

    output << ans << "\n";

    return 0;
}

