# Python
使用Python爬虫对sduoj和sdu官网进行爬取数据处理
本项目共分为3部分
3.1
1. 爬取 OJ 中的公开题目并保存，至少包含题目名称、题目 ID、通过数信息
2. 爬取 OJ 中的公开提交并保存，并分析出提交次数前 10、AC 次数前十的题目
• 爬取最近 2K 条即可，别干扰 OJ 正常使用1. 爬取 OJ 中的公开题目并保存，至少包含题目名称、题目 ID、通过数信息
2. 爬取 OJ 中的公开提交并保存，并分析出提交次数前 10、AC 次数前十的题目
• 爬取最近 2K 条即可，别干扰 OJ 正常使用
其中对应表格为3.1开头

3.2
1. 爬取 OJ 用户组中所有比赛中的所有题目并保存，至少应包含题目名称、题目 ID 信息
2. 在第一点的基础上，分析出自己未 AC 的题目
3. 爬取 OJ 用户组中最近 2K 条提交并保存
4. 在上述的基础上，分析某同学的提交数据，例如总提交数、AC 题目数等
3.2的文件为cookie文件

3.3
1. 爬取本科生院网站中的工作通知：工作通知，至少包含通知对应的 URL、通知标题、当前
爬取的时间
2. 对工作通知网页进行截图保存 PDF
3. 自动对每一个通知网页进行截图，并保存网页的 PDF 版本，命名应具有通知标题和爬取
到的时间点
3.3的文件为3.3开头，储存的PDF放在截屏这一文件下
