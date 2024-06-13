
def formulario_cadastrar_policial():
    return render_template("cadastro_policial.html")

@aplicacao.route("/cadastrar_usuario")
def formulario_cadastrar():
    return render_template("cadastro_usuario.html")

@aplicacao.route("/alterar_senha")
def formulario_alterar_senha():
    return render_template("alterar_senha.html")


aplicacao.register_blueprint(modulo_usuario)
aplicacao.register_blueprint(modulo_boletim_ocorrencia)
aplicacao.register_blueprint(modulo_relatorio_grafico)


if __name__ == "__main__":
    aplicacao.run(debug=True)
