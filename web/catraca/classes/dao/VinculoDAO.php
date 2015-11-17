<?php
/**
 *
 * Cadastro de vinculo ser� feito por dois usuarios diferetnes.
 * Administra��o ou Guiche. Com suas particularidades.
 *
 * A seguir o cadastro de vinculo pelo usuario administrador.
 *
 * 1- Verifica��o de Id de usuario de base externa.
 * Esse usuario existe na base local? Captura-se o Id da base local para: $idUsuarioBaseLocal;
 * N�o existe na base local: Cadastra-se e captura-se o id da base local para: $idUsuarioBaseLocal;
 *
 *
 *
 *
 * 2- Verifica��o de cart�o.
 * O cart�o existe. Verifica se o Tipo cooresponde. Faz UPDATE no tipo. Retorne o seu ID. 
 * O cart�o n�o existe. Cadastre e Retorne o seu ID. 
 * 
 * 
 *
 *
 *
 *
 * 3 - Verifica��o de vinculos do usuario.
 *
 *
 *
 * 4 - Verifica��o de vinculos do Cart�o.
 *
 *
 *
 * 5 - Adicionar vinculo novo vinculo. 
 *
 *
 *
 */
class VinculoDAO extends DAO {
	
	
	public function adicionaVinculo($idUsuarioBaseExterna, $numeroCartao, $dataDeValidade, $tipoCartao) {
		$idBaseLocal = $this->verificarUsuario($idUsuarioBaseExterna);
		echo'User'.$idBaseLocal;
		if(!$idBaseLocal)
			return 0;
		$numeroCartao = intval ( $numeroCartao);
		$tipoCartao = intval($tipoCartao);
		$idCartao = $this->verificaCartao($numeroCartao, $tipoCartao);
		if(!$idCartao)
			return 0;
		echo 'Card: '.$idCartao;
		$dataDeHoje = date("Y-m-d H:i:s");
		if($this->getConexao()->exec("INSERT into vinculo (usua_id, cart_id, vinc_refeicoes, vinc_avulso, vinc_inicio, vinc_fim) VALUES($idBaseLocal, $idCartao, 1,FALSE,'$dataDeHoje', '$dataDeValidade')")){
			echo 'Vinculo adicionado com sucesso ';
		}
	}
	public function adicionarVinculo($idUsuario, $idCartao, $dataValidade){
		
	}
	public function verificarVinculoUsuario($idUsuario){
		
	}
	public function verificarVinculoCartao($idCartao){
		
	}
	
	
	/**
	 * Atrav�s de um numero de cart�o iremos retornar seu verdadeiro ID. 
	 * Mas antes iremos alterar seu tipo. 
	 * 
	 * Caso ele nem exista a gente cadastra com o tipo oferecido aqui. 
	 * 
	 * @param int $numeroCartao
	 * @param int $idTipo
	 */
	public function verificaCartao($numeroCartao, $idTipo){
		$numeroCartao = intval($numeroCartao);
		$idTipo = intval($idTipo);
		
		$result = $this->getConexao()->query("SELECT * FROM cartao WHERE cart_numero = $numeroCartao");
		foreach($result as $linha){
			if($linha['tipo_id'] != $idTipo)
				if(!$this->getConexao()->exec("UPDATE cartao set tipo_id = $idTipo WHERE cart_numero = $numeroCartao"))
					return false;
			return $linha['cart_id'];
		}
		if($this->getConexao()->query("INSERT INTO cartao(cart_numero, cart_creditos, tipo_id) VALUES($numeroCartao, 0, $idTipo)")){
			foreach($this->getConexao()->query("SELECT * FROM cartao WHERE cart_numero = $numeroCartao") as $otraLinha){
				return $otraLinha['cart_id'];
			}
		}
		return false;
		
		
	}
	/**
	 * 
	 * @param int $idBaseExterna
	 * @return int
	 */
	public function verificarUsuario($idBaseExterna){
		$idBaseExterna = intval ( $idBaseExterna );
		$result = $this->getConexao()->query("SELECT id_base_externa, usua_id FROM usuario WHERE id_base_externa = $idBaseExterna");
		foreach ($result as $linha){
			return $linha['usua_id'];
		}
		//Vamos pegar da base exter a ecopiar para a base local. 
		//Se Nem existir na base externa, � o usuario frescando. Preciso dar nem resposta pra ele. Aborto tudo logo.
		$daoSistemasComum = new DAO(null, DAO::TIPO_PG_SISTEMAS_COMUM);
		$result2 = 	$daoSistemasComum->getConexao()->query("SELECT * FROM vw_usuarios_autenticacao_catraca WHERE id_usuario = $idBaseExterna");
		foreach($result2 as $linha){
			//Fa�amos um insert aqui. 
			//Apos esse insert iremos pegar o id inserido na base e retornalo. 
			$nivel = Sessao::NIVEL_COMUM;
			$nome = $linha['nome'];
			$email = $linha['email'];
			$login = $linha['login'];
			$senha = $linha['senha'];
			$idBaseExterna = $linha['id_usuario'];
			if($this->getConexao()->exec("INSERT into usuario(usua_login,usua_senha, usua_nome,usua_email, usua_nivel, id_base_externa)
					VALUES	('$login', '$senha', '$nome','$email', $nivel, $idBaseExterna)"))
			{
				foreach($this->getConexao()->query("SELECT * FROM usuario WHERE id_base_externa = $idBaseExterna") as $linha3){
					return $linha3['usua_id'];
				}
				
			}
		}
		return 0;	
		//Retorna 0, deu nada certo. Essa parada acaba aqui. 
		
		
	}
	
	
}

?>