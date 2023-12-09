#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

double area(int x1, int y1, int x2, int y2, int x3, int y3) {
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0);
}

double find_area_order(const pair<int, int>& nail1, const pair<int, int>& nail2, const pair<int, int>& nail3) {
    return area(nail1.first, nail1.second, nail2.first, nail2.second, nail3.first, nail3.second);
}

void win_game(vector<pair<int, int>>& nails, int m) {
    sort(nails.begin(), nails.end(), [](const auto& a, const auto& b) {
        return (a.second < b.second) || (a.second == b.second && a.first < b.first);
    });

    for (int i = 0; i < m; ++i) {
        double min_area = numeric_limits<double>::infinity();
        pair<int, int> removed_nail;

        for (size_t j = 0; j < nails.size() - 1; ++j) {
            for (size_t k = j + 1; k < nails.size(); ++k) {
                double current_area = find_area_order(nails[j], nails[k], nails[0]);

                if (current_area < min_area) {
                    min_area = current_area;
                    removed_nail = nails[j];
                }
            }
        }

        cout << removed_nail.first << " " << removed_nail.second << endl;
        nails.erase(remove(nails.begin(), nails.end(), removed_nail), nails.end());
    }

    cout << (nails.size() % 2 == 0 ? "YES" : "NO") << endl;
}

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> nails(n);
    for (int i = 0; i < n; ++i) {
        cin >> nails[i].first >> nails[i].second;
    }

    int m;
    cin >> m;

    win_game(nails, m);

    return 0;
}
