#include <iostream>

using namespace std;
 class salaryprint
 {
 private:
    int salary;
 public:
    string empname;
    void setsalary(int s)
    {
        salary=s;
         cout << salary << endl;
    }

    int getsalaryprint()
{
    cout << "salary is" << salary << endl;
}

 };
int main()
{
    salaryprint sp;

    sp. setsalary(50);


    sp. getsalaryprint();
    return 0;
}
