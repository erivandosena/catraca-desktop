#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
<<<<<<< HEAD
<<<<<<< HEAD
from catraca.util import Util
=======
>>>>>>> remotes/origin/web_backend
=======
from catraca.util import Util
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.dao.tipo_dao import TipoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CartaoDAO(ConexaoGenerica):

    def __init__(self):
        super(CartaoDAO, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def busca(self, *arg):
        obj = Cartao()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao " +\
                "WHERE cart_id = " + str(id)
        elif id is None:
<<<<<<< HEAD
<<<<<<< HEAD
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao ORDER BY cart_id"
=======
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao"
>>>>>>> remotes/origin/web_backend
=======
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao ORDER BY cart_id"
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.numero = dados[1]
                        obj.creditos = dados[2]
<<<<<<< HEAD
<<<<<<< HEAD
                        obj.tipo = self.busca_por_tipo(obj)
=======
                        obj.tipo = TipoDAO().busca(dados[3])
>>>>>>> remotes/origin/web_backend
=======
                        obj.tipo = self.busca_por_tipo(obj)
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
                        return obj
                    else:
                        return None
                elif id is None:
                    list = cursor.fetchall()
                    if list != []:
                        return list
                    else:
                        return None
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
        finally:
            pass

    def busca_por_tipo(self, obj):
        return TipoDAO().busca(obj.id)
        
    def busca_por_numero(self, numero):
        obj = Cartao()
        sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao " +\
              "WHERE cart_numero = " + str(numero)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados is not None:
                    obj.id = dados[0]
                    obj.numero = dados[1]
                    obj.creditos = dados[2]
                    obj.tipo = self.busca_por_tipo(obj)
                    return obj
                else:
                    return None
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
        finally:
            pass
        
        
    def busca_cartao_valido(self, numero, data = None):
        if data is None:
            data = Util().obtem_datahora_postgresql()
        sql = "SELECT cartao.cart_id, cartao.cart_numero, cartao.cart_creditos, "+\
            "tipo.tipo_valor, vinculo.vinc_refeicoes, tipo.tipo_id FROM cartao " +\
            "INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id " +\
            "INNER JOIN vinculo ON vinculo.cart_id = cartao.cart_id " +\
            "WHERE ('"+str(data)+"' BETWEEN vinculo.vinc_inicio AND vinculo.vinc_fim) AND "  +\
            "(cartao.cart_numero = "+str(numero)+")"   
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                obj = cursor.fetchone()
                if obj:
                    return obj
                else:
                    return None
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
        finally:
            pass
        
    def busca_isencao(self, data = None):
        if data is None:
            data = Util().obtem_datahora_postgresql()
        sql = "SELECT isencao.isen_inicio, isencao.isen_fim FROM cartao " +\
        "INNER JOIN isencao ON isencao.cart_id = cartao.cart_id WHERE ('"+str(data)+"' "+\
        "BETWEEN isencao.isen_inicio AND isencao.isen_fim)" 
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                obj = cursor.fetchone()
                if obj:
                    return obj
                else:
                    return None
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
        finally:
            pass
  
<<<<<<< HEAD
=======
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
        finally:
            pass
        
    def busca_por_numero(self, *arg):
        obj = Cartao()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao " +\
                  "WHERE cart_numero = " + str(id)
        elif id is None:
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.numero = dados[1]
                        obj.creditos = dados[2]
                        obj.tipo = TipoDAO().busca(dados[3])
                        return obj
                    else:
                        return None
                elif id is None:
                    list = cursor.fetchall()
                    if list != []:
                        return list
                    else:
                        return None
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
        finally:
            pass
        
>>>>>>> remotes/origin/web_backend
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO cartao("\
                        "cart_id, "\
                        "cart_numero, "\
                        "cart_creditos, "\
                        "tipo_id) VALUES (" +\
                        str(obj.id) + ", " +\
                        str(obj.numero) + ", " +\
                        str(obj.creditos) + ", " +\
                        str(obj.tipo) + ")"
                self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    #self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('Erro realizando INSERT na tabela cartao.', exc_info=True)
#             return False
<<<<<<< HEAD
=======
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela cartao.', exc_info=True)
            return False
>>>>>>> remotes/origin/web_backend
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
        finally:
            pass
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
                    if obj.id:
                        sql = "DELETE FROM cartao WHERE cart_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM cartao"
<<<<<<< HEAD
=======
                    sql = "DELETE FROM cartao WHERE cart_id = " + str(obj.id)
>>>>>>> remotes/origin/web_backend
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
                    self.aviso = "Excluido com sucesso!"
                else:
                    sql = "UPDATE cartao SET " +\
                          "cart_numero = " + str(obj.numero) + ", " +\
                          "cart_creditos = " + str(obj.creditos) + ", " +\
                          "tipo_id = " + str(obj.tipo) +\
                          " WHERE "\
                          "cart_id = " + str(obj.id)
                    self.aviso = "Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    #self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('Erro realizando DELETE/UPDATE na tabela cartao.', exc_info=True)
#             return False
        finally:
            pass
        
    def mantem_cartao_off(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM cartao_off WHERE caof_id = " + str(obj.id)
                    self.aviso = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE cartao_off SET " +\
                              "caof_numero = " + str(obj.numero) + ", " +\
                              "caof_creditos = " + str(obj.creditos) + ", " +\
                              "tipo_id = " + str(obj.tipo) +\
                              " WHERE "\
                              "caof_id = " + str(obj.id)
                        self.aviso = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO cartao_off("\
                                "caof_numero, "\
                                "caof_creditos, "\
                                "tipo_id) VALUES (" +\
                                str(obj.numero) + ", " +\
                                str(obj.creditos) + ", " +\
                                str(obj.tipo) + ")"
                        self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela cartao_off.', exc_info=True)
<<<<<<< HEAD
=======
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela cartao.', exc_info=True)
>>>>>>> remotes/origin/web_backend
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
            return False
        finally:
            pass
        