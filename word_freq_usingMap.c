#include<stdio.h>
#include<string.h>
// #define size 10
int keys[10];
int value[10];
int currentSize=0;

int showIndex(int word){
    for(int i=0;i<currentSize;i++){
        if(keys[i]==word){
            return i;
        }
    }
    return -1;
}

void Insert(int word,int data){
    int index=showIndex(word);
    if(index==-1){
        keys[currentSize]=word;
        value[currentSize]=data;
        currentSize++;
    }
    else
        value[index]=data;
}

int showValue(int word){
    int index=showIndex(word);
    if(index==-1){
        return -1;
    }
    else
        return value[index];
}

void print(){
    for(int i=0;i<currentSize;i++){
        printf("%d:%d\n",keys[i],value[i]);
    }
}

void main(){
    printf("Map is : ");
    Insert(100,1);
    Insert(200,2);
    Insert(300,3);
    print();

    printf("value of key 100 is %d",showValue(100));
}
