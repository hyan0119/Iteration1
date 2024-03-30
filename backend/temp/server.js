// 导入 Express 框架
const express = require('express');
const cors = require('cors');
// 创建 Express 应用程序
const app = express();
app.use(cors())
// 定义一个简单的路由
app.get('/api/data', (req, res) => {
  // 返回 JSON 格式的数据
  res.json({ "message": 'Hello from the backend!' });
});

// 启动服务器，监听端口 3000
app.listen(8000, () => {
  console.log('Server is running on port 8000');
});
