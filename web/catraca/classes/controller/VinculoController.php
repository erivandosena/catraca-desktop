<?php
class VinculoController {
	public static function main($tela) {
		switch ($tela) {
			case Sessao::NIVEL_SUPER :
				
				$controller = new VinculoController ();
				$controller->telaVinculo ();
				/*
				 * Queremos
				 * um formulario de pesquisa.
				 * Ao digitar um nome, vamos buscar.
				 * Temos uma lista que tras SIAP, Matricula, Nome, documentos.
				 * Vamos fazer o teste.
				 *
				 */
				
				break;
			case Sessao::NIVEL_DESLOGADO :
				break;
			default :
				break;
		}
	}
	public function listagemVinculos() {
		$daoLocalTeste = new DAO ( null, DAO::TIPO_PG_LOCAL );
		$dataAtual = date ( "Y-m-d H:i:s" );
		$result = $daoLocalTeste->getConexao ()->query ( "SELECT * FROM usuario
				INNER JOIN vinculo
				ON vinculo.usua_id = usuario.usua_id
				INNER JOIN cartao ON cartao.cart_id = vinculo.cart_id
				INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id
				WHERE '$dataAtual' BETWEEN vinc_inicio AND vinc_fim
				" );
		echo '<table border="1">';
		echo '<tr><th>ID usuario</th>
					<th>Nome</th>
					<th>Tipo</th>
					<th>Cartao</th>
					<th>Inicio</th>
					<th>Vencimento</th>
							</tr>';
		
		foreach ($result as $linha ) {
			echo '<tr><td>' . $linha ['id_base_externa'] . '</td>
				<td>' . $linha ['usua_nome'] . '</td>
				<td>' . $linha ['tipo_nome'] . '</td>
				<td>' .$linha ['cart_numero'] . '</td>
				<td>' .$linha ['vinc_inicio'] . '</td>
				<td>' .$linha ['vinc_fim'] . '</td>
				</tr>';
		}
		echo '</table>';
		echo '<br><br>';
	}
	public function telaVinculo() {
		echo '<section id="navegacao">
										<!--Tabs-->
										<ul class="nav nav-tabs">
											<li role="presentation" class="active"><a href="#tab1" data-toggle="tab">Usu&aacute;rios</a></li>
											<li role="presentation" class=""><a href="#tab2" data-toggle="tab">Cart&otilde;es</a></li>
										</ul><div class="tab-content">';
		
		echo '<div class="tab-pane active" id="tab1">';
		

		
		if (isset ( $_POST ['nome'] )) {
			$pesquisa = preg_replace ('/[^a-zA-Z0-9\s]/', '', $_POST ['nome'] );
			$pesquisa = strtoupper ( $pesquisa );
			$sql = "SELECT * FROM vw_usuarios_catraca WHERE nome LIKE '%$pesquisa%'";
			$dao = new DAO ( null, DAO::TIPO_PG_SIGAAA );
			$result = $dao->getConexao ()->query ( $sql );
			echo '
											<div class="doze linhas">
												<br><h2 class="texto-preto">Resultado da busca:</h2>
											</div>
											<table class="tabela borda-vertical zebrada texto-preto">
												<thead>
											        <tr>
											            <th>Nome</th>
											            <th>CPF</th>
											            <th>Passaporte</th>
											            <th>Matrícula</th>
														<th>SIAPE</th>
											            <th>Selecionar</th>
											        </tr>
											    </thead>
												<tbody>';
			foreach ( $result as $linha ) {
				echo '<tr>';
				echo '<td>' . $linha ['nome'] . '</a></td>';
				echo '<td>' . $linha ['cpf_cnpj'] . '</td>';
				echo '<td>' . $linha ['passaporte'] . '</td>';
				echo '<td>' . $linha ['matricula_disc'] . '</td>';
				echo '<td>' . $linha ['siape'] . '</td>';
				echo '<td class="centralizado">
											            	<a href="?pagina=cartao&selecionado=' . $linha ['id_usuario'] . '"><span class="icone-checkmark texto-verde2 botao" title="Selecionar"></span></a>
											            </td>';
				echo '</tr>';
			}
			echo '<br>
											    </tbody>
											</table>
											<nav>
												<ul class="pager">
													<li><a href="#">Anterior</a></li>
													<li><a href="#">Próximo</a></li>
												</ul>
											</nav>
										';
		}
		if (isset ( $_GET ['selecionado'] )) {
			
			if (is_int ( intval ( $_GET ['selecionado'] ) ) && intval ( $_GET ['selecionado'] )) {
				$dao = new DAO ( null, DAO::TIPO_PG_SIGAAA );
				$id = intval ( $_GET ['selecionado'] );
				$sql = "SELECT * FROM vw_usuarios_catraca WHERE id_usuario = $id";
				$result = $dao->getConexao ()->query ( $sql );
				foreach ( $result as $row ) {
					echo '<div class="borda">
									        Nome: ' . $row ['nome'] . ' 
									     <br>Login: ' . $row ['login'] . '
									     <br>Id SIGAA: ' . $row ['id_usuario'] . '
									     <br> CPF: ' . $row ['cpf_cnpj'] . '
									     <br> Identidade: ' . $row ['identidade'] . '
									     <br> Passaporte: ' . $row ['passaporte'] . '
									     <br>SIAPE: ' . $row ['siape'] . '
									     <br>Status Servidor: ' . $row ['status_servidor'] . '
									     <br>Status Discente: ' . $row ['status_discente'] . '
									     <br>Matricula Discente: ' . $row ['matricula_disc'] . '
									     <br>Tipo de Usuario: ' . $row ['tipo_usuario'] . '
									     <br>Categoria: ' . $row ['categoria'] . '
									    
						</div>';
					
					break;
				}
				$dao->fechaConexao ();
				// $dao= new DAO(null, DAO::TIPO_PG_LOCAL);
				// Agora vamos pegar os vinculos ativos desse usuario.
				$dao = new DAO ( null, DAO::TIPO_PG_LOCAL );
				// $daoLocalTeste->getConexao()->exec("UPDATE usuario set usua_nivel = 3 WHERE usua_login = 'acleber'");
				
				$dataTimeAtual = date ( "Y-m-d G:i:s" );
				$result = $dao->getConexao ()->query ( "SELECT * FROM usuario INNER JOIN vinculo
								ON vinculo.usua_id = usuario.usua_id
								LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
								LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id WHERE (usuario.id_base_externa = $id) 
						AND ('$dataTimeAtual' BETWEEN vinc_inicio AND vinc_fim)" );
				echo '<div class="borda">
						<table class="tabela borda-vertical zebrada texto-preto">';
				echo '<tr>
								<th>ID usuario</th>
								<th>Nome</th>
								<th>Tipo</th>
								<th>Cartao</th>
								<th>Inicio</th>
								<th>Fim</th>
						
							</tr>';
				foreach ( $result as $linha ) {
					echo '<tr>
							<td>' . $linha ['id_base_externa'] . '</td>
							<td>' . $linha ['usua_nome'] . '</td>
							<td>' . $linha ['tipo_nome'] . '</td>
							<td>' . $linha ['cart_numero'] . '</td>
							<td>' . $linha ['vinc_inicio'] . '</td>
							<td>' . $linha ['vinc_fim'] . '</td>
									</tr>';
				}
				echo '</table>
						</div>';
				if (isset ( $_GET ['cartao'] ) && isset ( $_GET ['selecionado'] )) {
					$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'H:00:01' );
					
					echo '<div class="borda">
							<form method="post" action="" class="formulario sequencial texto-preto" >																				
									    <label for="campo-texto-1">
									        Cartão: <input type="text" name="numero_cartao" id="cartao" />
									    </label>
									    <label for="campo-texto-1">
									        Validade: <input type="datetime-local" name="data_validade" value="' . $daqui3Meses . '" />
									    </label>
									     <label for="tipo">Tipo</label>
									       <select id="tipo" name="tipo">';
					$pesquisaTipos = $dao->getConexao ()->query ( "SELECT * FROM tipo" );
					foreach ( $pesquisaTipos as $linhaTipos ) {
						echo '<option value="' . $linhaTipos ['tipo_id'] . '">' . $linhaTipos ['tipo_nome'] . '</option>';
					}
					
					echo '
									        			
									        </select><br>
									    
									    <fieldset>
									        <legend>Cartão Avulso:</legend>
									        <label for="checkbox-1.1">
									            <input type="checkbox" name="checkbox-1" id="checkbox-1.1" value="1" /> Sim
									        </label>									        
									    </fieldset>
										<label for="campo-texto-1">
									        Quantidade de refeições: <input type="text" name="quantidade_refeicoes" id="periodo" />
									    </label><br>
										<input type="hidden" name="id_base_externa"  value="' . $_GET ['selecionado'] . '"/>
									   	<input type="submit"  name="salvar" value="Salvar"/>
									</form>
									</div>';
				} else {
					echo '<a class="botao" href="?pagina=cartao&selecionado=' . $_GET ['selecionado'] . '&cartao=add">Adicionar</a>';
				}
				if (isset ( $_POST ['salvar'] )) {
					
					// Todos os cadastros inicialmente ser�o n�o avulsos.
					$validade = $_POST ['data_validade'];
					$numeroCartao = $_POST ['numero_cartao'];
					$usuarioBaseExterna = $_POST ['id_base_externa'];
					$tipoCartao = $_POST ['tipo'];
					$vinculoDao = new VinculoDAO ( $dao->getConexao () );
					$vinculoDao->adicionaVinculo ( $usuarioBaseExterna, $numeroCartao, $validade, $tipoCartao );
					// No final eu redireciono para a pagina de selecao do usuario.
					echo '<meta http-equiv="refresh" content="3; url=.\?pagina=cartao&selecionado=' . $_POST ['id_base_externa'] . '">';
				}
			}
		}
		
		echo '</div>';
		
		echo '<div class="tab-pane" id="tab2">		Teste</div>';
		
		echo '</div>';
	}
}

?>