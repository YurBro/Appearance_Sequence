# Example Package
#在此文件内，可使用markdown撰写对包的详细介绍和说明，便于别人熟悉和使用，在此不再赘述
This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

外观数列

给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

 - countAndSay(1) = "1"
 - countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

前五项如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/5b28795d47674f4ca78d51aafa31dbd6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bqc5a2m6LevMTjlj7fovabnpZ4=,size_20,color_FFFFFF,t_70,g_se,x_16)
要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。

例如，数字字符串 "3322251" 的描述如下图：

![在这里插入图片描述](https://img-blog.csdnimg.cn/b62ad5a7bbc04db0b7f4f57fcd830db8.png)
**示例1**：

> **输入**：n = 1
**输出**："1"
**解释**：这是一个基本样例。

**示例2**：

> **输入**：n = 4
**输出**："1211"
**解释**：
countAndSay(1) = "1"
countAndSay(2) = 读 "1" = 一 个 1 = "11"
countAndSay(3) = 读 "11" = 二 个 1 = "21"
countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"

**提示**：

 - 1 <= n <= 30