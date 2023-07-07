<template>
    <body id="poster">
     <h1 >
         个人信息主页
     </h1>

     <el-form class="person-container" label-position="left" label-width="0px">
         <el-upload
                 class="upload-demo"
                 drag
                 action="https://jsonplaceholder.typicode.com/posts/"
                 multiple>
             <i class="el-icon-upload"></i>
             <div class="el-upload__text">点击上传头像</div>
             <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
         </el-upload>
         <el-form-item label="">
             <el-input type="text"   v-model="personForm.name" autocomplete="off" placeholder="姓名" prefix-icon="el-icon-edit"></el-input>
         </el-form-item>
         <el-form-item label="">
             <el-input type="text"   v-model="personForm.sex" autocomplete="off" placeholder="性别" prefix-icon="el-icon-s-custom"></el-input>
         </el-form-item>
         <el-form-item label="">
             <el-input type="text"   v-model="personForm.phonenum" autocomplete="off" placeholder="电话号码" prefix-icon="el-icon-phone-outline"></el-input>
         </el-form-item>
         <el-form-item label="">
             <el-input type="password"   v-model="personForm.password" autocomplete="off" placeholder="修改密码" prefix-icon="el-icon-edit"></el-input>
         </el-form-item>
         <el-form-item>
             <el-button type="primary" style="width: 100%;background: cornflowerblue;border: none" @click="update()">上传</el-button>

         </el-form-item>
         <div>
             <span>粉丝：0</span>
             <el-divider direction="vertical"></el-divider>
             <span>关注：22</span>
             <el-divider direction="vertical"></el-divider>
             <span>获赞:5</span>
             <el-divider direction="vertical"></el-divider>
             <span>赞过:112</span>
         </div>
         <el-tag style="width: 100px">我的积分</el-tag>
         <el-tag type="success" style="width: 100px">我的优惠券</el-tag>
         <el-tag type="info" style="width: 100px">我的奖品</el-tag>

     </el-form>
    </body>
</template>

<script>


export default {
    name: 'Person',
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
            personForm:{
                name:'',
                sex:'',
                phonenum:'',
                password:''
            }
        }
    },
    created() {
        this.personForm=JSON.parse(localStorage.getItem("userform"));
    },
    methods: {
        update()
        {
            this.axios.post('http://192.168.1.115:8080/user/update',this.personForm).then((resp) =>{
                console.log(resp);
                let data=resp.data;
                console.log(data);
                if(data.code===200){

                    this.$message({
                        message: '上传成功',
                        type: 'success'
                    });
                    this.axios.post('http://192.168.1.115:8080/user/get',JSON.parse(localStorage.getItem("idForm"))).then((resp) =>{
                        console.log(resp);
                        let data=resp.data;
                        console.log(data);
                        if(data.code===200){
                            localStorage.setItem("userform",JSON.stringify(data.data));

                        }
                        else{
                            this.$message({
                                message:data.data,
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

            })
        },

        handleAvatarSuccess(res, file) {
            this.imageUrl = URL.createObjectURL(file.raw);
        },
        beforeAvatarUpload(file) {
            const isJPG = file.type === 'image/jpeg';
            const isLt2M = file.size / 1024 / 1024 < 2;

            if (!isJPG) {
                this.$message.error('上传头像图片只能是 JPG 格式!');
            }
            if (!isLt2M) {
                this.$message.error('上传头像图片大小不能超过 2MB!');
            }
            return isJPG && isLt2M;
        }

        },

}
</script>
<style>


.person-container{
    position: fixed;
    top: 0px;
    left: 480px;
    border-radius: 15px;
    background-clip: padding-box;
    margin: 90px;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
}

</style>