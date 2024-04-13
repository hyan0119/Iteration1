<template>
  <div id="legend_area">
    <div id="description">{{ description }}</div>
    <svg id="legend">
      <g v-for="item in items" :key="item.label">
        <rect :x="item.x" :y="item.y" :width="item.width" :height="item.height" :fill="item.color"></rect>
        <text :x="item.textX" :y="item.textY" fill="black">{{ item.label }}</text>
      </g>
    </svg>
  </div>
</template>

<script>
export default {
  props: {
    items: { type: Array, required: true },
    description: { type: String, default: '' }
  }
}
</script>
