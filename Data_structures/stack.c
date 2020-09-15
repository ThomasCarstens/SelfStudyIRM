#include <stdio.h> //printf
#include <stdlib.h> //malloc
#include <unistd.h> //open write read close
#include <string.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
//#include <pthread.h> //pour le threading (makefile a modifier)

#include <errno.h> //errno perro


//////////////////////////////////

//STRUCT TYPEDEF
struct stack
{
  int maxsize;
  int top;
  int *items;
};
//Initialize stack with a function
struct stack* newStack(int capacity)
{
  struct stack *pt = (struct stack*)malloc(sizeof(struct stack));

  pt->maxsize = capacity;
  pt->top = -1;
  pt->items = (int*)malloc(sizeof(int)*capacity); //?
  return pt;
}

// Utility function to return the size of the stack1
int size(struct stack *pt)
{
  return pt -> top+1;
}

//.. to check if the stack is empty
int isEmpty(struct stack *pt)
{
  return pt -> top == -1; //ie. size(pt) == 0;   //validation in return?
}

//.. to check if the stack is full
int isFull(struct stack *pt)
{
  return pt->top == pt->maxsize -1; //ie. size(pt) == pt->maxsize;   //validation in return?
}

void push(struct stack *pt, int x)
{
  if (isFull(pt))
  {
    printf("Overflow");
    exit(EXIT_FAILURE);
  }
  printf("Inserting %d\n", x);

  pt -> items[++pt->top] = x;
}

//Return the top element.
int peek (struct stack *pt)
{
  if (!isEmpty(pt))
    return pt->items[pt->top];
  else
    exit(EXIT_FAILURE);
}
//Pop the top element
int pop(struct stack *pt)
{
  if (isEmpty(pt))
  {
    printf("UnderFlow\nProgram Terminated\n");
    exit(EXIT_FAILURE);
  }
  printf("Removing %d\n", peek(pt));
  return pt -> items [pt->top--];
}


int main(int argc, char const *argv[]){
  struct stack *pt = newStack(5);
  push(pt, 1);
  push(pt, 2);
  push(pt, 3);
  printf("Top element: %d\n: ", peek(pt));
  printf("Stack size: %d\n: ", size(pt));

  pop(pt);

}
