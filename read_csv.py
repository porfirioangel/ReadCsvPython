import csv

# Nombre,Fecha,Latitud,Longitud,Costo,Flyer,Categoría

with open('FestivalCulturalZacatecas2018.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    line_count = 1

    for row in reader:
        print("        Evento::create([")
        print("            'id' => %d," % (line_count))
        print("            'nombre' => '%s'," % (row['Nombre']))
        print("            'fecha' => '%s'," % (row['Fecha']))
        print("            'latitud' => '%s'," % (row['Latitud']))
        print("            'longitud' => '%s'," % (row['Longitud']))
        print("            'costo' => '%s'," % (row['Costo']))
        print("            'url_flyer' => '/uploads/%s'," % (row['Flyer']))
        print("            'categoria_evento_id' => %s" % (row['Categoría']))
        print("        ]);")
        print()
        line_count += 1