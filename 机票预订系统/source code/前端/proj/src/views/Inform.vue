<template>
    <body id="poster" style=" overflow: scroll;">
    <h1>我的订单</h1>

    <el-table class="Inform-container" label-position="left" label-width="0px"
            :data="orderform"
            style="width: 100%;" >
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
                           @click="refundFlight(sfz,scope.row.id)">退票</el-button>
            </template>

        </el-table-column>

    </el-table>

</body>
</template>

<script>


export default {
    name: 'Inform',
    mounted() {
        document.querySelector('body').setAttribute('style',
            "background-image: url("+require("../assets/tianzhushan.jpg")+");background-size: cover;" +
            "background-repeat: no-repeat")
    },
    beforeDestroy() {
        document.querySelector('body').removeAttribute('style')
    },

    data() {
        return {
            orderform:[],
            sfz:[],
            refundForm:{
                userId: '',
                flightId:'',
                seatnum:'123'
            }

        }
    },
    created() {
        var orderform=JSON.parse(localStorage.getItem("orderform"));
        var sfz=JSON.parse(localStorage.getItem("sfz"));
        this.sfz=sfz;
        this.orderform=orderform;
        console.log(orderform);

    },
    methods: {
       refundFlight(pid,fid){
           console.log(pid,fid);
           this.refundForm.flightId=fid;
           this.refundForm.userId=pid;
           /*localStorage.setItem("flightinfo",JSON.stringify(this.bookForm));*/
           this.axios.post('http://192.168.1.115:8080/book/delete',this.refundForm).then((resp) =>{
               console.log(resp);
               let data=resp.data;
               console.log(data);
               if(data.code===200){
                   this.$message({
                       message: '您已成功退票',
                       type: 'success'
                   });
                   this.axios.post('http://192.168.1.115:8080/book/history', JSON.parse(localStorage.getItem("idForm")
                   )).then((resp) => {
                       console.log(resp);
                       let data = resp.data;
                       console.log(data);
                       if (data.code === 200) {
                           localStorage.setItem("orderform",JSON.stringify(data.data));
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
       }

        },

}
</script>
<style>
.Inform-container{

    border: 10px solid;color: cornflowerblue;

}




</style>