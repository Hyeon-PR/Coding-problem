# Coding-problem

알고리즘·자료구조 문제 풀이 저장소입니다. 2024년부터 풀이 하나에 커밋 하나씩 남기고 있습니다.

<a href="https://solved.ac/lhbj1115"><img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=lhbj1115" alt="solved.ac 프로필" /></a>

![commits per year](https://img.shields.io/github/commit-activity/y/Hyeon-PR/Coding-problem?label=commits%20%2F%20year)

## 대표 풀이

| 유형 | 문제 | 접근 | 코드 |
|---|---|---|---|
| 격자 그래프 | BOJ 9376 탈옥 | 세 출발점에서 0-1 BFS, 칸별 비용 합산 | [C++](baekjoon/tier/platinum-4/탈옥.cpp) |
| 격자 그래프 | BOJ 4991 로봇 청소기 | (위치, 청소한 칸 비트마스크) 상태 BFS | [C++](baekjoon/tier/gold-1/로봇%20청소기.cpp) |
| 격자 그래프 | BOJ 1981 배열에서 이동 | 값 범위를 투 포인터로 좁히며 BFS로 도달 판정 | [C++](baekjoon/tier/platinum-5/배열에서%20이동.cpp) |
| 그래프 | BOJ 2150 Strongly Connected Component | Kosaraju | [C++](baekjoon/class/6/SCC.cpp) |
| 트리 | BOJ 11438 LCA 2 | Binary lifting | [C++](baekjoon/class/6/LCA2.cpp) |
| 문자열 | BOJ 1786 찾기 | KMP | [C++](baekjoon/class/6/찾기.cpp) |
| 문자열 | BOJ 15164 제보 | Manacher | [C++](baekjoon/tier/platinum-5/15164번_제보.cpp) |
| DP | BOJ 14003 가장 긴 증가하는 부분 수열 5 | O(N log N) LIS와 역추적 | [C++](baekjoon/class/5/가장긴증가하는부분수열5.cpp) |

## 구성

| 경로 | 분류 기준 |
|---|---|
| [`baekjoon/tier/`](baekjoon/tier) | 백준, 풀었을 당시의 solved.ac 티어 |
| [`baekjoon/class/`](baekjoon/class) | 백준, solved.ac CLASS |
| [`baekjoon/step/`](baekjoon/step) | 백준 「단계별로 풀어보기」 |
| [`baekjoon/topic/`](baekjoon/topic) | 백준, 알고리즘·자료구조 주제 |
| [`leetcode/`](leetcode) | LeetCode, 주제 |
| [`programmers/`](programmers) | 프로그래머스, 레벨 |
| [`codeforces/`](codeforces) | Codeforces |

백준 풀이는 그 시기에 공부하던 방식에 따라 네 기준 중 하나에 들어 있습니다. 백준이 2026년 4월 말 서비스를 중단한 뒤로는 LeetCode·프로그래머스·Codeforces에서 이어가고 있습니다.

## 커밋 메시지

2025년 하반기부터 커밋 메시지에 `주제 - 핵심 아이디어`를 적습니다. [커밋 기록](https://github.com/Hyeon-PR/Coding-problem/commits/main)에서 문제별 접근을 볼 수 있습니다.

```
Union Find - application for global set
Two pointer - O(n+m) solution for the previous commit by storing temporal optimized value
Stack - single-threaded CPU execution using an explicit call stack
```
