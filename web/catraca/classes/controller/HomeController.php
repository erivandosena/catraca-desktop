<?php


class HomeController{
	
	public static function main($nivelDeAcesso){
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				CatracaController::main($nivelDeAcesso);
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
		
	}
	
	
}


?>