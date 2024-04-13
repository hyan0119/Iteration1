<template>
  <el-header class="header">
    <div class="menu-container">
      <el-menu :mode="mode" class="menu left-menu" :background-color="backgroundColor">
        <!-- 动态生成菜单项 -->
        <el-menu-item v-for="item in menuItems" :key="item.index" :index="item.index" class="menu-item">
          <router-link :to="item.path">{{ item.label }}</router-link>
        </el-menu-item>
      </el-menu>
    </div>
  </el-header>
</template>

<script>
export default {
  name: 'HeaderNavigation',
  props: {
    mode: { type: String, default: 'horizontal' },
    backgroundColor: { type: String, default: 'transparent' },
    menuItems: { type: Array, required: true }
  }
}
</script>
