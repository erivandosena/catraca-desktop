<?php


class VinculoDAO extends DAO{
	
	
	/**
	 *
	 *Cadastro de vinculo ser� feito por dois usuarios diferetnes. 
	 *Administra��o ou Guiche. Com suas particularidades. 
	 *
	 *A seguir o cadastro de vinculo pelo usuario administrador. 
	 *
	 * 1-  Verifica��o de Id de usuario de base externa.
	 * 
	 * Esse usuario existe na base local? Captura-se o Id da base local para: $idUsuarioBaseLocal;
	 * N�o existe na base local: Cadastra-se e captura-se o id da base local para: $idUsuarioBaseLocal;
	 *
	 * 2- Verifica��o de cart�o. 
	 * 
	 * 
	 * 
	 * @param int $idUsuarioBaseExterna
	 * @param Vinculo $vinculo
	 */
	public function adicionaVinculo($idUsuarioBaseExterna, Vinculo $vinculo){
		
		$idUsuarioBaseExterna = intval($idUsuarioBaseExterna);
		
		
		
	}
	
	
}

?>