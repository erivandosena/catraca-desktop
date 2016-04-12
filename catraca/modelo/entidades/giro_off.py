#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class GiroOff(object):
    
    def __init__(self):
        self.__giof_id = None
        self.__giof_giros_horario = None
        self.__giof_giros_antihorario = None
        self.__giof_data_giros = None
        self.__catraca = None
    
    @property
    def id(self):
        return self.__giof_id
    
    @id.setter
    def id(self, valor):
        self.__giof_id = valor

    @property
    def horario(self):
        return self.__giof_giros_horario
    
    @horario.setter
    def horario(self, valor):
        self.__giof_giros_horario = valor
        
    @property
    def antihorario(self):
        return self.__giof_giros_antihorario
    
    @antihorario.setter
    def antihorario(self, valor):
        self.__giof_giros_antihorario = valor
        
    @property
    def data(self):
        return self.__giof_data_giros
    
    @data.setter
    def data(self, valor):
        self.__giof_data_giros = valor
        
    @property
    def catraca(self):
        return self.__catraca

    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
        