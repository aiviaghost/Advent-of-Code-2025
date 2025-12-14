#include <bits/stdc++.h>

using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
// #define unordered_map gp_hash_table

#define int ll
#define all(xs) xs.begin(), xs.end()
#define in(xs, a) (xs.find(a) != xs.end())
#define sz(x) (ll)(x).size()
#define rep(i, a, b) for (int i = a; i < (b); ++i)

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using pdd = pair<double, double>;
using vi = vector<int>;

template <typename T>
vector<T> make(T init, size_t size) { return vector<T>(size, init); }
template <typename T, typename... Args>
auto make(T init, size_t first, Args... sizes)
{
    auto inner = make<T>(init, sizes...);
    return vector<decltype(inner)>(first, inner);
}

const int INF = 2e9;
const int MOD = 1e9 + 7;

template <class T>
int sgn(T x) { return (x > 0) - (x < 0); }
template <class T>
struct Point
{
    typedef Point P;
    T x, y;
    explicit Point(T x = 0, T y = 0) : x(x), y(y) {}
    bool operator<(P p) const { return tie(x, y) < tie(p.x, p.y); }
    bool operator==(P p) const { return tie(x, y) == tie(p.x, p.y); }
    P operator+(P p) const { return P(x + p.x, y + p.y); }
    P operator-(P p) const { return P(x - p.x, y - p.y); }
    P operator*(T d) const { return P(x * d, y * d); }
    P operator/(T d) const { return P(x / d, y / d); }
    T dot(P p) const { return x * p.x + y * p.y; }
    T cross(P p) const { return x * p.y - y * p.x; }
    T cross(P a, P b) const { return (a - *this).cross(b - *this); }
    T dist2() const { return x * x + y * y; }
    double dist() const { return sqrt((double)dist2()); }
    // angle to x-axis in interval [-pi, pi]
    double angle() const { return atan2(y, x); }
    P unit() const { return *this / dist(); } // makes dist()=1
    P perp() const { return P(-y, x); }       // rotates +90 degrees
    P normal() const { return perp().unit(); }
    // returns point rotated 'a' radians ccw around the origin
    P rotate(double a) const
    {
        return P(x * cos(a) - y * sin(a), x * sin(a) + y * cos(a));
    }
    friend ostream &operator<<(ostream &os, P p)
    {
        return os << "(" << p.x << "," << p.y << ")";
    }
};

using P = Point<ll>;

namespace std
{
    template <>
    struct hash<P>
    {
        size_t operator()(const P &p) const noexcept
        {
            return 100'000 * p.x + p.y;
        }
    };
}

signed main()
{
    cin.tie(0)->sync_with_stdio(0);

    vector<P> points;
    int x, y;
    char c;
    while (cin >> x >> c >> y)
    {
        points.push_back(P(x, y));
    }

    int n = points.size();
    unordered_set<P> outside;
    unordered_set<P> boundary;
    for (int i = 0; i < n; i++)
    {
        P p1 = points[i];
        P p2 = points[(i + 1) % n];

        auto [x1, y1] = p1;
        auto [x2, y2] = p2;

        P dirs[] = {
            P(0, -1),
            P(0, 1),
            P(-1, 0),
            P(1, 0)};
        P outside_dir;
        for (P dir : dirs)
        {
            P main = p2 - p1;
            if (main.cross(dir) < 0)
            {
                outside_dir = dir;
            }
        }

        if (x1 == x2)
        {
            for (int y = min(y1, y2); y <= max(y1, y2); y++)
            {
                auto [ox, oy] = P(x1, y) + outside_dir;
                outside.emplace(ox, oy);
                boundary.emplace(x1, y);
            }
        }
        else
        {
            for (int x = min(x1, x2); x <= max(x1, x2); x++)
            {
                auto [ox, oy] = P(x, y1) + outside_dir;
                outside.emplace(ox, oy);
                boundary.emplace(x, y1);
            }
        }
    }

    for (auto p : boundary)
    {
        outside.erase(p);
    }

    int ans1 = 0;
    int ans2 = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            auto [x1, y1] = points[i];
            auto [x2, y2] = points[j];

            bool valid = true;
            for (int x = min(x1, x2); x <= max(x1, x2) && valid; x++)
            {
                valid &= !in(outside, P(x, y1));
                valid &= !in(outside, P(x, y2));
            }
            for (int y = min(y1, y2); y <= max(y1, y2) && valid; y++)
            {
                valid &= !in(outside, P(x1, y));
                valid &= !in(outside, P(x2, y));
            }

            int area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1);
            ans1 = max(ans1, area);
            if (valid)
            {
                ans2 = max(ans2, area);
            }
        }
    }

    cout << ans1 << "\n";
    cout << ans2 << "\n";
}
