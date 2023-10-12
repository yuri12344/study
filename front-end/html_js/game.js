const trocaElements = (tag, text) => {
    const element = document.querySelector(tag)
    element.textContent = text
}

trocaElements('ol', 'Atividade 10')

