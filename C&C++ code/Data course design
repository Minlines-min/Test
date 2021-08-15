#include<stdio.h>
#include<iostream>
#include <cstring>

using namespace std;

#define Max_ver 100                                               //最大结点数量
#define Malloc_new(type,n)      (type*)malloc(sizeof(type)*n);    //申请空间函数模板

int ve[Max_ver];                                                  //最早开始时间
int vl[Max_ver];                                                  //最晚开始时间

int indegree[Max_ver];                                            //入度
int outdegree[Max_ver];                                           //出度

int adjvex_list[Max_ver];                                         //关键事件下标数组

char* path;                                                       //记录当前关键路径数组

int graph_start[Max_ver];                                         //起点数组
int graph_end = 0;                                                //初始化终点

typedef struct Arc_node
{
    int adjvex;                                                   //头邻接点在数组下标
    struct Arc_node* next = NULL;                                 //指针域
    int wieght;                                                   //权值（活动时间）
}Arc_node,*ptr_Arc_node;

typedef struct Vn_node
{
    char data;                                                    //数据域
    ptr_Arc_node firstarc = NULL;                                 //邻接点指针域
}Vn_node,*Adj_list[Max_ver];

typedef struct Graph                                              //图
{
    Adj_list ver;                                                 //头邻接点数组
    int num_ver;                                                  //邻接点数
    int num_arc;                                                  //边数
}Graph,*ptr_Graph,**ptr_ptr_Graph;

typedef struct stack
{
    char data;                                                    //数据域
    struct stack* next;                                           //指针域
}stack,*ptr_stack,**ptr_ptr_stack;

stack* assist_stack;                                              //辅助栈，求最晚开始时间

void create_base_stack(ptr_ptr_stack p)                           //初始化栈
{
    (*p) = Malloc_new(stack, 1);
    (*p)->next = NULL;
}

bool stack_empty(ptr_stack p)                                     //栈是否为空
{
    if (p->next == NULL)
    {
        return 1;
    }
    return 0;
}

void push(ptr_stack p, char c)                                    //入栈函数
{
    ptr_stack temp = Malloc_new(stack, 1);
    temp->data = c;
    temp->next = NULL;
    temp->next = p->next;                                         //头插法
    p->next = temp;
}

void pop(ptr_stack p,char* c)                                     //出栈函数
{
    ptr_stack temp = p->next;
    (*c) = temp->data;                                            //参数指针传出数据
    p->next = p->next->next;
    free(temp);
}

int return_vn_subscript(Graph g, char c)                          //返回结点下标函数
{
    for (int i = 0; i < g.num_ver; i++)
    {
        if (g.ver[i]->data == c)
        {
            return i;
        }
    }
    printf("Erro\n");                                             //查询数据不存在
    return 0;
}

void create_base_graph(ptr_ptr_Graph g)                           //创建图的邻接表
{
    int wieght;
    char data_begin,data_end;
    (*g) = Malloc_new(Graph, 1);
    //scanf("%d %d", &((*g)->num_ver), &((*g)->num_arc));
    printf("Please input ver's num & arc's num:\n");
    cin >> (*g)->num_ver >> (*g)->num_arc;
    printf("Please input data:\n");
    for (int i = 0; i < (*g)->num_ver; i++)                       //输入数据，初始化头邻接点数组
    {
        //scanf("%c", g->ver[i]->data);
        (*g)->ver[i]=Malloc_new(Vn_node,1);
        cin >> (*g)->ver[i]->data;
        (*g)->ver[i]->firstarc = NULL;
    }
    for (int i = 0; i < (*g)->num_arc; i++)                       //创建邻接表
    {
        printf("Please input %d arc realationship:",i+1);
        cin >> data_begin >> data_end >> wieght;
        ptr_Arc_node p = Malloc_new(Arc_node, 1);
        p->adjvex = return_vn_subscript(*(*g), data_end);         //终点下标赋值
        p->next = NULL;
        p->wieght = wieght;
        int j = return_vn_subscript(*(*g), data_begin);           //起点下标赋值
        p->next = (*g)->ver[j]->firstarc;
        (*g)->ver[j]->firstarc = p;
    }
}

void statistics_in_degree(Graph g,int *indegree)                  //统计事件入度
{
    for (int i = 0; i < g.num_ver; i++)
    {
        indegree[i] = 0;
    }
    for (int i = 0; i < g.num_ver; i++)
    {
        for (ptr_Arc_node p = g.ver[i]->firstarc; p; p = p->next) //链接事件入度加1
        {
            indegree[p->adjvex]++;
        }
    }
}

void statistics_out_degree(Graph g, int *outdegree)               //统计事件出度
{
    for (int i = 0; i < g.num_ver; i++)
    {
        outdegree[i] = 0;
        for (ptr_Arc_node p = g.ver[i]->firstarc; p; p = p->next) //出度等于链表结点个数
        {
            outdegree[i]++;
        }
    }
}



