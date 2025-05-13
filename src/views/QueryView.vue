<template>
  <div class="QueryView">
    <GlobalHeader />
    <div class="container mx-auto px-4 py-8">
      <QueryForm @query-success="handleQuerySuccess" />
      <ResultTable :data="queryData" :loading="loading" :error="error" />
    </div>
  </div>
</template>

<script setup>
import GlobalHeader from '@/components/GlobalHeader.vue';
import QueryForm from '@/components/QueryForm.vue';
import ResultTable from '@/components/ResultTable.vue';
import { ref } from 'vue';

const queryData = ref([]);
const loading = ref(false);
const error = ref(null);

const handleQuerySuccess = (data) => {
  queryData.value = data;
};
</script>  