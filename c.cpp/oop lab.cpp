//OOP_Lab_Assignment_02
#include <iostream>
#include <string.h>
using namespace std;
class student
{
    string name, clas, dob, bld_grp, addr;
    int *rollno, div, mob;

public:
    friend class teacher;
    student()
    {
        rollno = new int;
        name, clas, dob, bld_grp, addr = "";
        *rollno, div, mob = 0;
    }
    student(student&obj)
    {
        this->name = obj.name;
        this->addr = obj.addr;
        this->clas = obj.clas;
        this->dob = obj.dob;
        this->bld_grp = obj.bld_grp;
        this->rollno = obj.rollno;
        this->div = obj.div;
        this->mob = obj.mob;
    }
    ~student()
    {
        delete rollno;
    }

    inline static void display_header()
    {
        cout << "-----------Student information system-----------\n";
        cout << "name\nroll no\nclass\ndivision\nmobile number\ndob\naddress\nblood group\n";
    }
    void getdata()
    {
        cout << "Enter roll no:\n";
        cin >> *rollno;
        cout << "Enter name:\n";
        cin.ignore();
        getline(cin, name);
        cout << "Enter class:\n";
        cin >> clas;
        cout << "Enter division:\n";
        cin >> div;
        cout << "Enter DOB:\n";
        cin >> dob;
        cout << "Enter mobile no:\n";
        cin >> mob;
        cout << "Enter address:\n";
        cin >> addr;
        cout << "Enter blood group:\n";
        cin >> bld_grp;
    }
    void display()
    {
        cout << name << "\n"
             << *rollno << "\n"
             << clas << "\n"
             << div << "\n"
             << dob << "\n"
             << mob << "\n"
             << addr << "\n"
             << bld_grp << "\n";
    }
};
class teacher
{
    int id;

public:
    teacher()
    {
        id = 0;
    }
    void display_t(student &obj1, int t_d)
    {
        try
        {
            if (obj1.div == t_d)
            {
                obj1.display();
            }
            else
            {
                throw(obj1.div);
            }
        }
        catch (int x)
        {
            cout << "Student & teacher division can not be matched";
        }
    }
};

int main()
{
    student s[10];
    teacher t;
    int ch, count = 0;
    do
    {
        cout << "-----------Student information system----------\n";
        cout << "------------------Menu-----------------------\n";
        cout << "1. Add Student Record\n";
        cout << "2. Display Student Record\n";
        cout << "3. Copy instructor\n";
        cout << "4. Division wise information\n";
        cout << "5. Exit\n";
        cout << "Enter a Choice:\n";
        cin >> ch;
        switch (ch)
        {
        case 1:
        {
            s[count].getdata();
            count++;
        }
        break;
        case 2:
        {
            student::display_header();
            for (int i = 0; i < count; i++)
            {
                s[i].display();
            }
        }
        break;
        case 3:
        {
            cout << "Copy Constructor\n";
            student s1;
            s1.getdata();
            student s2(s1);
            s2.display();
        }
        break;
        case 4:
        {
            int t_div;
            cout << "Enter Division:\n";
            cin >> t_div;
            for (int i = 0; i < count; i++)
            {
                t.display_t(s[i], t_div);
            }
            break;
        }
        case 5:
        {
            exit(0);
        }
        }
    } while (ch != 5);
    return 0;
}