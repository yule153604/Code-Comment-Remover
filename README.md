# Code Language Detector & Comment Remover

这是一个基于Flask的Web应用程序，能够自动检测代码语言并移除代码中的注释。

## 功能特性

- 🔍 **自动语言检测**: 使用Pygments库智能识别代码语言
- 🗑️ **注释移除**: 自动移除各种编程语言的注释
- 🎨 **友好界面**: 现代化的Web界面，支持双栏显示
- ⚡ **实时处理**: 即时处理代码并显示结果
- 📊 **置信度显示**: 显示语言检测的置信度
- 💬 **智能反馈**: 通过Flash消息提供操作反馈

## 支持的语言

支持Pygments库识别的所有编程语言，包括但不限于：
- Python
- JavaScript
- Java
- C/C++
- C#
- HTML/CSS
- SQL
- Shell脚本
- 以及数百种其他语言

## 安装要求

- Python 3.x
- Flask
- Pygments

## 安装步骤

1. 克隆或下载项目文件
```bash
git clone <repository-url>
cd cancel__
```

2. 安装依赖包
```bash
pip install Flask Pygments
```

3. 运行应用程序
```bash
python app.py
```

4. 在浏览器中访问 `http://127.0.0.1:5000`

## 使用方法

1. 在左侧文本框中粘贴您的代码
2. 点击"Detect Language and Remove Comments"按钮
3. 系统会自动检测代码语言并显示置信度
4. 右侧文本框将显示移除注释后的代码

## 项目结构

```
cancel__/
├── app.py              # 主应用程序文件
├── templates/
│   └── index.html      # Web界面模板
└── README.md           # 项目说明文档
```

## 核心功能说明

### 语言检测
- 使用Pygments的`guess_lexer()`函数自动检测代码语言
- 显示检测置信度以帮助用户了解检测准确性
- 对于无法识别的代码，会返回原始代码并提示

### 注释移除
- 使用Pygments tokenizer分析代码结构
- 识别并移除各种类型的注释（单行、多行等）
- 保持代码的原始格式和缩进

### 错误处理
- 优雅处理Pygments库缺失的情况
- 处理空输入和无效代码
- 提供详细的错误信息和建议

## 注意事项

- 语言检测对于很短的代码片段可能不够准确
- 建议提供较大或更清晰的代码片段以获得更好的检测结果
- 如果无法安装Pygments库，应用程序会显示错误信息但仍可访问

## 技术栈

- **后端**: Flask (Python Web框架)
- **语言检测**: Pygments库
- **前端**: HTML5, CSS3
- **模板引擎**: Jinja2

## 开发者信息

该应用程序设计为教育和开发辅助工具，帮助开发者快速清理代码注释或分析代码结构。

## 许可证

本项目遵循开源许可证，可自由使用和修改。

## 故障排除

### 常见问题

1. **Pygments未安装**
   ```bash
   pip install Pygments
   ```

2. **Flask未安装**
   ```bash
   pip install Flask
   ```

3. **端口被占用**
   - 检查5000端口是否被其他应用占用
   - 可以在`app.py`中修改端口号

### 开发模式

应用程序默认运行在调试模式下，便于开发和测试。生产环境使用时请关闭调试模式：

```python
app.run(debug=False)
```

## 贡献

欢迎提交问题报告和功能建议！
