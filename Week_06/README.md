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


2. 有效的字母异位词

   字母 字母个数相同，位置不同的多个单词

   解法1： python
      

      def is_True(word_1,word_2):
            return collections.Counter(word_1)==collections.Counter(word_2)


   解法2： 设置一个26长度的字母数组 统计每个字母出现的次数
   

      def is_true(word_1,word_2):
         if len(word_1)!=len(word_2):
            return False
         counts=26*[0]
         for i in range(len(word_1):
            counts[ord(word_1[i])-ord("a")]+=1
            counts[ord(word_2[i])-ord("a")]-=1
         for x in counts:
            if x > 0:
               return False
         return True



3. 字符串里第一个唯一字符

   解法1： 用Counter统计单词里各个字符出现的次数；顺序遍历这个字典，第一个唯一的元素就是答案


         def get_char(word_1):
            dic=collection.Counter(word_1)
            for index,value in enumerate(word_1):
               if dic[value]==1:
                     return index
            return -1


4. 反转字符串里的单词


   解法1： 用python切片功能提供反序 strip()去掉空格 split('')转list
   

         def get_reverse(str_test):
            return ".join([i for i in str_test.strip().split(' ') if i][::-1])


         def get_reverse_deque(str_test):
            left,right=0,len(str_test)-1
            while left<right and str_test[left]==' ':
                  left+=1
            while left<right and str_test[right]==' ':
                  right-=1
            q,temp_word=collections.deque(),[]
            while left<right:
                  if str_test[left]=' ' and word:
                     q.appendleft(''.join(word))
                     word=[]
                  elif str_test[left]!=' ':
                        word.append(str_test[left])
                  left+=1
            q.append(''.join(word))
            return ' '.join(result)


5. 反转字符串中的单词 III

   输入："Let's take LeetCode contest"
   输出："s'teL ekat edoCteeL tsetnoc"
   

      def get_string(str):
         return "".join([i for i in str.strip().split(' ')[::-1] if i])


6. 仅仅反转字母

   输入："Test1ng-Leet=code-Q!"
   输出："Qedo1ct-eeLg=ntse-T!"
   
   解法: isalpha()函数判断是否为字母 将字母存储在栈里 利用栈先进后出的特性完成逆序


         def get_str(test_str):
            stack,res=[char for char in test_str if char.isalpha()],[]
            for i in test_str:
               if i.isalpha():
                  res.append(stack.pop())
               else:
                  res.append(i)
            return ''.join(res)


7. 同构字符串

   输入：s = "egg", t = "add"
   输出：true
   
   解法： 依次求出每个元素所在字符串的index值 位置相同即为同构


      def is_true(str1,str2):
         return all([str1.index(str1[i])==str2.index(str2[i]) for i in len(str1)])


8. 验证回文字符串 II

   给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

   解法：设置一个lambda函数判断是否为回文。 如果遇到非回文的情况 用切片改变字符内容


         def is_true(test_str):
            cmp=lambda s:s[:]==s[::-1]
            left,right=0,len(test_str)-1
            while left<=right:
                  if test_str[left]==test_str[right]:
                     left+=1
                     right-=1
                  else:
                     return cmp(test_str[left+1,right+1])or cmp(test_str[left,right])
            return True

9. 反转字符串 II

   输入: s = "abcdefg", k = 2
   输出: "bacdfeg"
   
   解法： 遍历字符串设置步长为k 第一个k 反转 第二个k原样输出


      def get_str(test_str,k):
         res,flag=[],True
         for i in range(0,len(test_str),k):
            res.extend(test_str[i:i+k][::-1] if flag else test_str[i:i+k])
            flag=not flag
         return ''.join(res)