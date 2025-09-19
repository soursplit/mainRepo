#include <iostream>
using namespace std;

int main() {
    int n;
    string m;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> m;
        if (i % 2 == 0) {
            cout << m << endl;
        }
    }
}