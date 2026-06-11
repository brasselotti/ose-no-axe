window.addEventListener("load", function() {
    // === CÓDIGO EXISTENTE DA CHECKBOX DE INICIAÇÃO ===
    const checkbox = document.getElementById("id_filho_iniciado");
    const blocoIniciacao = document.querySelector(".grp-iniciacao");

    if (checkbox && blocoIniciacao) {
        function alternarCampos() {
            if (checkbox.checked) {
                blocoIniciacao.style.display = "block";
            } else {
                blocoIniciacao.style.display = "none";
            }
        }
        alternarCampos();
        checkbox.addEventListener("change", alternarCampos);
    }

    // === NOVO CÓDIGO DAS MÁSCARAS (SEM DEPENDÊNCIAS) ===
    const campoTelefone = document.getElementById("id_telefone");
    const campoCEP = document.getElementById("id_cep");

    // Lógica para aplicar máscara no CEP (00000-000)
    if (campoCEP) {
        campoCEP.addEventListener("input", function(e) {
            let x = e.target.value.replace(/\D/g, "").match(/(\d{0,5})(\d{0,3})/);
            e.target.value = !x[2] ? x[1] : x[1] + "-" + x[2];
        });
    }

    // Lógica para aplicar máscara no Telefone ((00) 00000-0000)
    if (campoTelefone) {
        campoTelefone.addEventListener("input", function(e) {
            let valor = e.target.value.replace(/\D/g, "");
            if (valor.length > 11) valor = valor.slice(0, 11); // Limita em 11 dígitos

            if (valor.length > 10) {
                // Formato Celular: (11) 99999-9999
                e.target.value = valor.replace(/^(\d{2})(\d{5})(\d{4})$/, "($1) $2-$3");
            } else if (valor.length > 6) {
                // Formato Fixo intermediário: (11) 9999-9999
                e.target.value = valor.replace(/^(\d{2})(\d{4})(\d{0,4})$/, "($1) $2-$3");
            } else if (valor.length > 2) {
                e.target.value = valor.replace(/^(\d{2})(\d{0,5})$/, "($1) $2");
            } else {
                e.target.value = valor;
            }
        });
    }
});
