学习笔记

1. 数组的相对排序 
   
    输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19]  arr2 = [2,1,4,3,9,6]
    输出：[2,2,2,1,4,3,3,9,6,7,19]
   
    根据数组2元素的位置排序数组1的内容，不包含的部分升序排列

    解法1： python 
    
        def get_py(arr1,arr2):
            def cmp(x):
                return (0,rank[x]) if x in ranke else (1,x)

            rank={value:index for index, value in enumerate}
            arr1.sort(key=cmp)
            return arr1
   
    解法2：计数排序
   
        def get_count(arr1,arr2):
            max_value=max(arr1)
            frequence=[0]*(max_value+1)
            for item in arr1:
                frequence[item]+=1
            result=[]
            for item in arr2:
                result.extend([item]*frequency[item])
                frequence[item]=0
            for item in range(max_value+1):
                if frequence[item]>0:
                    result.extend(frequence[item]*[item])
            return result