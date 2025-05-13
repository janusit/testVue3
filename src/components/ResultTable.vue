<template>
  <div class="bg-white rounded-lg shadow-md overflow-hidden">
    <div v-if="loading" class="p-6 text-center">
      <i class="fa fa-spinner fa-spin text-blue-500"></i> 加载中...
    </div>
    <div v-else-if="error" class="p-6 text-red-500">
      <i class="fa fa-exclamation-circle mr-2"></i>{{ error }}
    </div>
    <div v-else>
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th v-for="(header, index) in headers" :key="index" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                {{ header }}
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="(row, rowIndex) in data" :key="rowIndex" class="hover:bg-gray-50 transition-colors">
              <td v-for="(cell, colIndex) in row" :key="colIndex" class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ cell }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="p-4 flex justify-between items-center border-t border-gray-200">
        <div class="text-sm text-gray-700">
          共 {{ data.length }} 条记录
        </div>
        <div>
          <button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded transition-colors">
            <i class="fa fa-download mr-2"></i>导出数据
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  data: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: null
  }
});

// 计算表头
const headers = props.data.length > 0 ? Object.keys(props.data[0]) : [];
</script>  