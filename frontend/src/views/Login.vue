<template>
  <n-alert :show-icon="true" type="error" v-if="errorMessage" class="login-error">{{ errorMessage }}</n-alert>
  <div class="login-container">
    <n-card class="login-card">
      <h2 class="login-title">Форма авторизации</h2>
      <n-form ref="formRef" :model="formData" :rules="rules">
        <n-form-item label="Имя пользователя" path="login">
          <n-input v-model:value="formData.login" placeholder="Введите имя пользователя" clearable />
        </n-form-item>
        <n-form-item label="Пароль" path="password">
          <n-input v-model:value="formData.password" type="password" placeholder="Введите пароль" clearable/>
        </n-form-item>
        <n-button type="primary" @click="submitForm" Validate>Войти</n-button>
      </n-form>
    </n-card>
  </div>
</template>

<script>
import { ref } from 'vue';
import { NCard, NForm, NFormItem, NInput, NButton, NAlert, useMessage } from 'naive-ui';
import axios from "axios";
import { useRouter } from 'vue-router';

export default {
  components: {
    NCard,
    NForm,
    NFormItem,
    NInput,
    NButton,
    NAlert
  },
  setup() {
    const router = useRouter();
    const formData = ref({
      login: null,
      password: null
    });

    const errorMessage = ref('');
    const formRef = ref(null);

    const rules = {
      login: [
        { required: true,
          message: 'Логин обязателен для заполнения',
          trigger: 'blur' }
      ],
      password: [
        { required: true, message: 'Пароль обязателен для заполнения', trigger: 'blur' }
      ]
    };

    const submitForm = () => {
      if (!formData.value.login || !formData.value.password) {
          errorMessage.value = 'Пожалуйста, заполните обязательные поля.';
        } else {
          sendMessageToBackend();
        }
    };

    const sendMessageToBackend = () => {
      const requestData = {
        login: formData.value.login,
        password: formData.value.password
      };

      axios.post('http://localhost:8000/user/login', requestData)
        .then(response => {
          errorMessage.value = '';
          router.push({name: 'Table', params: {clients : JSON.stringify(response.data)}});
        })
        .catch(error => {
          console.log(error)
          if (error.response.status === 404)
            errorMessage.value = 'Пользователь со введёнными вами данными не найден'
          else
            errorMessage.value = 'Ошибка при отправке запроса на сервер';
        });
    };

    return {
      formData,
      errorMessage,
      formRef,
      rules,
      submitForm
    };
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-card {
  width: 400px;
}

.login-title {
  margin-bottom: 20px;
}

.login-error {
  margin-top: 20px;
}
</style>