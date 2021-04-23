"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros

def init_catalog():
    catalog = model.new_catalog()
    return catalog


# Funciones para la carga de datos


def load_data(catalog):
    load_videos(catalog)
    load_category_names(catalog)


def load_videos(catalog):
    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.add_video(catalog, video)


def load_category_names(catalog):
    category_names_file = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(category_names_file, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.add_category_name(catalog, category)

def get_most_view_videos(catalog,country_name,category_name):
    return model.get_most_view_videos(catalog,country_name,category_name)

def get_most_time_trending_country(catalog,country_name):
    return model.get_most_time_trending_country(catalog,country_name)

def get_most_time_trending_category(catalog,category_name):
    return model.get_most_time_trending_category(catalog,category_name)

def get_most_likes_tag(catalog,tag,country_name):
    return model.get_most_likes_tag(catalog,tag,country_name)  