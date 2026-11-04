#include <bits/stdc++.h>
using namespace std;

class Phone
{
public:
    Phone()
    {
        cout << "this is constractor";
    }
    ~Phone()
    {
        cout << "this is dractractor";
    }
    void display()
    {
        cout<<"display";
    }
};

int main()
{

    Phone p;
    
    return 0;
}