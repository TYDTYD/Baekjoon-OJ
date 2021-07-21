#include <iostream>

using namespace std;
// �ӽ� ���� ���ϱ�

int student[1000][5];
int studentCount[1000][1000] = { 0, };

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int num;
	cin >> num;


	for (int i = 0; i < num; i++)
	{
		for (int j = 0; j < 5; j++) // �г�
		{
			cin >> student[i][j];
		}
	}

	//for (int i = 0; i < num; i++)
	//{
	//	for (int j = 0; j < 5; j++) // �г�
	//	{
	//		cout << student[i][j] << " ";
	//	}
	//	cout << endl;
	//}

	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < num; j++)
		{
			for (int k = 0; k < num; k++)
			{
				if (k == j)
					continue;
				else if (student[j][i] == student[k][i])
				{
					studentCount[k][j] = 1;
				}
			}
		}
	}

	int maxCount = 0;
	int ans = 1; // ��� �л��� �ٸ� ���̾��ٸ� 1���
	for (int i = 0; i < num; i++)
	{
		int c = 1;
		for (int j = 0; j <= num; j++)
			c += studentCount[i][j];
		if (maxCount < c)
		{
			maxCount = c;
			ans = i + 1; // 
		}
	}
	cout << ans;

	return 0;
}