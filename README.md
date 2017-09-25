## cnvd spider
爬取 cnvd 工控信息

## require
基于 python 3

额外需要： ChormeDriver (应对 cnvd 的 cookie 限制策略)

## 使用
打开终端，输入
```
python app.py -p <number> 
```

number 表示需要爬取最近的多少页（一页 20 条信息），不写默认爬取 60 页，1200 条工控漏洞信息。

最终结果保存在 result 目录下的表格文件中。