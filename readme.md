Django 博客项目
1. 基础架构 (MVT 模式)

Model (模型)：在 models.py 中定义了 BlogPost 类，包含标题 (title)、正文 (text)、添加日期 (date_added)。

私有性增强：通过外键 owner 将每一篇博文与 Django 内置的 User 模型关联，实现“谁发布谁拥有”的逻辑。

Migration (迁移)：通过 makemigrations 和 migrate 命令，将 Python 代码定义的模型结构同步到了 SQLite 数据库中。

2. 业务逻辑 (Views & URLs)

index: 首页视图，获取所有博文并按时间顺序排列展示。

new_post: 处理新博文的发布。使用了 @login_required 装饰器，确保只有登录用户能发帖。

edit_post：编辑视图。在修改内容前，代码会强制检查 post.owner == request.user。如果当前用户不是作者，系统将拒绝访问（返回 404），有效保护了数据安全。

3. 用户认证系统 (Auth)

用户登录/登出：利用 Django 内置的认证视图实现。根据 Django 6.0 的安全要求，登出功能采用了 POST 表单形式以防止 CSRF 攻击。

用户注册：在 views.py 中自定义了 register 函数，使用 UserCreationForm 允许新访客创建账号。

登录重定向：在 settings.py 中配置了跳转逻辑，确保用户在登录或登出后能自动返回首页。

4. 前端展示 (Templates)

模板继承：创建了 base.html 作为公共框架，所有页面（index, login, register等）都继承自它，保证了导航栏的一致性。

UI 美化：引入了 Bootstrap 5 框架，通过导航条 (Navbar)、卡片布局 (Cards) 和响应式容器 (Container) 提升了页面的视觉体验，解决了原始 HTML 过于简陋的问题。