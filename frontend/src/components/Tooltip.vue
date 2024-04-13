<template>
  <div id="tooltip" v-show="visible">{{ content }}</div>
</template>

<script>
export default {
  props: {
    content: { type: String, default: '' },
    visible: { type: Boolean, default: false }
  }
}
</script>
