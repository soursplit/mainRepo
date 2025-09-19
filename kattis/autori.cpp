#include <iostream>
using namespace std;

int main() {
    string n;
    cin >> n;
    cout << n[0];
    for (int i; i < n.length(); i++) {
        if (n[i] == '-') {
            cout << n[i+1];
        }
    }
}