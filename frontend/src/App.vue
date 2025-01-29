<template>
  <div id="app">
    <h1>Gerenciamento de Produtos</h1>
    <ProductForm @product-added="fetchProducts" />
    <ProductList />
  </div>
</template>

<script>
import ProductForm from './components/ProductForm.vue';
import ProductList from './components/ProductList.vue';

export default {
  components: {
    ProductForm,
    ProductList
  }
};
</script>
