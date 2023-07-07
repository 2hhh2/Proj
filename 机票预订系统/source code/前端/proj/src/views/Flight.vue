<template>
    <body id="poster">

   <el-menu

       class="el-menu-demo"
       mode="horizontal"
       @select="handleSelect"
       background-color="#545c64"
       text-color="#fff"
       active-text-color="#ffd04b">
       <el-menu-item index="1" @click="order()">我的订单</el-menu-item>
       <el-submenu index="2">
           <template slot="title">我的工作台</template>
           <el-menu-item index="2-1" @click="perpage()">个人主页</el-menu-item>
           <el-menu-item index="2-2">我的收藏</el-menu-item>
           <el-menu-item index="2-3">浏览历史</el-menu-item>
           <el-submenu index="2-4">
               <template slot="title">我的社区</template>
               <el-menu-item index="2-4-1">好物推荐</el-menu-item>
               <el-menu-item index="2-4-2">最新动态</el-menu-item>
               <el-menu-item index="2-4-3">热点话题</el-menu-item>
           </el-submenu>
       </el-submenu>
       <el-menu-item index="3" >消息中心</el-menu-item>
       <el-menu-item index="4"><a href="">退出登录</a></el-menu-item>
   </el-menu>



   <div class="scenic">
       <h2 >热门景点推荐</h2>
       <el-carousel :interval="4000" type="card" height="400px">
           <el-carousel-item v-for="item in imgs" :key="item.id">
               <img :src="item.img" class="image" width="100%" height="100%">
           </el-carousel-item>
       </el-carousel>

   </div>


      <el-form class="flight-container" label-position="left" label-width="0px">
          <el-form-item label="">
              <el-input type="text"   v-model="flightForm.depAirport" autocomplete="off" placeholder="出发地" list="DATALIST"></el-input>
          </el-form-item>
          <datalist id="DATALIST">
              <option>北京</option>
              <option>上海</option>
              <option>武汉</option>
              <option>杭州</option>
              <option>郑州</option>
              <option>长沙</option>
              <option>深圳</option>
              <option>成都</option>
              <option>重庆</option>
              <option>天津</option>
              <option>西安</option>
          </datalist>
          <el-form-item label="">
              <el-input type="text" v-model="flightForm.arrAirport" autocomplete="off" placeholder="目的地" list="DATALIST"></el-input>
          </el-form-item>
          <datalist id="DATALIST">
              <option>北京</option>
              <option>上海</option>
              <option>武汉</option>
              <option>杭州</option>
              <option>郑州</option>
              <option>长沙</option>
              <option>深圳</option>
              <option>成都</option>
              <option>重庆</option>
              <option>西安</option>
          </datalist>

          <el-form-item label="">
              <el-col :span="11">
                  <el-date-picker type="datetime" placeholder="选择日期"  format="yyyy-MM-dd HH:mm:ss" value-format="yyyy-MM-dd HH:mm:ss"
                                  v-model="flightForm.depTime" style="width: 100%;"></el-date-picker>
              </el-col>
          </el-form-item>

          <el-form-item>
              <el-button type="primary" style="width: 100%;color: aquamarine;border: none" @click="Search()">搜索</el-button>
          </el-form-item>
      </el-form>

    </body>
</template>

<script>

export default {
  name: 'Flight',
    mounted() {
        document.querySelector('body').setAttribute('style',
            "background-image: url("+require("../assets/gugong.jpg")+");background-size: cover;" +
            "background-repeat: no-repeat")
    },
    beforeDestroy() {
        document.querySelector('body').removeAttribute('style')
    },

    data() {
        return {
            imgs: [
                {
                    id: 1, img: require("../assets/beijing.jpg")
                },
                {
                    id: 2, img: require("../assets/bendibao.jpg")
                },
                {
                    id: 3, img: require("../assets/chengdu.jpg")
                },
                {
                    id: 4, img: require("../assets/hangzhou.jpg")
                },
                {
                    id: 5, img: require("../assets/huanghelou.jpg")
                },
                {
                    id: 6, img: require("../assets/xiamen.jpg")
                },
                {
                    id: 7, img: require("../assets/wuxi.jpg")
                },
                {
                    id: 8, img: require("../assets/yunlonghu.jpg")
                },
                {
                    id: 9, img: require("../assets/shanghai.jpg")
                },
                {
                    id: 10, img: require("../assets/shaoxing.jpg")
                },
                {
                    id: 11, img: require("../assets/wuhan.jpg")
                },
                {
                    id: 12, img: require("../assets/jiuzhaigou.jpg")
                },
                {
                    id: 13, img: require("../assets/fenghuang.jpg")
                },
                {
                    id: 14, img: require("../assets/guizhou.jpg")
                },
                {
                    id: 15, img: require("../assets/haerbin.jpg")
                }
            ],
            idForm:{
              sfz:''
            },
            flightForm: {
                depAirport : '',
                arrAirport: '',
                depTime: '',
                activeIndex2: '1',
                student:[]
            }
        }
    },
    created() {
        this.idForm.sfz=JSON.parse(localStorage.getItem("sfz"));
        localStorage.setItem("idForm",JSON.stringify(this.idForm));
    },
    methods: {
      perpage(){
          this.axios.post('http://192.168.1.115:8080/user/get',this.idForm).then((resp) =>{
              console.log(resp);
              let data=resp.data;
              console.log(data);
              if(data.code===200){
                  localStorage.setItem("userform",JSON.stringify(data.data));
                  this.$message({
                      message: '个人信息',
                      type: 'success'
                  });
                  this.$router.push({path:'/Person'})
              }
              else{
                  this.$message({
                      message:data.data,
                      type: 'fail'
                  });
              }

          })

      },
      order(){
          this.idForm.userId=JSON.parse(localStorage.getItem("sfz"));
          localStorage.setItem("idForm",JSON.stringify(this.idForm

          ));
          this.axios.post('http://192.168.1.115:8080/book/history',this.idForm).then((resp) =>{
              console.log(resp);
              let data=resp.data;
              console.log(data);
              if(data.code===200){
                  localStorage.setItem("orderform",JSON.stringify(data.data));
                  this.$message({
                      message: '您的订单',
                      type: 'success'
                  });
                  this.$router.push({path:'/Inform'})
              }
              else{
                  this.$message({
                      message:data.data,
                      type: 'fail'
                  });
              }

          })

      },
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        },
        Search() {
            //console.log('submit!',this.loginForm);
            localStorage.setItem("depar",JSON.stringify(this.flightForm.depAirport+"至"+this.flightForm.arrAirport));
            localStorage.setItem("flightform",JSON.stringify(this.flightForm));
           this.axios.post('http://192.168.1.115:8080/flight/get', this.flightForm).then((resp) => {
                console.log(resp);
                let data = resp.data;
                console.log(data);
                if (data.code === 200) {
                    localStorage.setItem("flight",JSON.stringify(data.data));
                    console.log(data.data);
                    this.$message({
                        message: '查询到以下内容',
                        type: 'success'

                    });
                    this.$router.push({
                        path:'/Book',
                    });

                } else {
                    this.$message({
                        message: data.data,
                        type: 'fail'
                    });
                }
            })
        }
    },
}
</script>
<style>

.flight-container{
    position: fixed;
    top:50px;
    left: 950px;
    border-radius: 15px;
    background-clip: padding-box;
    margin: 60px;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
}
.scenic{
    position: fixed;
    top:100px;
    left: 50px;
    border:1px solid #000;
    width:900px; height:500px;

    font-family: 隶书;
    color: darkorchid;


}
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 400px;
    margin: 0;
}


</style>