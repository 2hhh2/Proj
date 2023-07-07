<template>
    <div id="poster">
        <el-form
            :model="ruleForm"
            status-icon
            :rules="rules"
            ref="ruleForm"
            label-position="left"
            label-width="0px"
            class="register-container">
            <h3 class="register_title">
                系统注册
                <el-button  @click="toLogin()">去登录</el-button>
            </h3>
            <el-form-item label="" prop="loginName">
                <el-input
                    type="text"
                    autocomplete="off"
                    v-model="ruleForm.sfz"
                    placeholder="请输入用户名"
                    prefix-icon="el-icon-user-solid"
                ></el-input>
            </el-form-item>
            <el-form-item label="" prop="name">
                <el-input
                    type="text"
                    autocomplete="off"
                    v-model="ruleForm.name"
                    placeholder="请输入网名"
                    prefix-icon="el-icon-user-solid"
                ></el-input>
            </el-form-item>
            <el-form-item label="" prop="password">
                <el-input type="password" v-model="ruleForm.password"
                          autocomplete="off" placeholder="请输入密码"
                          prefix-icon="el-icon-lock"
                ></el-input>
            </el-form-item>
            <el-form-item label="" prop="checkPass">
                <el-input type="password" v-model="ruleForm.checkPass"
                          autocomplete="off" placeholder="确认密码"
                          prefix-icon="el-icon-lock"
                ></el-input>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" style="background: greenyellow;border: none" @click="submitForm(ruleForm)">注册</el-button>
                <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>


export default {
    name: 'Register',
    mounted() {
        document.querySelector('body').setAttribute('style',
            "background-image: url("+require("../assets/sea.jpg")+");background-size: cover;" +
            "background-repeat: no-repeat")
    },
    beforeDestroy() {
        document.querySelector('body').removeAttribute('style')
    },

    data() {
        var validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入密码'));
            } else {
                if (this.ruleForm.checkPass !== '') {
                    this.$refs.ruleForm.validateField('checkPass');
                }
                callback();
            }
        };
        var validatePass2 = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请再次输入密码'));
            } else if (value !== this.ruleForm.password) {
                callback(new Error('两次输入密码不一致!'));
            } else {
                callback();
            }
        };
        return {
            ruleForm: {
                sfz: '',
                password: '',
                name: '',
                checkPass:''
            },
            rules: {
                sfz: [
                    { required: true,message:'请输入你的名称' ,trigger: 'blur' },
                    { min:2, max:9,message:'长度需为2到9个字符' ,trigger: 'blur' },
                ],
                password: [
                    { validator: validatePass, trigger: 'blur' }
                ],
                checkPass: [
                    { validator: validatePass2, trigger: 'blur' }
                ]
            }
        };
    },
    methods: {
        submitForm(ruleForm) {
            this.axios.post('http://192.168.1.110:8080/user/register',this.ruleForm).then((resp) =>{
                console.log(resp);
                let data=resp.data;
                console.log(data);
                if(data.code===200){
                    this.ruleForm={};
                    this.$message({
                        message: '您已成功注册',
                        type: 'success'
                    });
                    this.$router.push({path:'/Login'})
                }else{
                    this.$message({
                        message:data.data,
                        type: 'fail'
                    });
                }

            })
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        },
        toLogin(){
            this.$router.push({path:'/'})
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
    margin: 0px;
    padding: 0px;
}

.register-container{
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
.register_title{
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
}

</style>