// 백준 2438번 문제
#include <iostream>
using namespace std;


int main() {
    int a;
    cin >> a;
    for(int i = 0; i<a; i++){
        for(int j = -1 ; j<i; j++)
            cout << "*";

        cout << endl;
    }
    return 0;
}
