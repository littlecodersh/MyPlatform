#coding=utf8

TOKEN = ''
APP_ID = ''
SECRET_KEY = ''
TULING_KEY = ''
ADMIN_OAUTH = 'admin_oauth'
MENU = {
    "button":[{	
        "type":"click",
        "name":u"百度",
        "key":"This is baidu"
        },{
        "name":u"菜单",
            "sub_button":[{	
                "type":"view",
                "name":u"搜索",
                "url":"http://www.soso.com/"
            },{
                "type":"view",
                "name":u"视频",
                "url":"http://v.qq.com/"
            },{
                "type":"click",
                "name":u"赞一下我们",
                "key":"V1001_GOOD"
            }]
        }
    ]
}
