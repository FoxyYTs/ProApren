CREATE TABLE `cliente` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `correo` VARCHAR(255) UNIQUE NOT NULL,
  `direccion` TEXT
);

CREATE TABLE `producto` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `descripcion` TEXT,
  `precio` DECIMAL(10,2) NOT NULL,
  `cantidad` INT NOT NULL
);

CREATE TABLE `pedido` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `fk_cliente_id` INT NOT NULL,
  `fecha_hora` DATETIME NOT NULL,
  `estado` VARCHAR(255) NOT NULL,
  `precio_total` DECIMAL(10,2) NOT NULL
);

CREATE TABLE `detalles_pedido` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `fk_pedido_id` INT NOT NULL,
  `fk_producto_id` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `precio_unitario` DECIMAL(10,2) NOT NULL
);

CREATE UNIQUE INDEX `unico_detalle` ON `detalles_pedido` (`fk_pedido_id`, `fk_producto_id`);

ALTER TABLE `pedido` ADD CONSTRAINT `fk_pedido_cliente` FOREIGN KEY (`fk_cliente_id`) REFERENCES `cliente` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE `detalles_pedido` ADD CONSTRAINT `fk_detalle_pedido` FOREIGN KEY (`fk_pedido_id`) REFERENCES `pedido` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `detalles_pedido` ADD CONSTRAINT `fk_detalle_producto` FOREIGN KEY (`fk_producto_id`) REFERENCES `producto` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
