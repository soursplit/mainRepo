#include <iostream>
using namespace std;

int main() {
    int x;
    cin >> x;
    if (x <= 100) {
        cout << 99;
    } else {
        if (x % 100 <= 48) {
            x = x - ((x%100) + 1);
            cout << x;
        } else if (x % 100 >= 49) {
            x = x + (99 - (x%100));
            cout << x;
        }
    }

    return 0;
}