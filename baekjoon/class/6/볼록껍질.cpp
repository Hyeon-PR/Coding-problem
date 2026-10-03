#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
Andrew's Monotone Chain 알고리즘
- 볼록 껍질을 구하는 알고리즘 중 하나 (O(N log N))
- Graham Scan과 달리 기준점 각도 정렬 없이 좌표 정렬만 사용
- 볼록 껍질: 점들을 모두 포함하는 가장 작은 볼록 다각형
- 볼록 다각형: 모든 내각이 180도 미만인 다각형

1. 점들을 x좌표, x좌표가 같으면 y좌표 오름차순으로 정렬
2. 왼쪽에서 오른쪽으로 순회하며 아래 껍질을 구함
3. 오른쪽에서 왼쪽으로 순회하며 위 껍질을 구함
4. 마지막 두 점과 새 점이 반시계 방향(외적 > 0)이 아니면 마지막 점을 pop
   -> 일직선 위의 점(외적 == 0)도 빠지므로 변 위의 점은 양 끝만 남음
*/

struct Point
{
    long long x, y;
    bool operator<(const Point &p) const
    { // x좌표 오름차순, x좌표가 같으면 y좌표 오름차순
        return x < p.x || (x == p.x && y < p.y);
    }
};

long long cross(const Point &O, const Point &A, const Point &B)
{ // OA, OB 벡터의 외적 (result > 0: 반시계 방향, result < 0: 시계 방향, result == 0: 일직선)
    return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
}

vector<Point> convexHull(vector<Point> &points)
{ // 볼록 껍질 알고리즘
    int n = points.size(), k = 0;
    if (n <= 3)
        return points;
    vector<Point> hull(2 * n);

    // x좌표, x좌표가 같으면 y좌표 오름차순으로 정렬
    sort(points.begin(), points.end());

    // Build lower hull
    for (int i = 0; i < n; ++i)
    {
        while (k >= 2 && cross(hull[k - 2], hull[k - 1], points[i]) <= 0)
            k--; // 반시계 방향이 아니면 pop
        hull[k++] = points[i];
    }

    // Build upper hull
    for (int i = n - 1, t = k + 1; i >= 0; --i)
    {
        while (k >= t && cross(hull[k - 2], hull[k - 1], points[i]) <= 0)
            k--; // 반시계 방향이 아니면 pop
        hull[k++] = points[i];
    }

    hull.resize(k - 1);
    return hull;
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);

    int N; // 점의 개수
    cin >> N;
    vector<Point> points(N);
    for (int i = 0; i < N; i++)
    {
        cin >> points[i].x >> points[i].y;
    }

    vector<Point> hull = convexHull(points);

    cout << hull.size();
}