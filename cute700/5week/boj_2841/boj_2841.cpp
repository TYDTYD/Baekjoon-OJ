#include <iostream>
#include <stack>
// �ܰ����� ��Ÿ����
using namespace std;

int n, p, line, pNum, top;
stack<int> finger[7];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int result = 0;

	cin >> n >> p;
	for (int i = 0; i < n; i++)
	{
		cin >> line >> pNum;
		while (1)
		{
			if (finger[line].empty())
			{
				finger[line].emplace(pNum);
				result++;
				break;
			}
			top = finger[line].top();
			if (pNum == top) // �Է¹��� ������ ���� ������ ���α�
				break;
			else if (pNum > top) // �ƴ� ��� ���� �װ� ī��Ʈ
			{
				finger[line].emplace(pNum);
				result++;
			}
			else // �Է¹��� ������ �۴ٸ� ���� ���� �������� �հ��� ����
			{
				finger[line].pop();
				result++;
			}
		}
	}
	cout << result << '\n';

	return 0;
}