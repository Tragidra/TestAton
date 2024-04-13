<template>
  <div>
    <n-table :data="clients" v-if="clients.length > 0">
      <thead>
        <tr>
          <th>Номер счёта</th>
          <th>Фамилия</th>
          <th>Имя</th>
          <th>Отчество</th>
          <th>Дата рождения</th>
          <th>ИНН</th>
          <th>ФИО ответственного</th>
          <th>Статус</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="client in clients" :key="client.id">
          <td>{{client.score_numbers}}</td>
          <td>{{client.surname}}</td>
          <td>{{client.name}}</td>
          <td>{{client.patronymic}}</td>
          <td>{{client.date_of_birth}}</td>
          <td>{{client.inn}}</td>
          <td>{{client.responsible}}</td>
          <td>
            <n-select v-model:value="client.status" v-model="client.status"
                      :options="statusOptions" @update:value="changeStatus(client)"></n-select>
          </td>
        </tr>
      </tbody>
    </n-table>
    <div v-else>Нет данных для отображения</div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { NTable, NSelect } from 'naive-ui';
import { useRoute } from "vue-router";
import axios from "axios";

export default {
  components: {
    NTable,
    NSelect
  },
  setup() {
    const route = useRoute();
    const clients = ref(JSON.parse(route.params.clients));

    const statusOptions = [
      { label: 'В работе', value: 'В работе' },
      { label: 'Не в работе', value: 'Не в работе' },
    ];

    const changef = async (value) => {
      try {
          console.log(value)
        //  axios.post('http://localhost:8000/clients/update', client)
        // .then(response => {
        //   console.log(response.data)
        // })
        // .catch(error => {
        //   console.log(error)
        // });
      } catch (error) {
        console.error(error);
      }
    };

    return {
      clients,
      statusOptions,
      changeStatus(value){
        axios.post('http://localhost:8000/clients/update/', value)
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        });
      }
    };
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

</style>
