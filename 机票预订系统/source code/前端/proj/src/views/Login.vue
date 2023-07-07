<template>
    <body id="poster">
    <h1>
        欢迎使用机票预订系统
    </h1>
    <el-form class="login-container" label-position="left" label-width="0px">
        <h3 class="login_title">
            系统登录
            <el-button  @click="toRegister()">点我注册</el-button>
        </h3>
        <el-form-item label="">
            <el-input type="text"   v-model="loginForm.sfz" autocomplete="off" placeholder="账号"></el-input>
        </el-form-item>
        <el-form-item label="">
            <el-input type="password" v-model="loginForm.password" autocomplete="off" placeholder="密码"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" style="width: 100%;background: #505458;border: none" @click="Login()">登录</el-button>

        </el-form-item>
    </el-form>
    </body>
</template>

<script>


export default {
    name: 'Login',
    mounted() {
        document.querySelector('body').setAttribute('style',
            "background-image: url("+require("../assets/sea.jpg")+");background-size: cover;" +
            "background-repeat: no-repeat")
    },
    beforeDestroy() {
        document.querySelector('body').removeAttribute('style')
    },

    data() {
        return {
            loginForm: {
                name: '',
                password: '',
                sfz: ''

            }
        }
    },
    methods: {
        Login() {
            //console.log('submit!',this.loginForm);
            localStorage.setItem("sfz",JSON.stringify(this.loginForm.sfz));
           this.axios.post('http://192.168.1.115:8080/user/login',this.loginForm).then((resp) =>{
                console.log(resp);
                let data=resp.data;
                console.log(data);
                if(data.code===200){
                    this.loginForm={};
                    this.$message({
                        message: '您已成功登录，欢迎来到机票预订系统',
                        type: 'success'
                    });
                    this.$router.push({path:'/Flight'})
                }
                else{
                    this.$message({
                        message:data.data,
                        type: 'fail'
                    });
                }

            })
        },
        toRegister(){
            this.$router.push({path:'/Register'})
        }
    }

}
</script>
<style>
    #poster{
        background-position: center ;
        height: 100%;
        width: 100%;
        background-size: cover;
        position: fixed;
    }

    .login-container{
        float: right;
        border-radius: 15px;
        background-clip: padding-box;
        margin: 90px;
        width: 350px;
        padding: 35px 35px 15px 35px;
        background: #fff;
        border: 1px solid #eaeaea;
        box-shadow: 0 0 25px #cac6c6;
    }
    .login_title{
       margin: 0px auto 40px auto;
       text-align: center;
        color: #505458;
    }
    h1{
        font-family: "Lucida Console", "Courier New", monospace;
    }

</style>