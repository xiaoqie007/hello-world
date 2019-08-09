**requests**

然而在通常情况下，你应该以下面的模式将文本流保存到文件中：


```python
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

```

自定义请求头

然而在通常情况下，你应该以下面的模式将文本流保存到文件中：
```python
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

```

Response.iter_content 将会帮你处理大量由于直接使用 Response.raw 而不得不处理的内容。 当使用流下载时，我们推荐使用上面代码来获取内容。注意，请根据你的实际情况设置 chunk_size 的值。


自定义请求头
```python
>>> url = 'https://api.github.com/some/endpoint'
>>> import requests
>>> headers = {'user-agent': 'my-app/0.0.1'}
>>> r = requests.get(url, headers= headers)
>>> r
<Response [404]>
>>> 
```

定制 header 的优先级低于某些特定的信息源，例如：

- 如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。而如果设置了 auth= 参数，.netrc 的设置就无效了。
- 如果被重定向到别的主机，header 的授权就会被删除。
- header 代理授权会被 URL 中提供的代理身份覆盖掉。
- 在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。

此外，Requests 不会基于自定义 header 而改变自己的行为。只不过在最后的请求中，所有的 header 信息都会被传递进去。

注意：所有的 header 值必须是 string、bytestring 或者 unicode。尽管传递 unicode header 也是允许的，但我们不建议你这样做。


**更复杂的 POST 请求**

- **响应头**

```python
>>> r.raise_for_status()
>>> r
<Response [200]>
>>> r.headers
{'Access-Control-Allow-Credentials': 'true', 'Access-Control-Allow-Origin': '*', 'Content-Encoding': 'gzip', 'Content-Type': 'application/json', 'Date': 'Fri, 09 Aug 2019 05:26:16 GMT', 'Referrer-Policy': 'no-referrer-when-downgrade', 'Server': 'nginx', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'DENY', 'X-XSS-Protection': '1; mode=block', 'Content-Length': '185', 'Connection': 'keep-alive'}
>>> r.headers['Content-Type']
'application/json'
>>> r.headers.get('content-type')
'application/json'

```
> 接收者可以合并多个相同名称的 header 栏目，把它们合为一个“field-name: field-value”的键值对，将每个后续的栏目值依次追加到合并的栏目值中，并使用逗号隔开，这样做就不会改变信息的语义。


Cookies

```python
>>> url = 'http://httpbin.org/cookies'
>>> cookies = dict(cookies_are='zhaozhao')
>>> r = requests.get(url, cookies= cookies)
>>> r.text
'{\n  "cookies": {\n    "cookies_are": "zhaozhao"\n  }\n}\n'
>>> print(r)
<Response [200]>
>>> print(r.text)
{
  "cookies": {
    "cookies_are": "zhaozhao"
  }
}


>>> jar = requests.cookies.RequestsCookieJar()

>>> jar.set('tasty_cookie', 'yum', domain= 'httpbin.org', path= '/cookies')
Cookie(version=0, name='tasty_cookie', value='yum', port=None, port_specified=False, domain='httpbin.org', domain_specified=True, domain_initial_dot=False, path='/cookies', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)

>>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
Cookie(version=0, name='gross_cookie', value='blech', port=None, port_specified=False, domain='httpbin.org', domain_specified=True, domain_initial_dot=False, path='/elsewhere', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)

>>> url = 'http://httpbin.org/cookies'
>>> r = requests.get(url, cookies=jar)
>>> r.text
'{\n  "cookies": {\n    "tasty_cookie": "yum"\n  }\n}\n'
>>> print(r.text)
{
  "cookies": {
    "tasty_cookie": "yum"
  }
}

>>> 
```

重定向和历史

默认情况下除了 HEAD，Requests 会自动处理所有重定向。

可以使用响应对象的 history 属性来追踪重定向。

**Response.history** 是一个 Response 对象的列表，这些对象是为了完成请求而创建的。这个对象列表是按照从旧到新的请求进行排序。

```python
>>> r = requests.get('http://github.com')
>>> r.url
'https://github.com/'
>>> r.status_code
200
>>> r.history
[<Response [301]>]
>>> r = requests.get('http://github.com', allow_redirects = False)
>>> r.status_code
301
>>> r.history
[]
>>> r = requests.get('http://github.com', allow_redirects = True)
>>> r.url
'https://github.com/'
>>> r.history
[<Response [301]>]
>>> 
```

-**超时**

你可以告诉 Requests 在经过以 timeout 参数设定的秒数后停止等待响应，基本上所有的生产代码都应该使用这一参数，否则你的程序可能会永远地卡在那里：

**注意：**

- timeout 仅对连接过程有效，与响应体的下载时间无关。因为 timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时）。如果没有明确填写 timeout 的时间，那么 requests 默认是没有超时限制的。


**错误与异常**

**遇到网络问题**（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 **ConnectionError** 异常。

**如果 HTTP 请求返回了不成功的状态码**， Response.raise_for_status() 会抛出一个 **HTTPError** 异常。

**若请求超时**，则抛出一个 **Timeout** 异常。

若请求**超过了设定的最大重定向次数**，则会抛出一个 **TooManyRedirects** 异常。

所有 Requests 显式抛出的异常都继承自 **requests.exceptions.RequestException。**