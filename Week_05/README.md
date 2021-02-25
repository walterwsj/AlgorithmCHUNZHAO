学习笔记

并查集模板
    
    class UnionFind:
        def __init__(self):
            self.count=0
            self.parent={}
        def find(self,x):
            root=x
            while self.parent[root] is not None:
                root=self.parent[root]
            while root!=x:
                original_parent=self.parent[x]
                self.parent[x]=None
                x=original_parent
            return root

        