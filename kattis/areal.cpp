#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    float area, perimeter;
    cin >> area;
    perimeter = 4*(sqrt(area));
    cout << fixed << setprecision( 8 ) << perimeter << endl;
    return 0;
}