bool topological_sort(Graph g)                                    //拓扑排序函数
{
    int count = 0;
    statistics_in_degree(g, indegree);                            //统计所有邻接点
    ptr_stack s;                                                  //创建拓扑排序用栈
    create_base_stack(&s);                                        //初始化栈
    create_base_stack(&assist_stack);                             //初始化辅助栈
    for (int i = 0; i < g.num_ver; i++)
    {
        ve[i] = 0;                                                //初始化所有活动最早开始时间为0
    }
    for (int i = 0; i < g.num_ver; i++)
    {
        if (!indegree[i])
        {
            push(s, g.ver[i]->data);                              //入度为0，入栈
        }
    }
    while (!stack_empty(s))                                       //栈为空时拓扑排序完成
    {
        char c;
        int temp;
        pop(s, &c);                                               //出栈（顺序）
        push(assist_stack, c);                                    //入栈，准备求最晚开始时间（逆序）
        temp = return_vn_subscript(g, c);                         //记录出栈下标
        count++;
        for (ptr_Arc_node p = g.ver[temp]->firstarc; p; p = p->next)
        {
            int i = p->adjvex;
            if (!(--indegree[i]))                                 //删除与出栈函数有关的边，更改有关结点的入度（-1）
            {
                push(s, g.ver[i]->data);                          //该结点入栈
            }
            if ((ve[temp] + p->wieght) > ve[i])                   //计算各个结点的最早开始时间，取最大值
            {
                ve[i] = ve[temp] + p->wieght;
            }
        }
    }
    if (count < g.num_ver)
    {
        printf("Have joop.\n");                                   //存在环
        return 0;
    }
    else
    {
        printf("Topo ok\n");
        return 1;
    }
}

bool if_critical_event(int i,int n)                               //判断该事件是否为关键事件
{
    for (int j = 0; j < n; j++)
    {
        if (i == adjvex_list[j])
        {
            return 1;
        }
    }
    return 0;
}



bool find_simlple_path(Graph g, int j, int i, int m,int size)     //递归输出函数
{
    if (j == i)
    {
        path[m] = '\0';                                           //指定字符数组尾地址
        int k = strlen(path);                                     //计算字符数组长度
        for (int n = 0; n < k; n++)
        {
            printf("<%c> ", path[n]);                             //输出字符数组
            if (n + 1 != k)                                       //控制格式
            {
                printf("->");
            }
        }
        printf("\n");
        return 1;                                                 //打印完成，出栈
    }
    else
    {
        for (ptr_Arc_node p = g.ver[j]->firstarc; p; p = p->next) //邻接点不为空时向后遍历
        {
            if (if_critical_event(p->adjvex,size))                //邻接点是关键事件
            {
                path[m] = g.ver[p->adjvex]->data;                 //添加邻接点数据（出栈后复写）
                find_simlple_path(g, p->adjvex, i, m + 1, size);  //向后遍历邻接点
            }
        }
    }
    return 1;                                                     //全部打印完成，出栈
}

void print(Graph g,int size)                                      //打印函数
{
    int  i,count = 0;
    path = Malloc_new(char, size + 1);                            //申请指针数组空间为关键事件数+1
    for (i = 0; i < size; i++)
    {
        if (indegree[adjvex_list[i]] == 0)
        {
            graph_start[count++] = adjvex_list[i];                //关键事件入度为0为起点（多起点）
        }
        else if (outdegree[adjvex_list[i]] == 0)
        {
            graph_end = adjvex_list[i];                           //关键事件出度为0为终点（单终点）
        }
    }
    for (i = 0; i < count; i++)                                   //输出全部起点到终点路径
    {
        path[0] = g.ver[graph_start[i]]->data;                    //起点赋值
        find_simlple_path(g, graph_start[i], graph_end, 1, size); //递归函数
    }
}

int ve_max(int n)                                                 //最大最早开始时间
{
    int temp = ve[0];
    for (int i = 1; i < n; i++)
    {
        if (ve[i] > temp)
        {
            temp = ve[i];
        }
    }
    return temp;
}

void critical_path(Graph g)                                       //统计输出关键路径函数
{
    int temp,i,n = 0;
    char c;
    statistics_in_degree(g, indegree);                            //重新统计所有邻接点入度
    statistics_out_degree(g, outdegree);                          //统计邻接点出度
    for (i = 0; i < g.num_ver; i++)
    {
        vl[i] = ve_max(g.num_ver);                                //初始化最晚开始时间为最早开始时间最大值
    }
    while (!stack_empty(assist_stack))                            //辅助栈为空计算结束
    {
        pop(assist_stack, &c);
        i = return_vn_subscript(g, c);                            //记录出栈事件下标
        for (ptr_Arc_node p = g.ver[i]->firstarc; p; p = p->next)
        {
            temp = p->adjvex;
            if ((vl[temp] - p->wieght) < vl[i])
            {
                vl[i] = vl[temp] - p->wieght;                     //计算最晚开始时间，取最小值
            }
        }
    }
    for (i = 0; i < g.num_ver; i++)
    {
        if ((indegree[i] == 0)&&(vl[i] == 0))                     //入度为0且最晚开始时间为0的事件必为起点
        {
            adjvex_list[n++] = i;                                 //统计起点加入关键事件下标数组
        }
        for (ptr_Arc_node p = g.ver[i]->firstarc; p; p = p->next) //遍历
        {
            temp = p->adjvex;
            int ee = ve[i];                                       //边最早发生时间等与结点最早开始时间
            int el = vl[temp] - p->wieght;                        //边最晚发生时间等于结点最晚开始时间减去该活动持续时间
            if (ee == el)                                         //两者相等时，该活动为关键活动，活动两点为关键事件
            {
                if (!if_critical_event(temp, n))
                {
                    adjvex_list[n++] = temp;                      //关键事件下标统计
                }
            }
        }
    }
    print(g, n);
}

void free_graph(ptr_Graph g)                                      //释放空间
{
    ptr_Arc_node p;
    ptr_Arc_node q;                                               //防止断链
    for (int i = 0; i < g->num_ver; i++)
    {
        p = g->ver[i]->firstarc;
        while (p)
        {
            q = p->next;
            free(p);
            p = q;
        }
    }
}

int main()
{
    ptr_Graph g;
    create_base_graph(&g);
    topological_sort((*g));
    critical_path((*g));
    free_graph(g);
    system("pause");
    return 0;
}
