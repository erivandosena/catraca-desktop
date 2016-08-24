#!/usr/bin/env python
# -*- coding: latin-1 -*-


# from contextlib import closing
from catraca.logs import Logs
from catraca.util import Util
# from catraca.modelo.dados.conexao import ConexaoFactory
# from catraca.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.registro import Registro
# from catraca.modelo.dao.cartao_dao import CartaoDAO
#from catraca.modelo.dao.turno_dao import TurnoDAO
# from catraca.modelo.dao.catraca_dao import CatracaDAO
# from catraca.modelo.dao.vinculo_dao import VinculoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class RegistroDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(RegistroDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        if arg:
            sql = "SELECT "\
                "regi_id as id, "\
                "regi_data as data, "\
                "regi_valor_pago as pago, "\
                "regi_valor_custo as custo, "\
                "cart_id as cartao, "\
                "catr_id as catraca, "\
                "vinc_id as vinculo "\
                "FROM registro WHERE "\
                "regi_id = %s"
        else:
            sql = "SELECT "\
                "regi_id as id, "\
                "regi_data as data, "\
                "regi_valor_pago as pago, "\
                "regi_valor_custo as custo, "\
                "cart_id as cartao, "\
                "catr_id as catraca, "\
                "vinc_id as vinculo "\
                "FROM registro ORDER BY regi_id"
        return self.seleciona(Registro, sql, arg)
    
#     def busca_por_turno(self, obj):
#         return TurnoDAO().busca(obj.id)
    
    def busca_utilizacao(self, hora_ini, hora_fim, cartao_id):
        data = Util().obtem_datahora()
        data_ini = str(data.strftime("%Y-%m-%d")) + " " + str(hora_ini)
        data_fim = str(data.strftime("%Y-%m-%d")) + " " + str(hora_fim)
        sql = "SELECT "\
            "COUNT(regi_data) "\
            "FROM registro "\
            "WHERE "\
            "regi_data BETWEEN %s AND %s AND cart_id = %s"
        return self.seleciona(Registro, sql, data_ini, data_fim, cartao_id)
    
#     def busca_utilizacao(self, hora_ini, hora_fim, cartao_id):
#         data = Util().obtem_datahora()
#         data_ini = str(data.strftime("%Y-%m-%d")) + " " + str(hora_ini)
#         data_fim = str(data.strftime("%Y-%m-%d")) + " " + str(hora_fim)
#         sql = "SELECT COUNT(regi_data) FROM registro " +\
#             "WHERE (regi_data BETWEEN '"+ str(data_ini) +"' "\
#             "AND '"+ str(data_fim) +"') "\
#             "AND (cart_id = "+str(cartao_id)+")"
#         print "=" * 100
#         print sql
#         print "=" * 100
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 obj = cursor.fetchone()
#                 if obj[0] > 0:
#                     return obj[0]
#                 else:
#                     return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[registro] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass    
     
    def busca_por_periodo(self, data_ini, data_fim):
        sql = "SELECT "\
            "regi_id as id, "\
            "regi_data as data, "\
            "regi_valor_pago as pago, "\
            "regi_valor_custo as custo, "\
            "cart_id as cartao, "\
            "catr_id as catraca, "\
            "vinc_id as vinculo "\
            "FROM registro WHERE "\
            "regi_data::timestamp::time BETWEEN %s AND %s"
        return self.seleciona(Registro, sql, data_ini, data_fim)
        
