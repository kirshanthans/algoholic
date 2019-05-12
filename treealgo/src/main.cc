#include <iostream>
#include <cstdlib>
#include <ctime>
#include <random>

#define min(x, y) ((x)<(y)?(x):(y))
#define max(x, y) ((x)>(y)?(x):(y))

using namespace std;

class Node
{
    public:
        int data;
        Node * l; 
        Node * r;
        Node(){
            data = 0;
            l = NULL;
            r = NULL;
        };
        ~Node(){};
};

// build a random tree
Node * buildTree(int s, int e);
// delete a tree
void deleteTree(Node * n);
// count the nodes
int countNodes(Node * n);
// find the minimum vertex cover of a tree
int vertexCover(Node * n);
void vCover(Node * n);

Node * buildTree(int s, int e)
{
    if (s == e || s+1 == e) return NULL;
    // find a pivot
    int p = (e+s)/2;
    // construct the node
    Node * n = new Node();
    n->data = 0;
    n->l = buildTree(s, p);
    n->r = buildTree(p, e);
    // return node
    return n;
}

void deleteTree(Node * n)
{
    if (n == NULL) return;
    // delete subtrees
    deleteTree(n->l);
    deleteTree(n->r);
    // delete current node
    delete n;
}

int countNodes(Node * n)
{
    if (n == NULL) return 0;
    int lx = countNodes(n->l);
    int rx = countNodes(n->r);
    return 1+lx+rx;
}

int vertexCover(Node * n)
{
    if (n == NULL) 
        return 0;
    // include the current node
    int inc = 1 + vertexCover(n->l) + vertexCover(n->r);
    // excluding the current node
    int exc = 0;
    if (n->l != NULL){
        exc += 1;
        exc += vertexCover(n->l->l);
        exc += vertexCover(n->l->r);
    }
    if (n->r != NULL){
        exc += 1;
        exc += vertexCover(n->r->l);
        exc += vertexCover(n->r->r);
    }
    return min(inc, exc);
}

void vCover(Node * n)
{
    if (n == NULL) 
        return;
    vCover(n->l);
    vCover(n->r);

    // include the current node
    int inc = 1;
    // excluding the current node
    int exc = 0;
    if (n->l != NULL){
        inc += n->l->data;
        exc += 1;
        exc += (n->l->l != NULL) ? n->l->l->data : 0;
        exc += (n->l->r != NULL) ? n->l->r->data : 0;
    }
    if (n->r != NULL){
        inc += n->r->data;
        exc += 1;
        exc += (n->r->l != NULL) ? n->r->l->data : 0;
        exc += (n->r->r != NULL) ? n->r->r->data : 0;
    }
    n->data = min(inc, exc);
}

int main(int argc, char ** argv)
{
    srand(time(NULL));
    Node * root = buildTree(0, 9);
    int nc = countNodes(root);
    cout << "Node count: " << nc << endl;
    int vc1 = vertexCover(root);
    vCover(root);
    int vc2 = root->data;
    cout << "Vertex cover size1: " << vc1 << endl;
    cout << "Vertex cover size2: " << vc2 << endl;
    deleteTree(root);
    return 0;
}