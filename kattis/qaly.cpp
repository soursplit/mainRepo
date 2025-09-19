#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int num;
    float x, y, total;
    cin >> num;
    for (int i = 0; i < num; i++) {
        cin >> x >> y;
        total = total + (x*y);
    }
    cout << total;
    return 0;
}