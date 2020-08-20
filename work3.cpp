#include<iostream>
using namespace std;

template<class Type>
int Partition (Type a[], int p, int r)
{
	int i = p, j = r;
	Type x=a[p];
	while (true) {
		while (i<j && a[i] <=x) i++; // 将> x的元素交换到右边区域
		while (i<j && a[j] >=x) j--; // 将< x的元素交换到左边区域
		if (i>=j) break;
		swap(a[i], a[j]);
	}
	if(j!=r) {
		a[p] = a[j-1];
		a[j-1] = x;
		return j-1;
	} else {
		a[p] = a[j];
		a[j] = x;
		return j;
	}
}
//4 1 2 3 5 6 7 8 9 10原
//6 1 2 3 4 5 7 8 9 10现
int part(int *a,int l,int r)
{
	int temp=a[l];
	int u=r,d=l;
	while(u>d)
	{
		while(a[u]>=temp&&u>d)
			u--;
		while(a[d]<=temp&&u>d)
			d++;
		swap(a[u],a[d]);
	}
	swap(a[l],a[u]);
	return u;
 } 
void sort(int *a,int l,int r)
{
	if(l>=r)return;
	int t=part(a,l,r);
	sort(a,l,t);
	sort(a,t+1,r);
} 

int main()
{
//	int a[10]={5,10,9,8,7,6,4,3,2,1};
//	int a[10]= {10,9,8,7,6,5,4,3,2,1};
//	int a[10]={9,10,8,7,6,5,4,3,2,1};
	int a[10]={1,20,3,4,5,6,7,8,9,10};
	for(int i=0; i<10; i++)cout<<a[i]<<" ";
	cout<<endl;
//	Partition(a,0,9);
	sort(a,0,9);
	for(int i=0; i<10; i++)cout<<a[i]<<" ";
	cout<<endl;

}
