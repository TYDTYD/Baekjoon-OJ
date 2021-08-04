#include <iostream>
using namespace std;
// ��� ���ϱ�

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int n, p;
	long long songScore;

	cin >> n >> songScore >> p;
	long long* array = new long long[p];

	for (int i = 0; i < n; i++)
	{
		cin >> array[i];
	}

	int result = 1;
	int count = 0;
	for (int i = 0; i < n; i++)
	{
		if (songScore < array[i])
			result++;
		else if (songScore == array[i])
			result = result;
		else
			break;
		count++; 
	}

	if (count == p) // ����Ʈ ���̰� �Էµ� n���� ����(���߿����� )�� ���ٸ� 
		result = -1;
	if (n == 0)
		result = 1;

	delete[] array;
	cout << result << '\n';
	return 0;
}