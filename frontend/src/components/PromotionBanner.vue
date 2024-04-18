<template>
  <div id="promotion-container">
    <div id="promotion">{{ text }}</div>
  </div>
</template>

<script>
export default {
  props: {
    text: { type: String, required: true }
  }
}
</script>
