#include<iostream>
using namespace std;
int main()
{
	int maxv=5,temp,arg;
	int values[4]={12,10,20,15};
	int weight[4]={2,1,3,2};
	int take[5+1][4];
	static int dp[5+1];
	for(int i=0;i<5;i++)
	for(int j=0;j<4;j++)
		take[i][j]=1; 
	for(int i=1;i<=5;i++)
	{
		temp=dp[i];
		arg=-1;
		for (int j=0;j<4;j++)
		{
			if(i-weight[j]>=0&&dp[i-weight[j]]+values[j]>temp&& take[i-weight[j]][j]!=0)
			{
				temp=dp[i-weight[j]]+values[j];
				arg=j;
			}
				
		}
		if(temp>dp[i])
		{
			dp[i]=temp;
			for (int ttake=0;ttake<4;ttake++)
				take[i][ttake]=take[i-weight[arg]][ttake];
			take[i][arg]=0;
		}
	}
	cout<<dp[maxv]<<endl;
	for (int i=0;i<4;i++)
		cout<<take[maxv][i];
	return 0;
}
