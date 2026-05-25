/* परिवर्तिनि संसारे मृतः को वा न जायते |
   स  जातो येन जातेन याति वंश समुन्नतिम्||  */
   
#include<bits/stdc++.h>
#define Fastio ios_base::sync_with_stdio(false);cin.tie(0);
using namespace std;
typedef long double lld;
typedef unsigned long long ull;
typedef long long ll;

constexpr int MOD=1e9+7;

#ifdef ARPIT
#include "karpit.h"
#define deb(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define deb(x...)
#endif


signed main() {
Fastio
#ifdef ARPIT
    freopen("error.txt", "w", stderr);
#endif
    int t  = 1;
    cin>>t; 
    // Solve Here 
    while(t--){
      int n;
      cin>>n;
      vector<int> a(n);
      int total=0;
      for(int i=0;i<n;i++){
        cin>>a[i];
        total+=a[i];
      }

      int maxi=*max_element(a.begin(), a.end());
      int mini=*min_element(a.begin(), a.end());

      int ok=(maxi+mini)/2;

      cout<<max(abs(mini-ok), abs(maxi-ok))<<"\n";
    }
    return 0;
}