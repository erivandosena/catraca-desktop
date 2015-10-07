#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Turno(object):
    
    def __init__(self):
        self.__turn_id = None
        self.__turn_hora_inicio = None
        self.__turn_hora_fim = None
        self.__turn_descricao = None
    
    @property
    def id(self):
        return self.__turn_id
    
    @id.setter
    def id(self, valor):
        self.__turn_id = valor
        
    @property
    def inicio(self):
        return self.__turn_hora_inicio
    
    @inicio.setter
    def inicio(self, valor):
        self.__turn_hora_inicio = valor
        
    @property
    def fim(self):
        return self.__turn_hora_fim
    
    @fim.setter
    def fim(self, valor):
        self.__turn_hora_fim = valor
        
    @property
    def descricao(self):
        return self.__turn_descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.__turn_descricao = valor
        