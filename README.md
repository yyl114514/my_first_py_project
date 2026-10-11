# mall 接口与 UI 自动化测试

这是一个基于 `pytest`、`requests` 和 `Selenium` 的自动化测试练习项目。

被测对象是开源电商项目 [mall](https://github.com/macrozheng/mall) 的后台管理系统 `mall-admin` 和后台前端 `mall-admin-web`。本仓库只包含测试代码，不包含 mall 项目本身的业务代码。

项目当前包含 9 条自动化用例：

- 5 条后台用户管理接口测试
- 3 条商品品牌管理接口测试
- 1 条后台登录 UI 冒烟测试

## 功能特性

- 使用 `requests.Session` 保存登录状态和 JWT Token
- 使用 session 级 fixture 完成一次登录，供多条接口测试复用
- 使用 fixture 创建测试数据，并在用例结束后自动清理
- 将接口封装与测试用例分离，便于维护和复用
- 使用 Selenium Page Object 模式编写 UI 测试
- 使用 pytest marker 对测试模块进行分类
- 集成 Allure，支持生成可视化测试报告
- 通过 `.gitignore` 排除虚拟环境、缓存和测试报告等生成文件

## 技术栈

| 类别 | 技术 |
| --- | --- |
| 编程语言 | Python |
| 测试框架 | pytest |
| 接口测试 | requests |
| UI 自动化 | Selenium |
| UI 设计模式 | Page Object |
| 测试报告 | Allure |
| 测试数据 | MySQL、Navicat |
| 被测系统 | Spring Boot、MyBatis、Redis、Vue、Vite |

## 环境要求

运行测试前需要准备以下环境：

- Python 3.10 或更高版本
- Google Chrome
- MySQL
- Redis
- JDK
- Maven 或已构建好的 `mall-admin` 可执行 JAR
- Node.js 和 Vite
- Allure Commandline，用于本地打开 Allure 报告

需要提前启动的被测服务：

| 服务 | 地址 |
| --- | --- |
| mall 后台接口 | `http://localhost:8080` |
| mall 后台前端 | `http://localhost:5173` |

如果被测系统尚未启动，请先运行 `mall` 项目提供的启动脚本，确认 MySQL、Redis、后端和前端均正常启动。

## 安装项目

进入本测试项目目录：

```powershell
cd E:\my_first_py_project
```

创建并激活虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

安装依赖：

```powershell
pip install -r requirements.txt
```

如果 PowerShell 禁止执行激活脚本，可以不激活虚拟环境，直接使用虚拟环境中的 Python：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 测试配置

测试地址和账号配置位于 `config.py`：

```python
BASE_URL = "http://localhost:8080"
USERNAME = "admin"
PASSWORD = "macro123"

login_page_url = "http://localhost:5173/"
home_page_url = "http://localhost:5173/#/home"
```

如果本地环境或测试账号不同，请修改该文件。不要将真实生产环境账号、密码或 Token 提交到 Git 仓库。

## 运行测试

运行全部测试：

```powershell
pytest -q
```

也可以使用虚拟环境中的 Python：

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

只运行品牌管理接口测试：

```powershell
pytest -m brand -q
```

只运行后台用户管理接口测试：

```powershell
pytest -m admin -q
```

只运行后台登录 UI 测试：

```powershell
pytest -m web -q
```

同时运行品牌和后台用户接口测试：

```powershell
pytest -m "brand or admin" -q
```

## 生成测试报告

pytest 会将 Allure 原始数据输出到：

```text
reports/allure_temp
```

生成 HTML 报告：

```powershell
allure generate reports/allure_temp -o reports/allure_report --clean
```

打开报告：

```powershell
allure open reports/allure_report
```

`reports/` 是测试执行后生成的目录，已加入 `.gitignore`，不需要提交到 Git。

## 项目结构

```text
my_first_py_project/
├── api/
│   ├── admin_user_api.py      # 后台用户管理接口封装
│   ├── brand_api.py           # 品牌管理接口封装
│   └── login_api.py           # 登录会话创建
├── tests/
│   ├── conftest.py            # 全局 api_session fixture
│   ├── admin_user/            # 后台用户管理接口测试
│   ├── brand/                 # 商品品牌管理接口测试
│   └── ui/
│       ├── conftest.py        # Selenium driver fixture
│       ├── pages/
│       │   └── login_page.py  # 登录页面 Page Object
│       └── test_admin_login.py
├── config.py                  # 测试地址和账号配置
├── pytest.ini                 # pytest 配置和 marker 定义
├── requirements.txt           # 项目依赖
└── README.md
```

## 测试覆盖范围

### 后台用户管理

- 用户注册
- 查询登录用户信息
- 用户列表查询和用户信息查询
- 用户信息修改
- 用户删除

### 商品品牌管理

- 品牌创建
- 品牌修改
- 品牌删除

### UI 冒烟测试

- 打开 mall 后台登录页
- 输入用户名和密码
- 点击登录
- 校验登录后跳转到首页

## 测试设计说明

接口测试通过 `api_session` fixture 复用登录后的 Session，避免每条用例重复登录。

涉及数据修改的用例通过 fixture 创建临时数据，并使用 `yield` 配合 `finally` 在测试结束后清理数据，减少测试之间的数据污染。

UI 测试使用 Page Object 管理页面元素和操作，当前只覆盖登录冒烟场景。后续可以继续增加品牌管理和后台用户管理的 UI 用例。

## 已知限制

- 测试依赖本地运行的 mall 后端、前端、MySQL 和 Redis
- 测试数据依赖真实数据库，暂时没有使用独立测试数据库
- UI 测试目前只覆盖登录流程
- 测试账号配置在 `config.py` 中，后续可以通过环境变量管理
- 当前尚未接入持续集成，例如 GitHub Actions

## 后续计划

- 增加接口异常参数、权限和边界场景测试
- 使用 pytest 参数化减少重复代码
- 增加品牌和后台用户管理 UI 测试
- 将测试配置改为环境变量
- 接入 GitHub Actions，实现自动执行测试
