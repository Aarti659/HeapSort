//C++ program to implement heap sort

#include <iostream.h>

using namespace std;

static void heapsort(int Array[], int n);
static void heapify(int Array[], int n, int j);
static void PriArr(int Array[], int n);


static void heapsort(int Array[], int n) {
  int temp;

  for(int j = n/2; j >= 0; j--) {
    heapify(Array, n-1, j);
  }
  
  for(int j = n - 1; j >= 0; j--) {
    
    temp = Array[j];
    Array[j] = Array[0];
    Array[0] = temp;

    
    heapify(Array, j-1, 0);
  }
}


static void heapify(int Array[], int n, int j) {
  int max = j;
  int left = 2*j + 1;
  int right = 2*j + 2;

  
  if(left <= n && Array[left] > Array[max]) {
    max = left;
  }

  
  if(right <= n && Array[right] > Array[max]) {
    max = right;
  }

  
  if(max != j) {
    int temp = Array[j];
    Array[j] = Array[max];
    Array[max] = temp;
    
    heapify(Array, n, max); 
  }
}


static void PriArr(int Array[], int n) { 
  for (int j=0; j<n; j++) 
    cout<<Array[j]<<" "; 
  cout<<"\n"; 
} 


int main () {
  int MyArray[] = {20, 1, 23, 40, 7, -4};
  int n = sizeof(MyArray) / sizeof(MyArray[0]); 
  cout<<"Original Array\n";
  PriArr(MyArray, n);

  heapsort(MyArray, n);
  cout<<"\nSorted Array\n";
  PriArr(MyArray, n);
  return 0;
}



















