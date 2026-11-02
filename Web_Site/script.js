const QUANTIDADE_ESPERADA = 5;
const IMAGEM_SUBSTITUTA =
  "data:image/svg+xml;utf8," +
  encodeURIComponent(
    '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="450" viewBox="0 0 600 450">' +
      '<rect width="600" height="450" fill="#e2e4e8"/>' +
      '<text x="300" y="235" font-family="sans-serif" font-size="28" fill="#555555" text-anchor="middle">Imagem indisponível</text>' +
    "</svg>"
  );

// Elementos fixos do HTML, buscados uma vez só para simplificar o código
const elementoTitulo = document.getElementById("titulo-site");
const elementoCriador = document.getElementById("nome-criador");
const elementoGaleria = document.getElementById("galeria");

// Só aceita textos que começam com http:// ou https://. - Envita kunks vazios.
function linkEhValido(url) {
  return typeof url === "string" && /^https?:\/\//i.test(url.trim());
}

// Mostra um erro visível na página, para a pessoa entender o que houve
function mostrarErro(mensagem) {
  const caixaErro = document.createElement("p");
  caixaErro.className = "mensagem-erro";
  // textContent (e não innerHTML) trata a mensagem como texto puro, o que é mais seguro
  caixaErro.textContent = mensagem;
  elementoGaleria.appendChild(caixaErro);
}

// Cria a <img> já preparada para o caso de a imagem não carregar.
function criarImagem(item) {
  const imagem = document.createElement("img");
  imagem.className = "cartao__imagem";
  imagem.alt = item.tituloImagem || "Imagem sem título";

  // Se a imagem falhar, troca pela substituta.
  imagem.onerror = function () {
    imagem.onerror = null;
    imagem.src = IMAGEM_SUBSTITUTA;
  };

  // Um src vazio nem sempre dispara o onerror.
  imagem.src = item.urlImagem ? item.urlImagem : IMAGEM_SUBSTITUTA;
  return imagem;
}

// Monta um cartão completo
function criarCartao(item) {
  item = item || {};

  const cartao = document.createElement("article");
  cartao.className = "cartao";

  const imagem = criarImagem(item);
  const temLinkValido = linkEhValido(item.urlPagina);

  if (temLinkValido) {

    // Link válido: a imagem fica dentro de um <a> que abre em nova aba.
    // rel="noopener noreferrer" impede que a nova página controle esta aba.
    const link = document.createElement("a");
    link.className = "cartao__moldura";
    link.href = item.urlPagina.trim();
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.appendChild(imagem);
    cartao.appendChild(link);
  } else {
    
    // Link inválido: a imagem aparece, mas sem ser clicável
    const moldura = document.createElement("div");
    moldura.className = "cartao__moldura";
    moldura.appendChild(imagem);
    cartao.appendChild(moldura);
  }

  // Título visível abaixo da imagem
  const titulo = document.createElement("h2");
  titulo.className = "cartao__titulo";
  titulo.textContent = item.tituloImagem || "Sem título";
  cartao.appendChild(titulo);

  // O aviso toma o lugar do link quando ele não é válido
  if (!temLinkValido) {
    const aviso = document.createElement("p");
    aviso.className = "cartao__aviso";
    aviso.textContent = "Link inválido";
    cartao.appendChild(aviso);
  }

  return cartao;
}

// Função principal: valida o CONFIG e monta a página
function iniciar() {
  if (typeof CONFIG === "undefined") {
    console.error("O CONFIG não foi encontrado. Verifique se o arquivo config.js está na mesma pasta e se o nome está correto.");
    mostrarErro("Erro: não foi possível carregar o arquivo config.js.");
    return;
  }

  // Preenche título da aba, título do site e criador
  const titulo = CONFIG.tituloSite || "Galeria de Imagens";
  document.title = titulo;
  elementoTitulo.textContent = titulo;
  elementoCriador.textContent = "Criado por: " + (CONFIG.nomeCriador || "não informado");

  const itens = CONFIG.itens;
  if (!Array.isArray(itens) || itens.length !== QUANTIDADE_ESPERADA) {
    const quantidadeAtual = Array.isArray(itens) ? itens.length : 0;
    console.error(
      "CONFIG.itens deve ter exatamente " + QUANTIDADE_ESPERADA +
      " itens, mas foram encontrados " + quantidadeAtual + "."
    );
    mostrarErro(
      "Erro: o config.js precisa ter exatamente " + QUANTIDADE_ESPERADA +
      " itens em CONFIG.itens (encontrados: " + quantidadeAtual + ")."
    );
    return;
  }

  // Cria um cartão para cada item e coloca na galeria
  itens.forEach(function (item) {
    elementoGaleria.appendChild(criarCartao(item));
  });
}
iniciar();