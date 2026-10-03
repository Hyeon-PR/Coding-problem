#include <iostream>
#include <vector>
using namespace std;

int MOD = 1'000'000'007;
vector<long long> fact(4'000'001, 1);     // fact[i] = i! % MOD
vector<long long> inv_fact(4'000'001, 1); // inv_fact[i] = (i!)^(-1) % MOD

// nCr = n! / (r! * (n - r)!)
// nCr = n! * (r!)^(-1) * ((n - r)!)^(-1)

long long binomial_coefficient(int n, int r)
{ // nCr을 구하는 함수
    if (n < r)
        return 0;
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD;
}

long long modpow(long long base, long long exp)
{ // 분할정복을 이용한 거듭제곱 -> 지수를 절반씩 줄이며 밑을 제곱함 (O(log exp))
    long long result = 1;
    while (exp > 0)
    {
        if (exp % 2 == 1)
            result = result * base % MOD;
        base = base * base % MOD;
        exp /= 2;
    }
    return result;
}

// 페르마의 소정리: MOD가 소수이고 a가 MOD의 배수가 아니면 a^(MOD-1) ≡ 1 (mod MOD)
// 양변에 a^(-1)을 곱하면 a^(MOD-2) ≡ a^(-1) (mod MOD)
// n < MOD이므로 n!은 MOD의 배수가 아님 -> (n!)^(-1) ≡ fact[n]^(MOD-2) (mod MOD)
// (i!)^(-1) = ((i+1)!)^(-1) * (i+1) 이므로 inv_fact는 끝 값 하나만 거듭제곱으로 구하고 역순으로 채움
void precompute_factorials()
{
    fact[0] = 1;
    for (int i = 1; i <= 4'000'000; i++)
    {
        fact[i] = fact[i - 1] * i % MOD;
    }
    inv_fact[4'000'000] = modpow(fact[4'000'000], MOD - 2); // 페르마의 소정리
    for (int i = 4'000'000 - 1; i >= 0; i--)
    {
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD;
    }
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);

    int M; // M개의 (N, K) 쌍
    cin >> M;
    vector<pair<int, int>> v(M); // binomial coefficient의 (N, K) 쌍
    for (int i = 0; i < M; i++)
    {
        cin >> v[i].first >> v[i].second;
    }

    precompute_factorials(); // 팩토리얼과 역팩토리얼을 미리 계산
    for (int i = 0; i < M; i++)
    {
        int N = v[i].first;
        int K = v[i].second;
        cout << binomial_coefficient(N, K) << '\n';
    }
}