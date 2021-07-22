#include <iostream>

using namespace std;
// �ӽ� ���� ���ϱ�

int student[1000][5];
int studentCount[1000];

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int num;
	cin >> num;

	for (int i = 0; i < num; i++)
		studentCount[i] = 0;

	for (int i = 0; i < num; i++)
	{
		for (int j = 0; j < 5; j++) // �г�
		{
			cin >> student[i][j];
		}
	}

	for (int i = 0; i < num; i++) // ������ �л�
	{
		for (int j = 0; j < num; j++) // ���� �л�
		{
			for (int k = 0; k < 5; k++)
			{
				if (i == j)
					break;
				if (student[i][k] == student[j][k])
				{
					studentCount[i]++;
					break;
				}
			}
		}
	}

	int max = 0; // �ʱ� �ִ밪 ����
	int captain = 0; 
	for (int i = 0; i < num; i++)
	{
		if (max < studentCount[i])
		{
			max = studentCount[i];
			captain = i + 1;
		}
		else if (studentCount[i] == max)
			if (captain > i)
				captain = i + 1;
	}
	cout << captain << endl;

	for (int i = 0; i < num; i++) // �л� ���� ����̶� ���� ���̾����� ī��Ʈ ����
	{
		cout << studentCount[i] << ' ';
	}

	return 0;
}