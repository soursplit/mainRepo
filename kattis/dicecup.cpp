#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m, count, highest;
    count = 0;
    highest = 0;
    cin >> n >> m;
    vector<int> myNum;
    vector<int> myList;
    for (int i = 1; i <= n; i++) {
        for (int x = 1; x <= m; x++) {
            myNum.push_back(i+x);
        }
    }
    for (int i = 1; i <= n+m; i++) {
        for(int & x : myNum) {
            if (i == x) {
                count++;
            }
        }
        myList.push_back(count);
        count = 0;
    }
    for (int & i : myList) {
        if (highest < i) {
            highest = i;
        }
    }
    for (int i = 1; i <= n+m; i++) {
        if (highest == myList[i]) {
            cout << i +1 << endl;
        }
    }

    return 0;
}