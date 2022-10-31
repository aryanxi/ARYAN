/*#include<iostream>
#include<math.h>
using namespace std;

int main()
{
     
     int x=10;
     int y= x++;˜
     cout<<x;




}*/
#include<iostream>   //code for radius of circle and area of triangle  
#include<math.h>
using namespace std;

int main()
{
 cout<<"ENTER THE RADIUS OF ";
 int r;
 cin>>r;
 cout<<"Enter the value of length of triangle "<<endl;
int l;
 cin>>l;

 
 float x=(3.14 *(r*r) );
 float y=(0.5*r*l);
 cout<<x<<" is the area of circle\n";
 cout<<y<<" is the area of trianle\n";
 maths();

 return 0;

}


void maths(){

for(int i = 0; i < 5; i++)
{
     int x;
     x=i+4;
     cout<<x;
    
}
}

