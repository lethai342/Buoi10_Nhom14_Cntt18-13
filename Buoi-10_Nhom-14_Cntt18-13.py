import

edges = [(1,0,1), (3,0,2), (4,1,2), (2,1,3), (5,2,3)]
n = 4   # số đỉnh (0..3)

parent = list(range(n))
def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x,y):
    parent[find(x)] = find(y)

def kruskal(n, edges):
    edges.sort()
    global parent
    parent = list(range(n))
    mst = []
    total = 0
    for w,u,v in edges:
        if find(u) != find(v):
            union(u,v)
            mst.append((u,v,w))
            total += w
    return total, mst

total, mst = kruskal(n, edges)
print("\nMST ban đầu:", mst, " - Tổng trọng số:", total)

edges2 = edges + [(6,1,3)]
total2, mst2 = kruskal(n, edges2)
print("\nSau khi thêm cạnh (1,3,6):", mst2, "- Tổng trọng số:", total2)
print("=> Không thay đổi vì cạnh (1,3,2) nhỏ hơn cạnh (1,3,6).")

edges3 = [(3,0,1), (3,0,2), (4,1,2), (2,1,3), (5,2,3)]
total3, mst3 = kruskal(n, edges3)
print("\nSau khi đổi (0,1)=3:", mst3, "- Tổng trọng số:", total3)
print("=> MST thay đổi, trọng số tăng do cạnh (0,1) không còn nhẹ nhất.")

edges4 = [
    (1,0,1), (2,0,2), (5,1,2), (3,1,3),
    (4,2,4), (2,3,4), (6,3,5), (1,4,5)
]
total4, mst4 = kruskal(6, edges4)
print("\nMST cho đồ thị 6 đỉnh:", mst4, "- Tổng trọng số:", total4)
print("=> MST vẫn chọn cạnh nhỏ nhất, nhưng có 5 cạnh (n-1).")
