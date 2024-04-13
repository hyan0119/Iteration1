<template>
  <el-footer class="footer">
    <div class="footer-top">
      <div class="footer-section" v-for="section in footerSections" :key="section.title">
        <h2>{{ section.title }}</h2>
        <div v-html="section.content"></div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>{{ copyright }}</p>
    </div>
  </el-footer>
</template>

<script>
export default {
  name: 'FooterComponent',
  props: {
    footerSections: { type: Array, required: true },
    copyright: { type: String, default: '© Copyright All Rights Reserved' }
  }
}
</script>
