<template>
  <header class="bg-blue-600 text-white py-4 px-6 shadow-lg">
    <div class="container mx-auto flex justify-between items-center">
      <div class="flex items-center space-x-2">
        <i class="fa fa-database text-2xl"></i>
        <h1 class="text-xl font-bold">大数据分析教学平台</h1>
      </div>
      <nav>
        <ul class="flex space-x-6">
          <li><router-link to="/" class="hover:text-blue-200 transition-colors">首页</router-link></li>
          <li><router-link to="/query" class="hover:text-blue-200 transition-colors">数据查询</router-link></li>
          <li><router-link to="/analysis" class="hover:text-blue-200 transition-colors">数据分析</router-link></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
// 全局头部组件逻辑
</script>  