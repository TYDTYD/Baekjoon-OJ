#include <iostream>
using namespace std;

// �� �Ͷ߸���

int main()
{
	int n, k, sum = 0;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> k;

	if (n > 2 && k == 2)
	{                    // �� ���ǿ��� n��
		if (n % 2 == 0)  // ¦���� ������ 2
			cout << 2;
		else             // Ȧ���� ������ 1
			cout << 1;
		return 0;
	}

	for (int i = 1; i <= k; i++)
		sum += i;

	n -= sum;



	return 0;
}