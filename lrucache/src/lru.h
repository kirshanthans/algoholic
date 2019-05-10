#ifndef LRUH
#define LRUH

#include <list>
#include <unordered_map>
#include <iostream>

using namespace std;

class lrucache{

    public: 
        lrucache(int c) : capacity(c) {}
        void refer(int x);
        void display();
    
    int capacity;
    list<int> q;
    unordered_map<int, list<int>::iterator> m;
};

void lrucache::refer(int x)
{
    if (m.find(x) == m.end())
    {
        if (q.size() == capacity)
        {
            int last = q.back();
            q.pop_back();
            m.erase(last);
        }
    }
    else {
        m.erase(x);
    }
    q.push_front(x);
    m[x] = q.begin();

}

void lrucache::display()
{
    cout << "Cache Content" << endl;
    for(list<int>::iterator it = q.begin(); it != q.end(); ++it) cout << *it << endl;
}

#endif