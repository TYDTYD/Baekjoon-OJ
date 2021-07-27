#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	long long result = 0;
	int h, a;
	cin >> n;

	vector<pair<int, int>> tree(n);

	for (int i = 0; i < tree.size(); i++)
	{
		cin >> tree[i].second; // ù ���� ���� ����
	}
	for (int i = 0; i < tree.size(); i++)
	{
		cin >> tree[i].first; // �Ϸ翡 �ڶ�� ����
	}
	sort(tree.begin(), tree.end());  // first ���� �����ؾ��ϹǷ� �Ϸ翡 �ڶ�� ���̸� first�� ����

	for (int i = 0; i < n; i++)
	{
		result += tree[i].first * i + tree[i].second; // i ���ϴ� ������ ���ݱ��� �ڸ��� �ʰ� ������ ���̸� ��Ÿ���� ����, second�� ù�� ° �� �����ִ� ����
	}

	cout << result;

	return 0;
}