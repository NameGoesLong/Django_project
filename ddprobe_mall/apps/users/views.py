from django.http import JsonResponse

"""
需求分析： 根据页面的功能（从上到下，从左到右），哪些功能需要和后端配合完成
如何确定 哪些功能需要和后端进行交互呢？？？
        1.经验
        2.关注类似网址的相似功能

"""

"""
判断用户名是否重复的功能。

前端(了解)：     当用户输入用户名之后，失去焦点， 发送一个axios(ajax)请求

后端（思路）：
    请求:         接收用户名 
    业务逻辑：     
                    根据用户名查询数据库，如果查询结果数量等于0，说明没有注册
                    如果查询结果数量等于1，说明有注册
    响应          JSON 
                {code:0,count:0/1,errmsg:ok}
    
    路由      GET         usernames/<username>/count/        
   步骤：
        1.  接收用户名
        2.  根据用户名查询数据库
        3.  返回响应         
    
"""

from django.shortcuts import render
from django.views import View

from apps.users.models import User

# Getting the data from HTTP request => need urls.py to unpack the request
class UsernameCountView(View):
    def get(self,request,username):
        """
         1.根据用户名查询数量
         2.返回个数信息
        """
        # 2.  根据用户名查询数据库
        count=User.objects.filter(username=username).count()
        # 3.  返回响应
        return JsonResponse({'code':0,'count':count,'errmsg':'ok'})
    
class RegisterMobileCountView(View):

    def get(self,request,mobile):
        """
         1.根据用户名查询数量
         2.返回个数信息
        """
        # TODO finish this
        pass
