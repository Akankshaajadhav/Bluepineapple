#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* CreateNode(int value){
    struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
    temp->data=value;
    temp->left=NULL;
    temp->right=NULL;
return temp;
}

struct Node* InsertNode(struct Node* node,int value){
    if(node==NULL)
        return CreateNode(value);
    
    if(value<node->data)
        node->left=InsertNode(node->left,value);
    
    if(value>node->data)
        node->right=InsertNode(node->right,value);
return node;
}


struct Node* InOrder(struct Node* node){
    if(node==NULL)
        return 0;

    InOrder(node->left);
    printf("%d  ",node->data);
    InOrder(node->right);
}

struct Node* PreOrder(struct Node* node){
    if(node==NULL)
        return 0;

    printf("%d  ",node->data);
    PreOrder(node->left);
    PreOrder(node->right);
}

struct Node* PostOrder(struct Node* node){
    if(node==NULL)
        return 0;

    PostOrder(node->left);
    PostOrder(node->right);
    printf("%d  ",node->data);
}

void main(){
    int n,value;
    printf("ENter no of nodes : ");
    scanf("%d",&n);

    struct Node* root=NULL;
    printf("Enter values : ");
    for (int i=0;i<n;i++){
        scanf("%d",&value);
        root=InsertNode(root,value);
    }
    
    printf("Inoder traversal of tree is : ");
    InOrder(root);

    printf("\nPreoder traversal of tree is : ");
    PreOrder(root);

    printf("\nPostoder traversal of tree is : ");
    PostOrder(root);
}


