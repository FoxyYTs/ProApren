SELECT nombre FROM producto
SELECT nombre, precio FROM producto
SELECT * FROM producto
SELECT nombre, precio*0.00026 ,precio*0.00024 FROM producto
SELECT upper(nombre), precio FROM producto
SELECT lower(nombre), precio FROM producto
SELECT * FROM fabricante ORDER BY nombre ASC
SELECT * FROM fabricante ORDER BY nombre DESC
SELECT * FROM producto ORDER BY nombre ASC, SELECT * FROM producto ORDER BY precio DESC
SELECT * FROM fabricante LIMIT 5
SELECT * FROM producto WHERE id_fabricante IN (2)
SELECT * FROM producto WHERE precio <= 120
SELECT * FROM producto WHERE precio >= 400
SELECT * FROM producto WHERE precio < 400
SELECT * FROM producto WHERE precio>=80 AND precio<=300;
SELECT * FROM producto WHERE precio BETWEEN 60 AND 200
SELECT * FROM producto WHERE precio > 200 AND id_fabricante IN (6)
SELECT * FROM producto WHERE id_fabricante IN (1,3,5)
SELECT * FROM fabricante WHERE nombre LIKE "s%"
SELECT * FROM fabricante WHERE nombre LIKE "%e"
SELECT * FROM fabricante WHERE nombre LIKE "%w%"
SELECT * FROM fabricante WHERE LENGTH(nombre) <= 4
SELECT * FROM producto WHERE nombre LIKE "%portatil%"
SELECT * FROM producto WHERE nombre LIKE "%monitor%" AND precio < 215
SELECT nombre, precio FROM producto WHERE precio >= 180 ORDER BY precio DESC, SELECT nombre, precio FROM producto WHERE precio >= 180 ORDER BY nombre ASC