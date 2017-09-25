from util import *

selector = {
    'CNVD-ID': cnvd_id,
    '发布时间': release_time,
    '危害级别': harzard_level,
    '影响产品': influence_product,
    '漏洞描述': description,
    '参考链接': reference,
    '漏洞解决方案': solution,
    '漏洞发现者': discoverer,
    '厂商补丁': patch,
}

demand_list = [
    'CNVD-ID',
    '发布时间',
    '危害级别',
    '影响产品',
    '漏洞描述',
    '参考链接',
    '漏洞解决方案',
    '漏洞发现者',
    '厂商补丁',
]


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',

}
cookies = {
    'JSESSIONID': '81AAE48C645A822F7BAE59FB8828F58A',
    '__jsl_clearance': '1506217644.476|0|xIyVa%2BcEppx8ep%2F9NWWfvxR5Fgo%3D',
    '__jsluid': '713a6c8c1df5082aa6ff07627a76301d',
    'bdshare_firstime': '1505890790434',
}


