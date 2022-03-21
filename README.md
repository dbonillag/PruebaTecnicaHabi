# PruebaTecnicaHabi

Prueba Tecnica para el proceso de selección de Habi.

## Busqueda de propiedades

Para el desarrollo de la prueba se siguio un patrón red-green-refactor basada en el TDD. El primer paso fue diseñar los test de tal forma que cubrieran los casos de uso propuestos y fallaran al no estar la logica de negocio desarrollada, luego se desarrollo la logica y se aseguró que todas las pruebas pasaran, posteriormente se refactorizó el código refinando cualquier detalle faltante.

### Tecnologias Utilizadas

**Cherrypy**: Con el fin de cumplir lo propuesto para la prueba para la creación de las peticiones http se utilizó la libreria cherrypy, la cual mantiene un diseño minimalista y no ofrece mucho mas de lo que se define en RFC 7231.

**mysql-connector**: Libreria que permite conectarse a la base de datos mySql y por medio de la cual se pueden ejecutar las queries sin usar un ORM de por medio.

**unittest**: Libreria que permite realizar las pruebas unitarias.

### Estructura del endpoint

{{URL}}/search_properties?status=xx&city=xx&year=xx

#### Query Strings

**status**: ID del estado, por ejemplo: 3, que corresponde a pre-venta

**city**: Nombre de la ciudad, por ejemplo: bogota

**year**: Año de construcción del inmueble, por ejemplo: 2011



## Sistema de me gusta

### Diagrama Propuesto

![image](https://user-images.githubusercontent.com/42416371/159331190-14dfe6ea-a79d-4ca5-b3eb-0c92808feef8.png)

### Codigo Sql para extender el modelo
```sql
CREATE TABLE `like_history`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `like_date` datetime NULL,
  `property_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`)
);

ALTER TABLE `like_history` ADD CONSTRAINT `like_history_property_id_key` FOREIGN KEY (`property_id`) REFERENCES `property` ();
ALTER TABLE `like_history` ADD CONSTRAINT `like_history_user_id_key` FOREIGN KEY (`user_id`) REFERENCES `auth_user` ();
```

### Sustentación

Se plantea el siguiente modelo que permite tener un registro de likes, donde un usuario puede dar like a multiples propiedades y una propiedad puede recibir likes de multiples usuarios. Ademas se lleva un registro de la fecha del like.

para la tabla like_history se planteo usar una llave compuesta(property_id, user_id), lo cual al final no se hizo debido a la posibilidad de que se desee almacenar distintos eventos de like de un usuario al mismo inmueble.

## Propuesta modelo base de datos

### Propuesta 1

![image](https://user-images.githubusercontent.com/42416371/159334782-1c4e4dc9-d985-4d67-82d9-a6c169e0ee39.png)

Se propone el siguiente modelo con el fin de simplicar la relación entre la propiedad y su estado real, de esta forma si solo se desea obtener el estado se puede acceder directamente por esta relación.

### Propuesta 2

![image](https://user-images.githubusercontent.com/42416371/159335986-f5e79d14-e130-4247-ac65-5f2499b4f864.png)

La otra propuesta consiste en añadir el campo current a la tabla status history para obtener de forma mas veloz los estados actuales por propiedad.
