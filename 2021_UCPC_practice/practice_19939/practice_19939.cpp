#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// �� �Ͷ߸���

int main()
{
	int n, k;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> k;

	if (n < k)
		cout << -1;
	
	return 0;
}