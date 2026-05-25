#include <bits/stdc++.h>
using namespace std;

#define fastio()                 \
    ios::sync_with_stdio(false); \
    cin.tie(NULL)
#define ll long long
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define endl '\n'

void solve();
int main()
{
    fastio();

    int tt;
    cin >> tt;
    while (tt--)
    {
        solve();
    }

    return 0;
}
void solve()
{
    int n;
    cin >> n;

    vector<int> a(n);

    int mn = 100000, mx = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        mn = min(mn, a[i]);
        mx = max(mx, a[i]);
    }

    int ans = (mx - mn + 1) / 2;

    cout << ans << endl;
}