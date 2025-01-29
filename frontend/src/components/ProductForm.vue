<template>
  <div>
    <h2>Criar Produto</h2>
    <form @submit.prevent="createProduct">
      <input v-model="name" type="text" placeholder="Nome do Produto" required />
      <input v-model="price" type="number" placeholder="Preço" required />
      <button type="submit">Adicionar Produto</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      price: '',
    };
  },
  methods: {
    async createProduct() {
      try {
        const productData = {
          name: this.name,
          price: parseFloat(this.price),
        };
        await axios.post('http://localhost:8000/products/', {
          name: this.name,
          price: parseFloat(this.price),
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        } ,productData);
        this.$emit('product-added'); // Emite evento para atualizar lista
        this.name = '';
        this.price = '';
      } catch (error) {
        console.error('Erro ao criar produto', error);
      }
    }
  }
};
</script>
