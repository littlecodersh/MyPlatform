##准备工作
* **实名**认证过的[SAE账号](http://sae.sina.com.cn/)（实名认证需要一些时间，虽然运气好的话几小时就好）
* 微信公众平台个人账号（其他类型其实也可以啦）
* 图灵机器人API Key，[图灵官网](http://tuling123.com/)获取（如果没有也没关系，空着就好，只影响自动回复）
* 确保命令行能够运行`python`及`git`。（python版本为2.7）

本项目需要配置三样东西，按照顺序先后为：新浪SAE，微信公众平台，本地文件

##新浪SAE

再次提醒，配置该项目需要SAE[**实名认证**](http://www.sinacloud.com/ucenter/realshow.html)。

下面假设你已经拥有了一个实名认证的SAE账号并完成了登陆。

首先，我们需要创建一个应用（这一步在[控制台](http://sae.sina.com.cn/)操作即可）

创建一个应用

![创建应用](http://7xrip4.com1.z0.glb.clouddn.com/MyPlatform%2F%E5%88%9B%E5%BB%BA%E5%BA%94%E7%94%A8.png)

配置应用，自定义域名并选择Python 2.7作为运行环境

![配置应用](http://7xrip4.com1.z0.glb.clouddn.com/MyPlatform%2F%E9%85%8D%E7%BD%AE%E5%BA%94%E7%94%A8.png)

选择Git作为代码同步工具

![选择Git](http://7xrip4.com1.z0.glb.clouddn.com/MyPlatform%2F%E9%80%89%E6%8B%A9Git.png)

完成配置后获得仓库地址

![获得仓库地址](http://7xrip4.com1.z0.glb.clouddn.com/MyPlatform%2F%E8%8E%B7%E5%BE%97%E4%BB%93%E5%BA%93%E5%9C%B0%E5%9D%80.png)

将该仓库`git clone`到本地，按要求输入SAE用户名及安全密码（注意不是登录密码），你会得到一个目录（后文称项目目录）

```bash
git clone 仓库地址（换成自己的仓库地址）
```

到了这一步，新浪SAE的配置就完成了。

##微信公众平台

登陆并进入微信公众平台[后台](http://mp.weixin.qq.com)

进入开发者基本配置

![进入开发者基本配置](http://7xrip4.com1.z0.glb.clouddn.com/MyPlatform%2F%E8%BF%9B%E5%85%A5%E5%BC%80%E5%8F%91%E8%80%85%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE.png)

获取AppId(应用ID)和AppSecret(应用密匙)，这两项之后会用到，建议拿记事本记一下。

之后点击服务器配置右边的修改配置，将URL，Token，EncodingAESKey填写完成并选择明文模式（不要点提交）

Token可以随意填写，只要满足要求（之后会用到，记一下）。EncodingAESKey随机生成即可。URL即SAE应用域名地址，可以在[SAE控制台](http://sae.sina.com.cn)点进应用后找到。

![域名地址](http://7xrip4.com1.z0.glb.clouddn.com/MyPlatform%2F%E5%9F%9F%E5%90%8D%E5%9C%B0%E5%9D%80.png)

将网页放着不要关闭即可，不用点击提交。

到了这一步，微信公众平台基本就完成了配置。（还剩下确认要等本地文件完成后再做）

##本地文件

你首先需要把本项目下载到本地，你可以选择[下载压缩包](https://github.com/littlecodersh/MyPlatform/archive/master.zip)或者通过命令安装：

```bash
git clone https://github.com/littlecodersh/MyPlatform.git
```

把下载下来的东西（如果是压缩包则解压缩好）拖到项目目录（上文提到过）中，项目目录中应基本（我会更新）如下所示：

![项目目录](http://7xrip4.com1.z0.glb.clouddn.com/MyPlatform%2F%E9%A1%B9%E7%9B%AE%E7%9B%AE%E5%BD%95.png)

运行项目目录中的`update.py`（其实双击运行也可以），选择update config，根据提示输入内容
* TOKEN即微信公众平台一节中提到的Token
* APP_ID与SECRET_KEY对应微信公众平台一节中提到的AppId与AppSecret
* TULING_KEY对应文首提到的Tuling key

下面我们把需要展示的文章进行设置（之后的设置方法也是这样）

进入articles文件夹，按照栏目名创建txt文件，默认即两个栏目：测试、工具集

每个txt文件中放置微信文章的网址（装一个PC微信，手机将文章发给文件传输助手，复制链接地址即可），这个地址其实可以做一些删减，浏览器能浏览即可

![获取微信文章网址](http://7xrip4.com1.z0.glb.clouddn.com/MyPlatform%2F%E8%8E%B7%E5%8F%96%E5%BE%AE%E4%BF%A1%E6%96%87%E7%AB%A0%E7%BD%91%E5%9D%80.png)

txt文件中靠下的网址将靠上展示（为了方便每次更新网址）

之后运行`update.py`，选择update articles，如果没有出现`Articles update succeeded`则修改显示出的网址

```bash
python update.py
```

然后将项目上传即可，还是运行`update.py`，选择upload to server，在弹出的窗口中按照提示输入账号、安全密码（不是登录密码）即可上传成功。

至此，我们的本地文件已经全部配置完成了。

##开启后台

我们将微信公众平台一节中没有点的提交点掉（如果失败请检查你的`config.py`使用记事本打开后内容是否正确，是否能访问上文提到过的SAE应用地址）

如果失败且无法修复，可以尝试邮件联系我，联系方式可以在我的[主页](https://github.com/littlecodersh)找到。

点击服务器配置右边的启用，你的微信平台就可以使用了！

尝试回复你的微信平台“帮助”试试看呀。
