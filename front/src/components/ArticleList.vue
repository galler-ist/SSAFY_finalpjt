<template>
  <div class="aaaa">

    <div class="bbbb">
      
      <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
      />
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()
</script>

<style scoped>
.aaaa {
  width: 100%;
  display: flex;
  flex-direction: column;
}
.bbbb {
  padding: 0;
}
</style>
