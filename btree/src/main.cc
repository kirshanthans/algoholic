#include <iostream>
#include <cstdlib>

using namespace std;

class Node{
    public: 
        int * data;
        Node ** children;
        Node(){};
        ~Node(){};
        void traverse();
};

class BTree{
    public:
        static Node * createTree(int s, int e);
        static void destroyTree(Node * n);
        Node * root;
        BTree(int _s, int _e){ root = createTree(_s, _e); };
        ~BTree(){ destroyTree(root); };
        void traverse() {root->traverse();}
};

void Node::traverse()
{
    return;
}

Node * BTree::createTree(int s, int e)
{
    return NULL;
}

void BTree::destroyTree(Node *n)
{
    return;
}

int main(int argc, char ** argv)
{
    BTree tree(0, 10);
    tree.traverse();
    return 0;
}