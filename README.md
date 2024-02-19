# 在线考试系统
这个项目已经拖延了好几年了，2024年要重新开始动工，有需要这个项目做参考的同学，可以加我微信:MintBlueD，留言：GitHub  

到时候我会拉一个群，大家来说说，前端想用Vue、React还是Angular😏，截止在24年2月底哦～

---

功能模块有4大模块：`用户管理模块`、`试题管理模块`、`试卷管理模块`和`考试管理模块`

系统角色有3类：系统管理员、学生用户和教师用户

### 功能点  
#### 用户管理模块

+ [x] 用户登录
  - [x] 登录接口  
  - [x] 登录JWT
 + [x] 用户信息管理  
   - [x] 学生信息管理
     - [x] 学生信息新增接口
     - [x] 学生信息编辑接口
     - [x] 学生信息删除接口
     - [x] 学生信息查询接口（List）
     - [x] 学生信息查询接口（Detail）
   - [x] 教师信息管理
     - [x] 教师信息新增接口
     - [x] 教师信息编辑接口
     - [x] 教师信息删除接口
     - [x] 教师信息查询接口（List）
     - [x] 教师信息查询接口（Detail）
 + [x] 用户激活   
   - [x] 学生用户批量激活
 + [x] 修改密码
   - [x] 修改学生密码接口
   - [x]   修改教师（管理员）密码接口
 + [ ] 用户消息  
 + [ ] 日志管理  

####  试题管理模块

 + [x] 试题管理
   + [x] 试题新增接口
   + [x] 试题修改接口
   + [x] 试题删除接口
   + [x] 试题查询接口（List）
   + [x] 试题查询接口（Detail）
 + [x] 试题收藏&查询（面向教师用户）
   + [x] 试题收藏接口
   + [x] 试题取消收藏接口
   + [x] 根据用户ID获取所有收藏试题接口

 + [x] 错题查询及筛选（面向学生用户）
   - [x] 错题收藏接口
   - [x] 错题取消收藏接口
   - [x] 编辑错题收藏信息
   - [x] 根据用户ID获取错题收藏信息接口  

####  试卷管理模块

+ [x] 试卷管理
   + [x] 试卷信息新增接口
   + [x] 试卷信息修改接口
   + [x] 试卷信息删除接口（逻辑删除）
   + [x] 试卷信息查询接口
     - [x] 列表信息（查询条件）
+ [x] 试卷 - 模块管理
  - [x] 新增试卷-模块信息接口
  - [x] 编辑试卷-模块信息接口
  - [x] 删除试卷-模块信息接口（物理删除）
  - [x] 根据试卷ID获取模块信息接口
+ [ ] 试卷 - 试题管理
  - [x] 新增试卷-试题信息接口
  - [x] 编辑试卷-试题信息接口（修改分数、排序、所属模块）
  - [x] 删除（解绑）试卷-试题信息接口（物理删除）
  - [ ] 根据试卷ID获取试题信息接口
+ [ ] 复制试卷接口（包含试卷信息、模块信息以及绑定的试题）


####  考试管理模块

 + [ ] 新增考试  
 + [ ] 试卷答题（面向学生用户）  
 + [ ] 考试成绩查询  
 + [ ] 考试成绩下载  

#### 技术栈
服务端：Python 3.8 + Django 4.3.8

数据库：MySQL 8.2

#### MySQL安装
我是用Docker安装的MySQL，更加方便一些，下面👇是下载&启动命令：  
##### 下载

```
docker pull mysql:8.2
```

##### 启动容器  

```
docker run -p 3306:3307 --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:8.2
```


---
    PS：内容暂定，待完善。。。

#### 关于 Django ORM 的一些知识

##### 模糊查询操作符

1. `__icontains`: 包含某个字符串（不区分大小写）的值。
2. `__contains`: 包含某个字符串（区分大小写）的值。
3. `__iexact`: 等于某个字符串（不区分大小写）的值。
4. `__exact`: 等于某个字符串（区分大小写）的值。
5. `__startswith`: 以某个字符串开头的值。
6. `__endswith`: 以某个字符串结尾的值。

例子：

```python
queryset = Paper.objects.filter(title__icontains='大三')
```

