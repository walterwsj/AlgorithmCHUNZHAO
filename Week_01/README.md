学习笔记


删除排序数组中的重复项

方法: 根据已排序特性，重复元素必相邻
定义两个指针，一个在前一个在后，如果后一个指针指向的元素跟前一个指针所指元素不同，就把
这个不同的元素赋值给前一指针的下一位；如果相同前指针不动，后指针继续向前。直到后指针到达数组
的末尾，前指针停止的地方正好就是非重复的最后一个元素
    while q<len_nums:
        if nums[p]!=nums[q]:
            p+=1
            nums[p]=nums[q]
        else:
            q+=1
    return p+1

旋转数组
注意参数K的判断 
    是否为数组长度的整数倍 如果是 直接返回原数组即可
    如果是负数 正向循环长度-k的次数

方法一:
    字面意思 循环K次 数组所有元素全部依次向右移动即可
    while k:
        tmp=nums[-1]
        for i in range(len_nums)[::-1]:
            nums[i]=nums[i-1]
        nums[0]=tmp
        k-=1

方法二:
    字符串反转 全部反转->[:k-1]反转->[k:]反转
    reverse(nums,0,len_nums-1)
    reverse(nums,0,k-1)
    reverse(nums,k,len_nums-1)

方法三:
    借用辅助空间
    1. 循环队列索引思想
        slave=copy.deepcopy(nums)
        for i in range(len_nums):
            nums[(i+k)%len_nums]=slave[i]
    2. 已知结果拼结果
        slave=nums[:len_nums-k]
        # k 之前的元素删除
        for i in range(len_nums-k):
            del nums[0]
        nums.extend(slave)


合并两个有序数组

方法1：典型归并排序思想 确定结果的末尾元素所以 依次从后向前赋值即可 缺点就是遍历的
长度过长会影响时间复杂度

方法2：以较短长度列表为外循环
    i, j, k = m - 1, n - 1, m + n - 1
    while j>0:
        while i>=0 and nums2[j]<nums1[i]:
            swap(nums1[i],nums1[k])
            i-=1
            k-=1
        swap(nums2[j],nums1[k])
        j-=1
        k-=1


两数之和

方法1: 暴力 两层循环

方法2: 利用字典 哈希特性 一次循环
        for index,value in enumerate(nums):
            rest=target-value
            if rest in dict:
                res.append(dict[rest],i)
            else:
                dict[value]=index

移动零

方法一:两个指针 一个记录非零元素的下一个位置 另一个向前探索非零元素 如果有零出现 
两指针会产生差值 交换位置即可

方法二:设置一个index只记录非零元素。遍历结束index位置之后的元素全部赋值为零
        for i in range(len_nums):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
        while index<len_nums:
            nums[index]=0
            index+=1
        return nums

加一

方法一:
数组转为数字，加1后返回（统计第一元素开始连续为零的个数）

方法二:
先在结果数组之前加一位 逢9为0 后一位加1
    digits=[0]+digits
    for i in range(len_digits)[::-1]:
        if digits[i]==9:
            digits[i]=0
        else:
            digits[i]+=1
            break
    if digits[0]==0:
        return digits[1:]
    else
        return digits