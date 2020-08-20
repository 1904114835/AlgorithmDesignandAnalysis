#include <stdio.h>

#define N 6        //������/����

int weight[][N] = {{0,2,2,3,1,4},{2,0,1,5,2,3},{2,1,0,2,1,4},{3,5,2,0,6,2},
{1,2,1,6,0,1},{4,3,4,2,1,0}};

int t[N][N];    //t[i][j]��ʾ�����{Vi-1VkVj}������Ȩֵ
int s[N][N];    //s[i][j]��¼Vi-1��Vj���������ʷֵ��м��K

int get_weight(const int a, const int b, const int c)
{
    return weight[a][b] + weight[b][c] + weight[c][a];
}

void minest_weight_val()
{
    int i,r,k,j;
    int min;

    for (i = 1; i < N; i++)
    {
        t[i][i] = 0;
    }

    for (r = 2; r < N; r++)
    {
        for (i = 1; i < N-r+1; i++)
        {
            j = i + r -1;
            min = 9999;        //������Сֵ
            for (k = i; k < j; k++)
            {
                t[i][j] = t[i][k] + t[k+1][j] + get_weight(i-1,k,j);
                if (t[i][j] < min)        //�ж��Ƿ�����Сֵ
                {
                    min = t[i][j];
                    s[i][j] = k;    
                }
            }
            t[i][j] = min;        //ȡ�ö����{Vi-1��Vj}�Ļ���������СȨֵ
        }
    }
}

void back_track(int a, int b)
{
    if (a == b) return;
    back_track(a,s[a][b]);
    back_track(s[a][b]+1,b);    //�ǵ�����Ҫ��һ
    printf("��������: V%d V%d V%d.\n",a-1,s[a][b],b);
}



int main()
{
    minest_weight_val();
    printf("result:%d\n",t[1][N-1]);
    back_track(1,5);
    return 0;
}
