<template>
  <div>
    <h2>Lista de Produtos</h2>
    <ul>
      <li v-for="product in products" :key="product.id">
        {{ product.name }} - R$ {{ product.price }}
        <button @click="deleteProduct(product.name)">Excluir</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      products: [],
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost:8000/products/');
        this.products = response.data;
      } catch (error) {
        console.error('Erro ao buscar produtos', error);
      }
    },
    async deleteProduct(name) {
      try {
        await axios.delete('http://localhost:8000/products/', {
          params: { name }
        });
        this.fetchProducts(); // Atualiza a lista após excluir
      } catch (error) {
        console.error('Erro ao excluir produto', error);
      }
    }
  }
};
</script>
