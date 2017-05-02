#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script para extraer etiquetas meta de páginas web"""
__author__ = 'John J. Villavicencio Sarango'

import time
import re
import csv
import os
import os.path as path
import datetime
import codecs
from bs4 import BeautifulSoup
import requests


def obtener_meta_tag(pagina_web):
    """Función obtener etiquetas meta"""


    #Armar url para scrapear posibles perfiles
    url_base = pagina_web

    print ('===================================')
    print (u'Link scrapy: %s \n' % url_base)

    # Realizamos la petición a la web
    req = requests.get(url_base)
    # Comprobamos que la petición nos devuelve un Status Code = 200
    status_code = req.status_code

    lista = []

    if status_code == 200:

            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(req.text, "lxml")

            # Obtenemos todos los divs donde estan los perfiles
            entradas = html.find_all('head')

            # Recorremos todas las entradas para extraer el Nombre del perfil,
            # el link, y sus atributos
            for entrada in entradas:
                #Armamos la URL de los posibles perfiles
                meta_tag = entrada.find_all('meta')
                
                counter = 0
                for tag in meta_tag:
                    counter += 1
                    lista.append((counter, tag))
            
            print (u'Total de tags: %d \n' % counter)                          
            print ('===================================')

            # Abrimos archivo temporal para almacenar
            csvsalida = open('META_TAGS.csv', 'a')
            salida = csv.writer(csvsalida)
            salida.writerow(['CONT', 'META'])
            salida.writerows(lista)
            del salida
            csvsalida.close()

obtener_meta_tag('http://stackoverflow.com/questions/36768068/get-meta-tag-content-property-with-beautifulsoup-and-python')