#     def busca_por_periodo(self, data_ini, data_fim):
#         sql = "SELECT regi_id, "\
#               "regi_data, "\
#               "regi_valor_pago, "\
#               "regi_valor_custo, "\
#               "cart_id, "\
#               "catr_id, "\
#               "vinc_id "\
#               "FROM registro WHERE "\
#               "regi_data::timestamp::time BETWEEN '" + str(data_ini) + "' AND '" + str(data_fim) +"'"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 list = cursor.fetchall()
#                 if list != []:
#                     return list
#                 else:
#                     return None
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('[registro] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass

    def busca_ultimo_registro(self):
        sql = "SELECT MAX(regi_id) FROM registro"
        obj = self.seleciona(Registro, sql)
        return obj[0][0] if obj[0][0] else 0
    
#     def busca_ultimo_registro(self):
#         sql = "SELECT MAX(regi_id) FROM registro"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 obj = cursor.fetchone()
# #                 if obj != (None,):
#                 if obj[0] > 0:
#                     return obj[0]
#                 else:
#                     return 0
#                  
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[registro] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
    
    def insere(self, obj):
        sql = "INSERT INTO registro "\
            "("\
            "cart_id, "\
            "catr_id, "\
            "regi_valor_custo, "\
            "regi_data, "\
            "regi_id, "\
            "regi_valor_pago, "\
            "vinc_id "\
            ") VALUES ("\
            "%s, %s, %s, %s, %s, %s, %s)"
        return self.inclui(sql, obj)
     
    def atualiza(self, obj):
        sql = "UPDATE registro SET "\
            "cart_id = %s, "\
            "catr_id = %s, "\
            "regi_valor_custo = %s, "\
            "regi_data = %s, "\
            "regi_valor_pago = %s, "\
            "vinc_id = %s "\
            "WHERE regi_id = %s"
        return self.altera(sql, obj)
     
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM registro"
        if obj:
            sql = str(sql) + " WHERE regi_id = %s"
        return self.deleta(sql, obj)
     
    def atualiza_exclui(self, obj, boleano):
        if obj or boleano:
            if boleano:
                if obj is None:
                    return self.exclui()
                else:
                    self.exclui(obj)
            else:
                return self.atualiza(obj)
        
#     def busca(self, *arg):
#         obj = Registro()
#         id = None
#         for i in arg:
#             id = i
#         if id:
#             sql = "SELECT regi_id, regi_data, regi_valor_pago, regi_valor_custo, " +\
#             "cart_id, catr_id, vinc_id FROM registro WHERE regi_id = " + str(id)
#         elif id is None:
#             sql = "SELECT regi_id, regi_data, regi_valor_pago, regi_valor_custo, " +\
#             "cart_id, catr_id, vinc_id FROM registro ORDER BY regi_id"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 if id:
#                     dados = cursor.fetchone()
#                     if dados is not None:
#                         obj.id = dados[0]
#                         obj.data = dados[1]
#                         obj.pago = dados[2]
#                         obj.custo = dados[3]
#                         obj.cartao = dados[4]
#                         obj.catraca = dados[5]
#                         obj.vinculo = dados[6]
#                         return obj
#                     else:
#                         return None
#                 elif id is None:
#                     list = cursor.fetchall()
#                     if list != []:
#                         return list
#                     else:
#                         return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[registro] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#   
# #     def busca_por_cartao(self, obj):
# #         return CartaoDAO().busca(obj.id)
#         
#     def busca_por_turno(self, obj):
#         return TurnoDAO().busca(obj.id)
#         
# #     def busca_por_catraca(self, obj):
# #         return CatracaDAO().busca(obj.id)
#     
# #     def busca_por_vinculo(self, obj):
# #         return VinculoDAO().busca(obj.id)
#     
#     def busca_utilizacao(self, hora_ini, hora_fim, cartao_id):
#         data = Util().obtem_datahora()
#         data_ini = str(data.strftime("%Y-%m-%d")) + " " + str(hora_ini)
#         data_fim = str(data.strftime("%Y-%m-%d")) + " " + str(hora_fim)
#         sql = "SELECT COUNT(regi_data) FROM registro " +\
#             "WHERE (regi_data BETWEEN '"+ str(data_ini) +"' "\
#             "AND '"+ str(data_fim) +"') "\
#             "AND (cart_id = "+str(cartao_id)+")"
#         print "=" * 100
#         print sql
#         print "=" * 100
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 obj = cursor.fetchone()
#                 if obj[0] > 0:
#                     return obj[0]
#                 else:
#                     return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[registro] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass    
#     
#     def busca_por_periodo(self, data_ini, data_fim):
#         sql = "SELECT regi_id, "\
#               "regi_data, "\
#               "regi_valor_pago, "\
#               "regi_valor_custo, "\
#               "cart_id, "\
#               "catr_id, "\
#               "vinc_id "\
#               "FROM registro WHERE "\
#               "regi_data::timestamp::time BETWEEN '" + str(data_ini) + "' AND '" + str(data_fim) +"'"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 list = cursor.fetchall()
#                 if list != []:
#                     return list
#                 else:
#                     return None
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('[registro] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#           
#     def busca_ultimo_registro(self):
#         sql = "SELECT MAX(regi_id) FROM registro"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 obj = cursor.fetchone()
# #                 if obj != (None,):
#                 if obj[0] > 0:
#                     return obj[0]
#                 else:
#                     return 0
#                 
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[registro] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
# 
#     def insere(self, obj):
#         try:
#             if obj:
#                 if obj.id is None:
#                     sql = "INSERT INTO registro("\
#                           "regi_data, "\
#                           "regi_valor_pago, "\
#                           "regi_valor_custo, "\
#                           "cart_id, "\
#                           "catr_id, "\
#                           "vinc_id) VALUES ('" +\
#                           str(obj.data) + "', " +\
#                           str(obj.pago) + ", " +\
#                           str(obj.custo) + ", " +\
#                           str(obj.cartao) + ", " +\
#                           str(obj.catraca) + ", " +\
#                           str(obj.vinculo) + ")"
#                 else:
#                     sql = "INSERT INTO registro("\
#                           "regi_id, "\
#                           "regi_data, "\
#                           "regi_valor_pago, "\
#                           "regi_valor_custo, "\
#                           "cart_id, "\
#                           "catr_id, "\
#                           "vinc_id) VALUES (" +\
#                           str(obj.id) + ", '" +\
#                           str(obj.data) + "', " +\
#                           str(obj.pago) + ", " +\
#                           str(obj.custo) + ", " +\
#                           str(obj.cartao) + ", " +\
#                           str(obj.catraca) + ", " +\
#                           str(obj.vinculo) + ")"
#                 self.aviso = "[registro] Inserido com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[registro] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[registro] Erro realizando INSERT.', exc_info=True)
#             return False
#         finally:
#             pass
#         
#     def atualiza_exclui(self, obj, delete):
#         try:
#             if obj or delete:
#                 if delete:
#                     if obj:
#                         sql = "DELETE FROM registro WHERE regi_id = " + str(obj.id)
#                     else:
#                         sql = "DELETE FROM registro"
#                     self.aviso = "[registro] Excluido com sucesso!"
#                 else:
#                     sql = "UPDATE registro SET " +\
#                           "regi_data = '" + str(obj.data) + "', " +\
#                           "regi_valor_pago = " + str(obj.pago) + ", " +\
#                           "regi_valor_custo = " + str(obj.custo) + ", " +\
#                           "cart_id = " + str(obj.cartao) + ", " +\
#                           "catr_id = " + str(obj.catraca) + ", " +\
#                           "vinc_id = " + str(obj.vinculo) +\
#                           " WHERE "\
#                           "regi_id = " + str(obj.id)
#                     self.aviso = "[registro] Alterado com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[registro] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[registro] Erro realizando DELETE/UPDATE.', exc_info=True)
#             return False
#         finally:
#             pass
        
        