<template>


<body id="poster" style=" overflow: scroll;">
  <h1>查询到从
      <h2>
       {{depar}}
  </h2>
      的航班</h1>

  <el-table class="book-container" label-position="left" label-width="0px"
          :data="flight"
          stripe
          style="width: 100%" >
      <el-table-column
              prop="airline"
              label="航空公司"
              width="180" >
      </el-table-column>
      <el-table-column
              prop="depAirport"
              label="出发地"
              width="180" >
      </el-table-column>
     <el-table-column
              prop="arrAirport"
              label="目的地"
              width="180">
      </el-table-column>
      <el-table-column
              prop="depTime"
              label="起飞时间">
      </el-table-column>
      <el-table-column
              prop="arrTime"
              label="降落时间"
              width="180">
      </el-table-column>
      <el-table-column
              prop="price"
              label="价格"
              width="180">
      </el-table-column>
      <el-table-column
              prop="availableSeats"
              label="剩余座位"
              width="180">
      </el-table-column>
      <el-table-column
              prop="id"
              label="预订机票"
              width="180">
          <template slot-scope="scope">
              <!--<el-button type="primary"  style="width: 100%;background: #2c3e50;border: none" @click="bookFlight()">订票</el-button>-->
              <el-button type="primary"  style="width: 100%;color: floralwhite;border: none"
                         @click="bookFlight(sfz,scope.row.id)">订票</el-button>
          </template>

      </el-table-column>

  </el-table>






</body>


</template>



<script>


export default {
    name: 'Book',

    mounted() {
        document.querySelector('body').setAttribute('style',
            "background-image: url("+require("../assets/lake.jpg")+");background-size: cover;" +
            "background-repeat: no-repeat")
    },
    beforeDestroy() {
        document.querySelector('body').removeAttribute('style')
    },

    data() {
        return {
            flight:[],
            depar:[],
            sfz:[],
            bookForm: {
                userId: '',
                flightId:'',
                seatnum:'123'

            }
        }
    },
    created() {
       var flight=JSON.parse(localStorage.getItem("flight"));
        var depar=JSON.parse(localStorage.getItem("depar"));
        var sfz=JSON.parse(localStorage.getItem("sfz"));
        this.sfz=sfz;
       this.flight=flight;
       this.depar=depar;
       console.log("身份证",sfz);
        console.log("获取到的数据",flight);
        console.log("出发目的地",depar);
    },
    methods: {
        bookFlight(pid,fid){

            console.log(pid,fid);
            this.bookForm.flightId=fid;
            this.bookForm.userId=pid;
            localStorage.setItem("flightinfo",JSON.stringify(this.bookForm));
            this.axios.post('http://192.168.1.115:8080/book/add',this.bookForm).then((resp) =>{
                console.log(resp);
                let data=resp.data;
                console.log(data);
                if(data.code===200){
                    this.$message({
                        message: '恭喜您成功订票,可去”我的订单“中查看',
                        type: 'success'
                    });
                        this.axios.post('http://192.168.1.115:8080/flight/get', JSON.parse(localStorage.getItem("flightform"))).then((resp) => {
                            console.log(resp);
                            let data = resp.data;
                            console.log(data);
                            if (data.code === 200) {
                                localStorage.setItem("flight",JSON.stringify(data.data));
                                console.log(data.data);
                        } else {
                            this.$message({
                                message: data.data,
                                type: 'fail'
                            });
                        }
                      })
                }
                else{
                    this.$message({
                        message:data.data,
                        type: 'fail'
                    });
                }

            });
            /*this.axios.post('http://192.168.1.100:8080/book/add',this.bookForm).then((resp) =>{
                console.log(resp);
                let data=resp.data;
                console.log(data);
                if(data.code===200){
                    this.$message({
                        message: '恭喜您成功订票',
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

            })*/
        },

        /*bookFlight(){

            localStorage.setItem("ID",JSON.stringify(this.bookForm.id));
            console.log("航班ID",this.bookForm.id);
            this.$message({
                message: '恭喜您订票成功',
                type: 'success'
            });
            this.$router.push({
                path:'/Inform',
            });
        }*/

    }

}


</script>



<style>
.book-container{


    border: 10px solid;color: cornflowerblue;

}
h1{
    font-family: 隶书;
    color: cornflowerblue;
}



</style>