#include <iostream>

using namespace std;
<<<<<<< HEAD
class parentbird
{
private:
    string color;
int weight;
=======
class birds
{
private:
    string color;
string weight;
>>>>>>> 4cb537b92fd82aa2d40d9311cf1db3ed3552318a
public:
    void eat()
    {
        cout << "i can eat" << endl;

    }
     string birdname()
    {

        string name = "rose";
        return name;

    }
    /*string mycolor()
    {
        string color = "red";
        return color;
    }*/



    void setcolor()
    {
<<<<<<< HEAD
        cout << "setcolor is:" ;
=======
        cout << "setcolor is:" << endl;
>>>>>>> 4cb537b92fd82aa2d40d9311cf1db3ed3552318a
        cin >> color;
    }
    string getcolor()
    {
      return color;
    }
    void setweight()
    {
<<<<<<< HEAD
        cout << "setweight is :" << endl;
=======
        cout << "setweight is" << endl;
>>>>>>> 4cb537b92fd82aa2d40d9311cf1db3ed3552318a
        cin >> weight;
    }
    int getweight()
    {
        return weight;
    }
};
<<<<<<< HEAD
    class childbird : public parentbird{

        public:

        void birdsound()
        {
            cout << "i can sing" << endl;
        }

    };
class grandchildbird : public childbird{

};
class parrot : public parentbird{
  public:

        void birdsound()
        {
            cout << "i can mow" << endl;
        }

};
int main()
{

    /*cout << "parentbird output:" << endl;
   parentbird pb;
    pb.setcolor();
    pb.myweight();
    pb.eat();

    cout << "color is:" << pb.getcolor() << endl;
    cout << pb.birdname() << endl;
    //cout << bs.mycolor() << endl;
    cout << pb.myweight() << endl;



   /* if(bs.myweight()==25)
    {
    cout << "return type is equal to 25" << endl;
    }*/

    cout << "this output is childbird class" << endl;

childbird cb;

cb.setcolor();
cb.getweight();
cb.eat();
cb.birdsound();
    cout << "color is:" << cb.getcolor() << endl;
    cout << "weight is:" << cb.getweight() << endl;
    return 0;

cout << "this output is grandchilbird class" << endl;



grandchildbird gb;

gb.setcolor();
gb.getweight();
gb.eat();
gb.birdsound();
    cout << "color is:" << gb.getcolor() << endl;
    cout << "weight is:" << gb.getweight() << endl;
    return 0;



parrot p;

p.setcolor();
p.getweight();
p.eat();
p.birdsound();
    cout << "color is:" << p.getcolor() << endl;
    cout << "weight is:" << p.getweight() << endl;
=======
    class dog : public birds{
    };

int main()
{
   /* birds bs;
    bs.eat();
    cout << bs.birdname() << endl;
    //cout << bs.mycolor() << endl;
    cout << bs.myweight() << endl;
    bs.myweight1();
    bs.setcolor();
    cout << "color is:" << bs.getcolor() << endl;

    if(bs.myweight()==25)
    {
    cout << "return type is equal to 25" << endl;
    }*/
dog dg;
dg.eat;
dg.setcolor();
    cout << "color is:" << dg.getcolor() << endl;
dg.getweight();
    cout << "weight is:" << dg.getweight() << endl;
>>>>>>> 4cb537b92fd82aa2d40d9311cf1db3ed3552318a
    return 0;
}
