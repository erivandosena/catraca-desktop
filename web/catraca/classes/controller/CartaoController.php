<?php


class CartaoController{
	
	public static function main($nivelDeAcesso){
		
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				$controller = new CartaoController();
				$controller->telaCartao();
				
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	
	
	public function telaCartao(){
		
		$view = new CartaoView();
		
		echo '<section id="navegacao">
										<ul class="nav nav-tabs">
											<li role="presentation" class="active"><a href="#tab1" data-toggle="tab">Usu&aacute;rios</a></li>
											<li role="presentation" class=""><a href="#tab2" data-toggle="tab">Cart&otilde;es</a></li>
											<li role="presentation" class=""><a href="#tab3" data-toggle="tab">Isentos</a></li>
										</ul><div class="tab-content">';
		
		echo '<div class="tab-pane active" id="tab1">';
		
		$view->formBuscaUsuarios();
		if (isset ( $_POST ['nome'] )) {
			$usuarioDao = new UsuarioDAO(null, DAO::TIPO_PG_SIGAAA);
			$listaDeUsuarios = $usuarioDao->pesquisaNoSigaa($_POST ['nome']);
			$view->mostraResultadoBuscaDeUsuarios($listaDeUsuarios);
			$usuarioDao->fechaConexao();
		}
		if (isset ( $_GET ['selecionado'] )) {
			$idDoSelecionado = intval($_GET['selecionado']);
			
			$usuarioDao = new UsuarioDAO(null, DAO::TIPO_PG_SIGAAA);
			$usuario = new Usuario();
			$usuario->setIdBaseExterna($idDoSelecionado);
			$usuarioDao->retornaPorIdBaseExterna($usuario);
			$view->mostraSelecionado($usuario);
			$vinculoDao = new VinculoDAO(null, DAO::TIPO_PG_LOCAL);
			$vinculos = $vinculoDao->retornaVinculosValidosDeUsuario($usuario);
			$view->mostraVinculos($vinculos);
			
			if (!isset ( $_GET ['cartao'] )){
				echo '<a class="botao" href="?pagina=cartao&selecionado=' . $idDoSelecionado . '&cartao=add">Adicionar</a>';
			}else{
				$tipoDao = new TipoDAO($vinculoDao->getConexao());
				$listaDeTipos = $tipoDao->retornaLista();
				$view->mostraFormAdicionarVinculo($listaDeTipos, $idDoSelecionado);
				
			}
			if (isset ( $_POST ['salvar'] )) {
				
				// Todos os cadastros inicialmente ser�o n�o avulsos.
				$validade = $_POST ['data_validade'];
				$numeroCartao = intval($_POST ['numero_cartao']);
				$usuarioBaseExterna = intval($_POST ['id_base_externa']);
				$tipoCartao = $_POST ['tipo'];
				$vinculoDao->adicionaVinculo ( $usuarioBaseExterna, $numeroCartao, $validade, $tipoCartao );
				// No final eu redireciono para a pagina de selecao do usuario.
				echo '<meta http-equiv="refresh" content="3; url=.\?pagina=cartao&selecionado=' . $usuarioBaseExterna . '">';
			}
			$usuarioDao->fechaConexao();
			$vinculoDao->fechaConexao();
		}
		
		
		echo '</div>';
		
		echo '<div class="tab-pane" id="tab2">Teste</div>';
		echo '<div class="tab-pane" id="tab3">Isentos</div>';
		
		echo '</section>';
		
	}
	
	
	
	
}



?>