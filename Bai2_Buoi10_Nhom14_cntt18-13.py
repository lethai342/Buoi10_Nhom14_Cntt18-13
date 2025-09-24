import heapq

edges = [
    (0, 1, 1),
    (0, 3, 2),
    (1, 2, 3),
    (1, 4, 2),
    (2, 4, 1),
    (2, 5, 3),
    (3, 5, 2)
]

G = {}
for u,v,w in edges:
    G.setdefault(u,[]).append((v,w))
    G.setdefault(v,[]).append((u,w))

def prim(start, G):
    visited = set()
    heap = [(0, start, -1)]
    total_weight = 0
    mst_edges = []
    print(f"\nBắt đầu từ đỉnh {start}")
    while heap:
        w,u,parent = heapq.heappop(heap)
        if u in visited: 
            continue
        visited.add(u)
        total_weight += w
        if parent != -1:
            print(f"  -> Chọn cạnh ({parent},{u}) trọng số {w}")
            mst_edges.append((parent,u,w))
        for v,wt in G.get(u,[]):
            if v not in visited:
                heapq.heappush(heap,(wt,v,u))
    print(f" Tổng trọng số: {total_weight}")
    return total_weight, mst_edges

prim(0, G)

edges_new = edges + [(4,6,3),(5,6,2)]
G2 = {}
for u,v,w in edges_new:
    G2.setdefault(u,[]).append((v,w))
G2.setdefault(v,[]).append((u,w))
print("\nSau khi thêm đỉnh 6:")
prim(0, G2)
print("=> MST có thêm 1 cạnh để nối với đỉnh 6, tổng trọng số tăng.")

print("\nBắt đầu từ đỉnh 3:")
prim(3, G)
print("=> Tổng trọng số không đổi, nhưng thứ tự chọn cạnh khác.")

edges_mod = [
    (0, 1, 1),
    (0, 3, 6),
    (1, 2, 3),
    (1, 4, 2),
    (2, 4, 1),
    (2, 5, 3),
    (3, 5, 2)
]
G3 = {}
for u,v,w in edges_mod:
    G3.setdefault(u,[]).append((v,w))
    G3.setdefault(v,[]).append((u,w))
print("\nSau khi đổi (0,3)=6:")
prim(0, G3)
print("=> Cạnh (0,3) bị bỏ vì quá nặng, MST chọn cạnh khác nhẹ hơn.")
