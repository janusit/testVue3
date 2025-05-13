<template>
  <div>
    <GlobalHeader />
    <div class="container mx-auto px-4 py-8">
      <h2 class="text-2xl font-bold mb-6">数据分析</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div class="bg-white p-6 rounded-lg shadow-md">
          <h3 class="text-lg font-semibold mb-4">数据统计</h3>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">选择分析类型</label>
              <select v-model="analysisType" class="w-full p-2 border border-gray-300 rounded">
                <option value="count">记录总数</option>
                <option value="avg">平均值</option>
                <option value="sum">总和</option>
                <option value="max">最大值</option>
                <option value="min">最小值</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">选择字段</label>
              <select v-model="analysisField" class="w-full p-2 border border-gray-300 rounded">
                <option value="age">年龄</option>
                <option value="salary">薪资</option>
                <option value="score">分数</option>
              </select>
            </div>
            <button @click="runAnalysis" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded transition-colors">
              <i class="fa fa-calculator mr-2"></i>执行分析
            </button>
          </div>
        </div>
        
        <div class="bg-white p-6 rounded-lg shadow-md">
          <h3 class="text-lg font-semibold mb-4">分析结果</h3>
          <div v-if="analysisResult" class="p-4 bg-gray-50 rounded">
            <p class="text-lg font-medium">
              {{ analysisTypeText }}: <span class="text-blue-600">{{ analysisResult }}</span>
            </p>
          </div>
          <div v-else class="p-4 text-gray-500 italic">
            请执行数据分析
          </div>
        </div>
      </div>
      
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h3 class="text-lg font-semibold mb-4">数据可视化</h3>
        <div class="h-80">
          <canvas ref="chartCanvas"></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import Chart from 'chart.js/auto';

const analysisType = ref('count');
const analysisField = ref('age');
const analysisResult = ref(null);
const chartCanvas = ref(null);
let chartInstance = null;

const analysisTypeText = computed(() => {
  const map = {
    'count': '记录总数',
    'avg': '平均值',
    'sum': '总和',
    'max': '最大值',
    'min': '最小值'
  };
  return map[analysisType.value] || '分析结果';
});

const runAnalysis = async () => {
  try {
    const response = await axios.post('/api/analyze', {
      type: analysisType.value,
      field: analysisField.value
    });
    
    analysisResult.value = response.data.result;
    updateChart(response.data.chartData);
  } catch (err) {
    console.error(err);
    alert('分析失败');
  }
};

const updateChart = (chartData) => {
  if (chartInstance) {
    chartInstance.destroy();
  }
  
  chartInstance = new Chart(chartCanvas.value, {
    type: 'bar',
    data: {
      labels: chartData.labels,
      datasets: [{
        label: analysisField.value,
        data: chartData.values,
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
};

onMounted(() => {
  // 初始化图表
  updateChart({
    labels: ['一月', '二月', '三月', '四月', '五月', '六月'],
    values: [12, 19, 3, 5, 2, 3]
  });
});
</script>  