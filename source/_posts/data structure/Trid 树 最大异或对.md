---
title: 
date: 2025-05-01 13:59:06
tags:
---

# Trid 数
![[Pasted image 20241119215849.png]]
![[Pasted image 20241119215858.png]]
插入操作代码
~~~
void insert(char *str)
{
    int p = 0;  //类似指针，指向当前节点
    for(int i = 0; str[i]; i++)
    {
        int u = str[i] - 'a'; //将字母转化为数字
        if(!son[p][u]) son[p][u] = ++idx;
        //该节点不存在，创建节点,其值为下一个节点位置
        p = son[p][u];  //使“p指针”指向下一个节点位置
    }
    cnt[p]++;  //结束时的标记，也是记录以此节点结束的字符串个数
}
~~~
查找操作代码
~~~
int query(char *str)
{
    int p = 0;
    for(int i = 0; str[i]; i++)
    {
        int u = str[i] - 'a';
        if(!son[p][u]) return 0;  //该节点不存在，即该字符串不存在
        p = son[p][u]; 
    }
    return cnt[p];  //返回字符串出现的次数
}
~~~
# 最大异或对
~~~
#include<iostream>
#include<algorithm>
using namespace std;
int const N=100010,M=31*N;

int n;
int a[N];
int son[M][2],idx;
//M代表一个数字串二进制可以到多长

void insert(int x)
{
    int p=0;  //根节点
    for(int i=30;i>=0;i--)
    {
        int u=x>>i&1;   /////取X的第i位的二进制数是什么  x>>k&1(前面的模板)
                        // 移动后，若最后一位与1 相同则为1， 否则为0
                        //& : 只有全部为1才为1
        if(!son[p][u]) son[p][u]=++idx; ///如果插入中发现没有该子节点,开出这条路
        p=son[p][u]; //指针指向下一层
    }
}
int search(int x)
{
    int p=0;int res=0;
    for(int i=30;i>=0;i--)
    {                               ///从最大位开始找
        int u=x>>i&1;
        if(son[p][!u]) ////如果当前层有对应的不相同的数
        {   ///p指针就指到不同数的地址

          p=son[p][!u];
          res=res*2+1;
             ///*2相当左移一位  然后如果找到对应位上不同的数res+1 例如    001
        }                                                       ///       010 
        else                                            ////          --->011                                                                           //刚开始找0的时候是一样的所以+0    到了0和1的时候原来0右移一位,判断当前位是同还是异,同+0,异+1
        {
            p=son[p][u];
            res=res*2+0;
        }
    }
    return res;
}
int main(void)
{
    cin.tie(0);
    cin>>n;
    idx=0;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
        insert(a[i]);
    }
    int res=0;
    for(int i=0;i<n;i++)
    {   
        res=max(res,search(a[i]));  ///search(a[i])查找的是a[i]值的最大与或值
    }
    cout<<res<<endl;
}
~~~