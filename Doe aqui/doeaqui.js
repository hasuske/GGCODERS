function selecionarValor(valor) {
    document.getElementById('valorDoacao').value = valor.toFixed(2); // Limpar campo "Outro valor"
    document.getElementById('outroValor').disabled = true; // Desabilitar campo "Outro valor"
    document.getElementById('outroValor').setAttribute('data-valor', valor); // Salvar o valor selecionado
  }
  
  function mostrarCampoOutroValor() {
    document.getElementById('valorDoacao').value = ''; //limpar campo de valor
    document.getElementById('outroValor').disabled = false; // Habilitar campo "Outro valor"
  }
  
  function realizarDoacao() {
    let valorDoacao = document.getElementById('valorDoacao').value;
    if (valorDoacao === '') {
      valorDoacao = document.getElementById('outroValor').value;
    }
  
    // Coletar os valores dos campos de CPF, nome, sobrenome, email, etc.
    // Realizar a chamada para o processamento da doação usando o valor coletado
  
    // Exemplo de chamada para o backend:
    // fetch('URL_DO_BACKEND', {
    //   method: 'POST',
    //   body: JSON.stringify({
    //     valor: valorDoacao,
    //     cpf: document.getElementById('cpf').value,
    //     nome: document.getElementById('nome').value,
    //     // ... outros campos
    //   }),
    //   headers: {
    //     'Content-Type': 'application/json'
    //   }
    // })
    // .then(response => {
    //   // Tratar a resposta do servidor
    // })
    // .catch(error => {
    //   // Lidar com erros
    // });
  }
  