#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float atBats, total, in, done, count;
    count = 0;
    cin >> atBats;
    for (int i = 0; i < atBats; i++) {
        cin >> in;
        if (in != -1.0) {
            total = total + in;
        } else {
            count++;
        }
    }
    done = total/(atBats-count);
    cout << setprecision(16) << done;
    return 0;
}