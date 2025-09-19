#include <iostream>
using namespace std;

int main() {
    int length, num;
    cin >> length;
    int ls[length];
    
    for (int i = 0; i < length; i++) {
        cin >> num;
        ls[i] = num;
    }
    for (int i = length-1; i > -1; i--) {
        cout << ls[i] << endl;
    }
    return 0;
}