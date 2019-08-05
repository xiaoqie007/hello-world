Requests是以**PEP20（Python之婵）**为指导思想开发的：
1. Beautifull is better than ugly.(美丽优于丑陋)
2. Explicit is better than implicit(直白优于含蓄)
3. Simple is better than complex(简单优于复杂)
4. Complex is better than complicated(复杂优于繁杂)
5. Readability counts.(可读性很重要)


Apache2 协议

现在你找到的许多开源项目都是以 GPL 协议发布的。虽然 GPL 有它自己的一席之地，但我们不建议使用这个协议。因为一旦项目发行于 GPL 协议之后，就不能应用于任何本身没开源的商业产品中。

MIT、BSD、ISC、Apache2 协议都是优秀的替代品，它们允许你的开源软件自由地应用在私有闭源的软件中。

因此，Requests 的发布协议为 Apache2 License。


传递 URL 参数 (**params**)

```python
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('http://httpbin.org/get', params = payload)
>>> print(r)
<Response [200]>
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2
>>> payload = {'key1': 'value1', 'key2': ['value2', 'values3']}
>>> r = requests.get('http://httpbin.org/get', params = payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=values3
>>> 
```

