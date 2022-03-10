
criaSaudacao = () => {
    const dataAtual = new Date()
    const hora = dataAtual.getHours()

    const saudacao = hora < 19 ? "Olá Usuário" : "Boa Noite"

    const elementoSaudacao = document.querySelector(".saudacao")
    elementoSaudacao.innerHTML = saudacao

    elementoSaudacao.style.fontWeight = "bold"
    elementoSaudacao.style.color = hora < 19 ? "red" : "blue"
}

excluirAnotacao = (event) => {
    console.log(event);
    let elemento = event.target.parentNode
    elemento = elemento.parentNode
    elemento.remove()

}
function excluirTodasanotacoes(){
    const tag = $("section");
    tag.empty(); // Apagar todos os elementos dentro da tag ou div

}
finalizaAnotacao = (event) => {
    let elemento = event.target.parentNode
    elemento = elemento.parentNode
    elemento.style.color = "gray"
    elemento.style.fontStyle = "italic"
    elemento.style.textDecoration = "line-through"
    
}
normalizaAnotacao = (event) => {
    let elemento = event.target.parentNode
    elemento = elemento.parentNode
    elemento.style.color = "black"
    elemento.style.fontStyle = "normal"
    elemento.style.textDecoration = "none"
}

function finalizaTodas(){
    
    elemento =document.getElementById("itens")
    elemento.style.color = "gray"
    elemento.style.fontStyle = "italic"
    elemento.style.textDecoration = "line-through"
    
}


criaAnotacao = (descricao) => {
    // console.log(descricao); 
    
    //cria div para cada anotacao
    const novaAnotacao = document.createElement("div")
    novaAnotacao.classList.add("item", "d-flex", "flex-row")

    const novaAnotacaoDesc = document.createElement("p")
    novaAnotacaoDesc.innerHTML = descricao
    novaAnotacaoDesc.classList.add("flex-grow-1")

    novaAnotacao.appendChild(novaAnotacaoDesc)

    //cria opcoes
    const opcoes = document.createElement("div")
    opcoes.classList.add("opcoes")

    novaAnotacao.appendChild(opcoes)

    // cria opcao excluir
    const opcaoExcluir = document.createElement("i")
    opcaoExcluir.classList.add("bi", "bi-trash")
    // evento disparado ao clicar no ícone lixeira
    opcaoExcluir.onclick = excluirAnotacao
    // opcaoExcluir.addEventListener("click", excluirAnotacao)



    //  cria opcao finalizar
    const opcaoFinalizar = document.createElement("i")
    opcaoFinalizar.classList.add("bi", "bi-check")
    opcaoFinalizar.onclick = finalizaAnotacao 

    const opcaoNormalizar = document.createElement("i")
    opcaoNormalizar.classList.add("bi", "bi-check")
    opcaoNormalizar.onclick = normalizaAnotacao 
    
    // insrindo as opçoes na div
    opcoes.appendChild(opcaoFinalizar)
    opcoes.appendChild(opcaoNormalizar)
    opcoes.appendChild(opcaoExcluir)
    
    // adicionando o item na lista
    const listaAnotacoes = document.querySelector("section")
    listaAnotacoes.appendChild(novaAnotacao)
}

document.getElementById("entrada").onkeypress = (event) => {
    // console.log(event);
    if (event.key == 'Enter') {
        criaAnotacao(event.target.value)    
    }
}

criaSaudacao()
