$("document").ready(function(){
    console.log("teste")
    //como se fosse um for, para o jquery
    //Ao carregar a pagina, ele associa esse evento ao clique do botao
    //vai buscar todos os itens que tem a classe "stop"
    $(".stop").each(function(){
        $(this).click(function(){
            var cid = $(this).attr("id");
            $.ajax({
              url: "/container/stop",
              type: "POST",
              data: {cid:cid}
            })
            .done(function(data){
              alert(data.message);
              window.location.href = "/"
            })
            .fail(function(data){
              alert(data.message);
              console.log(data);
            })
            
        })
    })

    //funcao para Capturar click e startar  docker
    $(".start").each(function(){
        $(this).click(function(){
            var cid = $(this).attr("id");
            $.ajax({
              url: "/container/start",
              type: "POST",
              data: {cid:cid}
            })
            .done(function(data){
              alert(data.message);
              window.location.href = "/"
            })
            .fail(function(data){
              alert(data.message);
              console.log(data);
            })
            
        })
    })

    //funcao para Capturar click do "Criar"
    $(".criar").each(function(){
        $(this).click(function(){
            var name = prompt("Digite o nome do Container:");
            $.ajax({
              url: "/container/criar",
              type: "POST",
              data: {name:name, image:"ubuntu"}
            })
            .done(function(data){
              alert(data.message);
              window.location.href = "/"
            })
            .fail(function(data){
              alert(data.message);
              console.log(data);
            })
            
        })
    })


});
