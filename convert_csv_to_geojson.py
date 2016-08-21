# -*- coding: utf-8 -*-

import csv
import json

geojson_file = "laposte.js"

with open("laposte_poincont2.csv", 'rb') as csvf:
    reader = csv.DictReader(csvf, delimiter=';')
    count = 0
    geojson = dict(type='FeatureCollection', features=[])

    for row in reader:
        print ("{} is located at {}".format(row['Libellé_du_site'], row.get('Adresse')))
        lat = row['Latitude']
        lng = row['Longitude']

        props = dict(identifiant_du_site=row.get('identifiant_du_site'),
                     libelle_du_site=row.get('Libellé_du_site').title(),
                     caracteristique_du_site=row.get('Caractéristique_du_site'),
                     adresse=row.get('Adresse'),
                     complement_d_adresse=row.get('Complément_d_adresse'),
                     lieu_dit=row.get('Lieu_dit').title(),
                     localite=row.get('Localité').title(),
                     code_postal=row.get('Code_postal'),
                     pays=row.get('Pays')
                     )
        geom = dict(type='Point',
                    coordinates=[lng, lat])
        feature = dict(type='Feature',
                       geometry=geom,
                       properties=props)

        geojson['features'].append(feature)

        count += 1
        # if count >= 20:
        #     break
        print("there is {} entries".format(count))
        with open(geojson_file, 'w') as f:
            f.write("var points = ")
            json.dump(geojson, open(geojson_file, 'awb'))
