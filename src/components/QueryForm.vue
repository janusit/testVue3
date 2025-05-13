<template>
  <div class="bg-white p-6 rounded-lg shadow-md mb-6">
    <h2 class="text-xl font-semibold mb-4">数据查询</h2>
    <form @submit.prevent="submitQuery">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">数据表</label>
          <select v-model="tableName" class="w-full p-2 border border-gray-300 rounded">
            <option value="users">用户表</option>
            <option value="orders">订单表</option>
            <option value="products">产品表</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">查询字段</label>
          <input v-model="fields" type="text" placeholder="id,name,age" class="w-full p-2 border border-gray-300 rounded">
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">过滤条件</label>
          <input v-model="condition" type="text" placeholder="age > 18" class="w-full p-2 border border-gray-300 rounded">
        </div>
      </div>
      <div class="mt-4">
        <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded transition-colors">
          <i class="fa fa-search mr-2"></i>执行查询
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';
import axios from 'axios';

const tableName = ref('users');
const fields = ref('*');
const condition = ref('');
const queryResult = ref(null);
const loading = ref(false);
const error = ref(null);

const emit = defineEmits(['query-success']);

const submitQuery = async () => {
  loading.value = true;
  error.value = null;
  
  try {
    const response = await axios.post('/api/query', {
      table: tableName.value,
      fields: fields.value,
      condition: condition.value
    });
    
    queryResult.value = response.data;
    emit('query-success', response.data);
  } catch (err) {
    error.value = err.message;
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>  