# Code Language Detector & Comment Remover

一个基于 Flask 的 Web 应用程序，能够自动检测代码语言并移除代码中的注释。支持数百种编程语言，提供简洁直观的 Web 界面。

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Pygments](https://img.shields.io/badge/Pygments-Syntax%20Highlighter-green.svg)](https://pygments.org/)

## ✨ 功能特性

- 🔍 **智能语言检测**: 基于 Pygments 库自动识别代码语言
- 🗑️ **精确注释移除**: 支持单行注释、多行注释等各种注释格式
- 🎨 **现代化界面**: 响应式双栏设计，支持移动端访问
- ⚡ **实时处理**: 即时分析代码并显示处理结果
- 📊 **置信度显示**: 显示语言检测的准确度评分
- 💬 **智能反馈**: 通过 Flash 消息提供详细的操作反馈
- 🛡️ **错误处理**: 优雅处理各种异常情况

## 🌍 支持的语言

支持 Pygments 库识别的 500+ 编程语言，包括：

### 主流语言
- **Python** - `.py`
- **JavaScript** - `.js`, `.jsx`
- **Java** - `.java`
- **C/C++** - `.c`, `.cpp`, `.h`
- **C#** - `.cs`

### Web 技术
- **HTML/CSS** - `.html`, `.css`
- **TypeScript** - `.ts`, `.tsx`
- **PHP** - `.php`
- **Ruby** - `.rb`

### 脚本语言
- **Shell/Bash** - `.sh`, `.bash`
- **PowerShell** - `.ps1`
- **Perl** - `.pl`
- **Go** - `.go`

### 数据库
- **SQL** - `.sql`
- **PL/SQL** - `.plsql`

### 其他
- **Rust**, **Kotlin**, **Swift**, **Scala**, **R**, **MATLAB** 等数百种语言

## 🔧 环境要求

- **Python**: 3.6+
- **Flask**: 2.0+
- **Pygments**: 2.0+

## 📦 安装步骤

### 1. 克隆项目
```bash
git clone https://github.com/yule153604/Code-Comment-Remover.git
cd Code-Comment-Remover
```

### 2. 安装依赖
```bash
# 使用 pip 安装
pip install Flask Pygments

# 或者使用虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install Flask Pygments
```

### 3. 启动应用
```bash
python app.py
```

### 4. 访问应用
在浏览器中打开: `http://127.0.0.1:5000`

## 🚀 使用指南

### 基本使用
1. 在左侧文本框中粘贴您的代码
2. 点击 **"Detect Language and Remove Comments"** 按钮
3. 查看检测到的语言类型和置信度
4. 右侧显示移除注释后的代码

### 示例

**输入代码:**
```python
# 这是一个Python示例
def hello_world():
    """
    打印Hello World
    """
    print("Hello, World!")  # 输出问候语
    return True
```

**输出结果:**
```python
def hello_world():
    
    print("Hello, World!")  
    return True
```

## 📁 项目结构

```
Code-Comment-Remover/
├── app.py                  # Flask 主应用程序
├── templates/
│   └── index.html         # Web 界面模板
├── README.md              # 项目文档
└── requirements.txt       # 依赖列表 (建议添加)
```

## ⚙️ 核心功能详解

### 语言检测机制
- 使用 `pygments.lexers.guess_lexer()` 进行智能检测
- 通过 `analyse_text()` 方法计算置信度评分
- 对于模糊代码片段提供友好提示

### 注释移除算法
- 基于词法分析器 (lexer) 进行 token 解析
- 识别 `Comment` 类型的 token 并过滤
- 保持原始代码格式和缩进结构

### 错误处理策略
- **依赖检查**: 检测 Pygments 是否正确安装
- **输入验证**: 处理空输入和无效代码
- **异常捕获**: 优雅处理各种运行时错误

## 🛠️ 技术栈

| 组件 | 技术 | 用途 |
|------|------|------|
| **后端框架** | Flask | Web 服务器和路由 |
| **语言检测** | Pygments | 代码语法分析 |
| **前端样式** | CSS3 | 响应式界面设计 |
| **模板引擎** | Jinja2 | 动态 HTML 生成 |

## 🐛 故障排除

### 常见问题及解决方案

#### 1. Pygments 未安装
```bash
# 错误信息: "Pygments library not found"
pip install Pygments
```

#### 2. Flask 未安装
```bash
# 错误信息: "No module named 'flask'"
pip install Flask
```

#### 3. 端口被占用
```bash
# 错误信息: "Address already in use"
# 解决方案: 修改 app.py 中的端口
app.run(debug=True, port=5001)
```

#### 4. 语言检测不准确
- **原因**: 代码片段过短或语法不明确
- **解决**: 提供更完整的代码示例
- **示例**: 包含函数定义、导入语句等特征性语法

### 开发配置

#### 生产环境部署
```python
# 修改 app.py
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
```

#### 启用日志记录
```python
import logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')
```

## 🔒 安全注意事项

- **密钥管理**: 更改默认的 SECRET_KEY
- **输入验证**: 不要处理可执行代码
- **生产部署**: 关闭调试模式

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支: `git checkout -b feature/amazing-feature`
3. 提交更改: `git commit -m 'Add amazing feature'`
4. 推送分支: `git push origin feature/amazing-feature`
5. 提交 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 👨‍💻 作者

- **yule153604** - [GitHub Profile](https://github.com/yule153604)

## 🙏 致谢

- [Pygments](https://pygments.org/) - 强大的语法高亮库
- [Flask](https://flask.palletsprojects.com/) - 简洁的 Web 框架

---

## 📈 更新日志

### v1.0.0 (2025-06-12)
- 初始版本发布
- 支持多语言代码检测
- 实现注释移除功能
- 提供 Web 界面

---
