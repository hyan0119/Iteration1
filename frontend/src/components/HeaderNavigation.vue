<template>
  <el-header class="header">
    <div class="menu-container">
      <div class="logo_container" @click="goHome">
            <img src="@/assets/logo.png" alt="Logo" class="logo"/>
            <div class="logo_text">
              <div>COOLDOWN</div>
              <div>MELBOURNE</div>
            </div>
          </div>
      <!-- <el-menu mode="horizontal" class="menu left-menu" background-color="transparent">
        <el-menu-item index="1" class="menu-item home">
          <router-link to="/">Home</router-link>
        </el-menu-item>
      </el-menu> -->

      <el-menu class="menu right-menu" background-color="transparent">
        <el-menu-item index="0" :class="['menu-item',activeIndex =='0'?'activeItem':'']">
          <router-link to="/">Home</router-link>
        </el-menu-item>
        <el-menu-item index="1" :class="['menu-item',activeIndex =='1'?'activeItem':'']">
          <router-link to="/uhi-map">UHI MAP</router-link>
        </el-menu-item>
        <el-menu-item index="2" :class="['menu-item',activeIndex =='2'?'activeItem':'']">
          <router-link to="/plant-planner">PLANT PLANNER</router-link>
        </el-menu-item>
        <el-menu-item index="3" :class="['menu-item',activeIndex =='3'?'activeItem':'']">
          <router-link to="/my-plants">COOL CITY</router-link>
        </el-menu-item>
        <el-menu-item index="4" :class="['menu-item',activeIndex =='4'?'activeItem':'']">
          <router-link to="/info-page">INFO</router-link>
        </el-menu-item>
      </el-menu>
    </div>
  </el-header>
</template>

<script>
export default {
  name: 'HeaderNavigation',
  data(){
    return{
      activeIndex:'0'
    }
  },
  watch:{
    $route:{
      handler(to,form){
        // console.log(to,"to")
        if(to.path == '/') {
          this.activeIndex = '0'
        } else if(to.path == '/uhi-map'){
          this.activeIndex = '1'
        } else if(to.path == '/plant-planner'){
          this.activeIndex = '2'
        } else if(to.path == '/my-plants'){
          this.activeIndex = '3'
        } else if(to.path == '/info-page'){
          this.activeIndex = '4'
        }
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    goHome(){
      this.$router.push("/")
    }
  },
}
</script>

<style scoped>
.logo_container{
  display: flex;
  cursor: pointer;
}
.logo_text{
  font-family: 'Fredoka One', cursive;

  font-size: 16px;
  font-weight: 700;
  line-height: 28px;
  text-align: left;
  color: #fff;
  margin-left: 20px;
  }
  .activeItem{
    background: #09A03D;
    border-radius: 25px;
  
  }
  .activeItem a{
    font-weight: 600!important;
  }
</style>
